import nmap
import sys
import os

from src.util.validator import *

sys.path.append('src/04_Reporting/')
from report_log import *

def scan_plcs(target):
    """Function to scan all the PLCs devices running
    :params
		target - The address of the device
    :return
        No return, just output the results"""
    if (is_valid_ipv4(target)):
        os.system("python lib/plcscan/plcscan.py " + target)


