import socket
import psutil
import time
import csv
import datetime
import smtplib
import traceback
from email.message import EmailMessage
from math import floor
import platform
from datetime import datetime

from monit import config


def build_table(type, err, table, init_time):

        table.project = config.project
        table.company = config.company
        table.dev = config.dev
        table.date = datetime.now()

        if init_time:
            fim = time.perf_counter()
            tempo_execucao = floor(fim - init_time)
            table.runtime = tempo_execucao

            print_error_to_console(type, err)

        table.cpu = get_cpu_usage()
        table.mem = get_memory_usage()
        table.disk = get_disk_usage()
        table.system = platform.system()
        table.ping = ping_host()

        if err:
            error = str(err).replace('\n', '')
            # full_error = str(type) + ": " + str(error)

            table.type = type
            table.error = error
        else:
            table.type = ""
            table.error = ""

        return table

def print_error_to_console(type, err):
    # Imprime o erro no console.
    if err:
        # error_type = type(err).__name__
        tb = traceback.extract_tb(err.__traceback__)
        filename, line, func, text = tb[-1]
        strerror = f"File \"{filename}\", line {line}\n\t{text}\n\n{type}: {err}"
        print(strerror)



def ping_host():
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

def get_disk_usage():
    disk = psutil.disk_usage('/')
    total_disk_space = disk.total
    used_disk_space = disk.used
    disk_percent = (used_disk_space / total_disk_space) * 100
    return f"{disk_percent:.0f}%"

def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=1):.0f}%"

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"{mem.percent:.0f}%"

# Função para converter bytes em megabytes
def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)
