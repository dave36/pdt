import os
import sys

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

def scan_uid(ip):
    report_log('Result of UID scan:\n[+] Start Brute Force UID on : ' + ip)
    printLine('[+] Start Brute Force UID on : ' + ip,bcolors.OKGREEN)
    for i in range(1,256): # Total of possible uid values (0-255)
        c = connectToTarget(ip,502)
        if(c == None):
            print("Connection error")
            break
        try:
            response = c.sr1(ModbusADU(transId=getTransId(),unitId=i)/ModbusPDU_Read_Generic(funcCode=1),timeout=2, verbose=0)
            if (response is not None):
                printLine('[+] UID on ' + ip + ' is : ' + str(i),bcolors.OKGREEN)
                report_log('[+] UID on ' + ip + ' is : ' + str(i))
            else:
                printLine('[-] UID on ' + ip + ' is not running : ' + str(i),bcolors.FAIL)
                report_log('[+] UID on ' + ip + ' is not running : ' + str(i))
            closeConnectionToTarget(c)
        except Exception,e:
            print e
            closeConnectionToTarget(c)
            pass
    return
