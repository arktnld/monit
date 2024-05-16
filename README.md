### Monit

**Instalação:**
```bash
pip install pymonit
```
**Atualização:**
```bash
pip install -U pymonit
```
**Exemplo arquivo `.monit`:**
```bash
# Project info
# Informações obrigatórias
PROJECT=sample_project
COMPANY=acme
DEV=coder

# Database info
# Informações obrigatórias
DB_USER=user
DB_PASSWORD=p@ssw0rd
DB_HOST=localhost
DB_DATABASE=teste

# Email info
# Deixe em branco para desativar o envio de e-mails
EMAIL=
EMAIL_PASSWORD=
```
### Exemplo de Uso:

**Utilização do Monit para notificação de erros**
```python
#
#  IMPORTANTE: importar OS e entrar na pasta atual é obrigatório
#
import os

script_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(script_path))

import time

from monit.core import Monitor as monit
from monit.error import SetupError

def main():

    try:
        time.sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify_and_exit(e)


if __name__ == "__main__":
    main()
```

**Utilização do Monit para notificação de erros que
não são grandes o suficientes para exigir que o
processo seja interrompido.**

```Python
# sample.py

#
#  IMPORTANTE: importar OS e entrar na pasta atual é obrigatório
#
import os

script_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(script_path))

import time

from monit.core import Monitor as monit
from monit.error import SetupError
# from monit.logger import Logger
# from monit.log2file import Log2File

def main():
    # Initialize the Monitor
    monit = Monitor()

    # Log2File()
    # log = Logger()

    try:
        # Your code that might raise exceptions
        time.sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify(e)

    monit.end()


if __name__ == "__main__":
    main()
