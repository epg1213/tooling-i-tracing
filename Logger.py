# Logger.py
import os
from datetime import datetime

LOGFILE = "{}/suspicious_domains.log".format(os.path.dirname(os.path.abspath(__file__)))

class Logger:
    def __init__(self, print_logs: bool = False):
        self.print_logs=print_logs

    def alert(self, message: str):
        with open(LOGFILE, "a") as file:
            file.write("{} {}\n".format(datetime.now(), message))
        if self.print_logs:
            print(message)

    def high(self, domain, authority):
        self.alert("[HIGH]  {}  {}".format(domain, authority))

    def medium(self, domain, authority):
        self.alert("[MEDIUM]  {}  {}".format(domain, authority))

    def low(self, domain, authority):
        self.alert("[LOW]  {}  {}".format(domain, authority))

