import os

# Função para verificar a existência do arquivo .env
def verify_env():
    if not os.path.exists('.monit'):
        raise FileNotFoundError("MonitError: Arquivo .monit não encontrado. Por favor, crie um arquivo .monit com as configurações necessárias.")
