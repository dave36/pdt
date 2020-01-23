import os
import sys
import nmap
import pprint

sys.path.append('src/04_Reporting/')
from report_log import *

sys.path.append('lib/smod/')
from System.Core.Global import *
from System.Core.Colors import *
from System.Core.Modbus import *


def discover_modbus(target):
    try:
        report_log("Result of scanning the modbus target")
        scanner = nmap.PortScanner()
        result = scanner.scan(target, arguments='-Pn -sT -p502 --script modbus-discover')
        pprint.pprint(result["scan"])
        report_log(result["scan"])
    except:
        print("Nmap not installed")
    return result