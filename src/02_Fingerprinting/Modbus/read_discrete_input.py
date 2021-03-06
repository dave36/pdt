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

def read_discrete_input(ip, uid):
    """Function to read the discrete input on the modbus UID device running
    :params
		ip - The address of the modbus device
		uid - The UID slave of modbus
    :return
        No return, just output the results"""
    c = connectToTarget(ip,502)
    if(c == None):
        printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
        return
    printLine('[+] Connecting to ' + ip,bcolors.OKGREEN)
    ans = c.sr1(ModbusADU(transId=getTransId(),unitId=int(uid))/ModbusPDU02_Read_Discrete_Inputs(startAddr=int(startAddr,16),quantity=int(quantity,16)),timeout=timeout, verbose=0)
    ans = ModbusADU_Answer(str(ans))
    printLine('[+] Response is :',bcolors.OKGREEN)
    ans.show()
    return
