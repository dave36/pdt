import nmap
import sys
import pprint

sys.path.append('src/04_Reporting/')
from report_log import *

def scan_open_ports(target):
    result = ""
    try:
        report_log("Result of port scanning the target")
        scanner = nmap.PortScanner()
        result = scanner.scan(target, arguments='-sC -sV')
        pprint.pprint(result["scan"])
        report_log(result["scan"])
    except:
        print("Nmap not installed")
    return result


