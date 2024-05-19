import socket
import psutil
import time
import datetime
import traceback
import platform
from datetime import datetime

from monit import config


def build_json(err=None, init_time=None):
    data = {
        "project": config.project,
        "company": config.company,
        "location": config.location,
        "dev": config.dev,
        "stderr": bool(err),
        "phone": config.phone
    }

    if init_time:
        fim = datetime.now()
        total_time = fim - init_time
        data["runtime"] = total_time.total_seconds()
        data["date_init"] = init_time.isoformat()
        data["date_end"] = fim.isoformat()

    data["cpu"] = _get_cpu_usage()
    data["mem"] = _get_memory_usage()
    data["disk"] = _get_disk_usage()
    data["ping"] = _ping_host()
    data["system"] = platform.system()

    if err:
        error = str(err).replace('\n', '')
        data["error"] = error
        _print_error_to_console(err)

    return data

def _print_error_to_console(err):
    if err:
        tb = traceback.extract_tb(err.__traceback__)
        filename, line, func, text = tb[-1]
        strerror = f"{func}: File \"{filename}\", line {line}\n\t{text}\n\n"
        print(strerror)

def _ping_host():
    host = '1.1.1.1'
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            start_time = time.time()
            s.connect((host, 80))
            end_time = time.time()
            rtt = (end_time - start_time) * 1000
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
