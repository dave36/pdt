import nmap
import sys

sys.path.append('src/04_Reporting/')
from report_log import *

def scan_open_ports(target):
    result = ""
    try:
        report_log("Result of port scanning the target")
        scanner = nmap.PortScanner()
        scanner.scan(target, arguments='-sC -sV')
        result = scanner.csv()
    except:
        print("Nmap not installed")
    report_log(result)
    return result


