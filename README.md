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
PROJECT='project_name'
COMPANY='company_name'
DEV='coder'
LOCATION='location_name'
HANDLER_URL='https://example.com'
PHONE='556199999999'
```
### Exemplo de Uso:

**Utilização simples**
```python
import time

from monit.core import Monitor as monit

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

**Utilização avançada**

```Python
import time

from monit.core import Monitor as monit
from monit.logger import Logger
from monit.log2file import Log2File

def main():

    Log2File() # Salva todo o log em um arquivo
    log = Logger()

    try:
        log.info("Hello, World!")
        time.sleep(5)

        raise ValueError("This is a sample error.")

    except Exception as e:
        monit.notify(e)

    try:
        time.sleep(2)
        raise ValueError("This is another a sample error.")

    except Exception as e:
        monit.notify(e, "Custom message")

    num = 0
    for _ in range(3):
        num += 1
    monit.msg(f"Total count in for loop: {num}")

    monit.end()


if __name__ == "__main__":
    main()
```
