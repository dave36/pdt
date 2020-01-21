import os
import sys
import nmap
import pprint

sys.path.append('src/04_Reporting/')
from report_log import *


def scan_siemens(target):
    os.system("python lib/s7scan/s7scan.py --log-dir reports/ --tcp " + target)


