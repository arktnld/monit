import socket
import psutil
import time
import datetime
import traceback
from math import floor
import platform
from datetime import datetime
import smtplib
from email.message import EmailMessage

from monit import config


def build_table(err, table, init_time):

        table.project = config.project
        table.company = config.company
        table.dev = config.dev
        table.stderr = bool(err)

        fim = datetime.now()

        total_time = fim - init_time
        table.runtime = total_time.total_seconds()
        table.date_init = init_time
        table.date_end = fim

        table.cpu = _get_cpu_usage()
        table.mem = _get_memory_usage()
        table.disk = _get_disk_usage()
        table.ping = _ping_host()
        table.system = platform.system()

        if err:
            error = str(err).replace('\n', '')

            # table.type = type
            table.error = error

            _print_error_to_console(err)
            _send_email_notification(error)

        return table

def _print_error_to_console(err):
    # Imprime o erro no console.
    if err:
        # error_type = type(err).__name__
        tb = traceback.extract_tb(err.__traceback__)
        filename, line, func, text = tb[-1]
        strerror = f"File \"{filename}\", line {line}\n\t{text}\n\nError: {err}"
        print(strerror)

def _send_email_notification(err):
    # Envia um e-mail com o erro.
    if config.email and config.email_password:
        message = f"{config.company}\n{config.project}\n\n{err}"

        if err:
            msg = EmailMessage()
            msg['subject'] = f'Error in {config.project} on {config.company}'
            msg['from'] = config.email
            msg['to'] = config.email
            msg.set_content(message)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(config.email, config.email_password)
                smtp.send_message(msg)

def _ping_host():
    host = '1.1.1.1'  # Host alvo para ping (por exemplo, google.com)
    try:
        # Cria um socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Define um tempo limite para a conexão
            s.settimeout(2)
            start_time = time.time()
            # Tenta se conectar ao host na porta 80 (HTTP)
            s.connect((host, 80))
            end_time = time.time()
            # Calcula o tempo de resposta
            rtt = (end_time - start_time) * 1000  # Convertendo para milissegundos
            return f"{round(rtt, 2):.0f}"
    except Exception as e:
        print("Erro ao pingar o host:", e)
        return None

def _get_disk_usage():
    disk = psutil.disk_usage('/')
    total_disk_space = disk.total
    used_disk_space = disk.used
    disk_percent = (used_disk_space / total_disk_space) * 100
    return f"{disk_percent:.0f}%"

def _get_cpu_usage():
    return f"{psutil.cpu_percent(interval=1):.0f}%"

def _get_memory_usage():
    mem = psutil.virtual_memory()
    return f"{mem.percent:.0f}%"

# Função para converter bytes em megabytes
def _bytes_to_mb(bytes):
    return bytes / (1024 * 1024)
