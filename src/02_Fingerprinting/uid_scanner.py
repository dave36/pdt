import os
import sys

sys.path.append('lib/smod/')
from System.Core.Global import *
from System.Core.Colors import *
from System.Core.Modbus import *

#ip='127.0.0.1'

def printLine(str,color):
    if(str.find('[+]') != -1):
        print str.replace('[+]',color + '[+]' + bcolors.ENDC)
    elif(str.find('[-]') != -1):
        print str.replace('[-]',color + '[+]' + bcolors.ENDC)
    else:
        print str

def scan_uid(ip):
    printLine('[+] Start Brute Force UID on : ' + ip,bcolors.OKGREEN)
    for i in range(10,11): # Total of 255 (legal) uid
        c = connectToTarget(ip,502)
        if(c == None):
            print("Connection error")
            break
        try:
            
            c.sr1(ModbusADU(transId=getTransId(),unitId=i)/ModbusPDU_Read_Generic(funcCode=1),timeout=timeout, verbose=0)
            printLine('[+] UID on ' + ip + ' is : ' + str(i),bcolors.OKGREEN)
            closeConnectionToTarget(c)
        except Exception,e:
            print e
            closeConnectionToTarget(c)
            pass
