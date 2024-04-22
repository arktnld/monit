# sample.py
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

    monit.end()


if __name__ == "__main__":
    main()
