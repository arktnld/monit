import os

# Função para verificar a existência do arquivo .env
def verify_env():
    if not os.path.exists('.env'):
        raise FileNotFoundError("Arquivo .env não encontrado. Por favor, crie um arquivo .env com as configurações necessárias.")
