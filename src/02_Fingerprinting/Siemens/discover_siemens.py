import sys
import nmap
import pprint

sys.path.append('src/04_Reporting/')
from report_log import *


def discover_siemens(target):
    """Function to discover the siemens devices
    :params
		target - The address of the siemens device
    :return
        No return, just output the results"""
    try:
        report_log("Result of scanning the siemens target")
        scanner = nmap.PortScanner()
        result = scanner.scan(target, arguments='-Pn -sT -p102 --script s7-info')
        pprint.pprint(result["scan"])
        report_log(result["scan"])
    except:
        print("Nmap not installed")
    return result