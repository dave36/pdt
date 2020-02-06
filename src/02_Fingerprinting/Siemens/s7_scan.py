import os
import sys
import nmap
import pprint

sys.path.append('src/04_Reporting/')
from report_log import *


def scan_siemens(target):
    """Function to scan s7 devices
    :params
		target - The address of the siemens device
    :return
        No return, just output the results"""
    os.system("python lib/s7scan/s7scan.py --log-dir reports/ --tcp " + target)


