import os
import sys
import inspect
from datetime import datetime

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()  # Para garantir que a saída seja escrita imediatamente
    def flush(self):
        for f in self.files:
            f.flush()

class Log2File:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        self.start_logging()

    def start_logging(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Obtém o nome do arquivo que importou esta classe
        caller_filename = inspect.stack()[2].filename

        # Define o caminho completo para o arquivo de log
        caller_filename_without_extension = os.path.splitext(os.path.basename(caller_filename))[0]
        log_filename = caller_filename_without_extension + ".log"
        log_path = os.path.join(self.log_dir, log_filename)

        # Abre o arquivo de log em modo de adição para manter o conteúdo existente
        self.log_file = open(log_path, "a")

        # Redireciona a saída padrão (stdout e stderr) para o arquivo de log e para o terminal
        sys.stdout = Tee(sys.stdout, self.log_file)
        sys.stderr = Tee(sys.stderr, self.log_file)

# Inicializa o redirecionamento de log assim que o módulo for importado
# Log2File()

# # Exemplo de uso:
# if __name__ == "__main__":
#     # Seu código aqui...
#     print("Hello, world!")
#     x = 5
#     print("The value of x is:", x)
#     y = "not_an_integer"
#     try:
#         y = int(y)
#     except ValueError as e:
#         print("Erro ao converter para inteiro:", e)

# # O redirecionamento do log será finalizado automaticamente quando o script terminar de ser executado.
