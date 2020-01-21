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


def printLine(str,color):
    if(str.find('[+]') != -1):
        print str.replace('[+]',color + '[+]' + bcolors.ENDC)
    elif(str.find('[-]') != -1):
        print str.replace('[-]',color + '[-]' + bcolors.ENDC)
    else:
        print str

"""def discover_modbus(ip):
    # nmap -Pn -sT -p502 --script modbus-discover <target>
    result = connectToTarget(ip,502)
    if (result != None):
        printLine('[+] Modbus is running on : ' + ip,bcolors.OKGREEN)
    else:
        printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
    return"""

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