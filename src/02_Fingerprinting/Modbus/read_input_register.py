import os
import sys

sys.path.append('lib/smod/')
from System.Core.Global import *
from System.Core.Colors import *
from System.Core.Modbus import *


startAddr = '0x0000'
quantity = '0x0001'

def printLine(str,color):
    if(str.find('[+]') != -1):
        print str.replace('[+]',color + '[+]' + bcolors.ENDC)
    elif(str.find('[-]') != -1):
        print str.replace('[-]',color + '[-]' + bcolors.ENDC)
    else:
        print str

def read_input_register(ip, uid):
    c = connectToTarget(ip,502)
    if(c == None):
        printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
        return 
    printLine('[+] Connecting to ' + ip,bcolors.OKGREEN)
    ans = c.sr1(ModbusADU(transId=getTransId(),unitId=int(uid))/ModbusPDU04_Read_Input_Registers(startAddr=int(startAddr,16),quantity=int(quantity,16)),timeout=timeout, verbose=0)
    ans = ModbusADU_Answer(str(ans))
    printLine('[+] Response is :',bcolors.OKGREEN)
    ans.show()
    return
