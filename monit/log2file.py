import os
import sys
import inspect

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
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

        caller_filename = inspect.stack()[2].filename

        caller_filename_without_extension = os.path.splitext(os.path.basename(caller_filename))[0]
        log_filename = caller_filename_without_extension + ".log"
        log_path = os.path.join(self.log_dir, log_filename)

        self.log_file = open(log_path, "a")

        sys.stdout = Tee(sys.stdout, self.log_file)
        sys.stderr = Tee(sys.stderr, self.log_file)
