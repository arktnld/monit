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
        monit.notify_and_exit(e)


if __name__ == "__main__":
    main()
```

**Utilização avançada**

```Python
from time import sleep

from monit.core import Monitor as monit
from monit.logger import Logger
from monit.log2file import Log2File

Log2File() # Salva todo o log em um arquivo
log = Logger()

def main():

    try:
        log.info("Hello, World!")

        sleep(2)
        raise ValueError("This is a sample error.")

    except Exception as e:
        monit.notify(e)

    monit.msg("O Script terminou com sucesso.") # whatsapp

    monit.end() # manda sinal de fim sem erros


if __name__ == "__main__":
    main()
```
