# Logger.py
import os
from datetime import datetime

LOGFILE = "{}/suspicious_domains.log".format(os.path.dirname(os.path.abspath(__file__)))

class Logger:
    def __init__(self, print_logs: bool = False, log_file: str = LOGFILE):
        self.print_logs=print_logs
        self.log_file = log_file

    def alert(self, message: str):
        with open(self.log_file, "a") as file:
            file.write("{} {}\n".format(datetime.now(), message))
        if self.print_logs:
            print(message)

    # not optimal to have three times the same function but handy from the user end
    def high(self, domain, authority):
        self.alert("[HIGH]  {}  {}".format(domain, authority))

    def medium(self, domain, authority):
        self.alert("[MEDIUM]  {}  {}".format(domain, authority))

    def low(self, domain, authority):
        self.alert("[LOW]  {}  {}".format(domain, authority))

