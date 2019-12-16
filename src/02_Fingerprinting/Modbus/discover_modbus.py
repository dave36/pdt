import os
import sys

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

def discover_modbus(ip):
    result = connectToTarget(ip,502)
    if (result != None):
        printLine('[+] Modbus is running on : ' + ip,bcolors.OKGREEN)
    else:
        printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
    return