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
        monit.notify_and_exit(e) # para o script

    monit.end() # manda sinal de fim sem erros


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
        monit.msg("Ocorreu um erro, tentando de novo...") # Whatsapp
        monit.notify(e) # não para o script

        try:
            log.info("Tentando novamente...")

            sleep(2)
            raise ValueError("This is another error.")

        except Exception as e:
            monit.msg("Script terminou com erros.")
            monit.notify_and_exit(e)

    monit.end()


if __name__ == "__main__":
    main()
```

### Soluções de erros:

#### PdhAddEnglishCounterW failed. Performance counters may be disabled.

O erro ocorre porque os contadores de desempenho do Windows estão desativados ou corrompidos, causando a falha da função PdhAddEnglishCounterW.
Execute os seguintes comandos em um CMD com privilégios administrativos:

```cmd
lodctr /r
winmgmt /resyncperf
```
