### Monit

**Instalação:**
```bash
pip install monit-agd
```
**Exemplo arquivo `.env`:**
```bash
# Project info
PROJECT=sample_project
COMPANY=acme
LOCATION=ec2
DEV=coder

# Database info
DB_USER=user
DB_PASSWORD=p@ssw0rd
DB_HOST=localhost
DB_DATABASE=teste
```
**Exemplo de Uso:**
```Python
import time

from monit.core import Monitor
from monit.error import SetupError

def main():
    # Initialize the Monitor
    monit = Monitor()

    try:
        # Your code that might raise exceptions
        # For demonstration purposes, let's raise an exception
        time.sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        # Notify the Monitor about the error
        monit.notify(SetupError, e)
        # monit.notify_and_exit(SetupError, e)

    monit.end()


if __name__ == "__main__":
    main()
```
**Tipos de erros:**
```bash
SetupError
DatabaseError
HTTPError
FileError
FolderError
TooManyRequests
```
