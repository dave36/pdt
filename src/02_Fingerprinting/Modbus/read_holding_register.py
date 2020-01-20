import os
import sys

sys.path.append('lib/smod/')
from System.Core.Global import *
from System.Core.Colors import *
from System.Core.Modbus import *


startAddr = '0x0001'

def printLine(str,color):
    if(str.find('[+]') != -1):
        print str.replace('[+]',color + '[+]' + bcolors.ENDC)
    elif(str.find('[-]') != -1):
        print str.replace('[-]',color + '[-]' + bcolors.ENDC)
    else:
        print str

def read_holding_register(ip, uid):
    ask_address()
    c = connectToTarget(ip,502)
    report_log("Result of reading holding registers")
    if(c == None):
        printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
        report_log('[-] Modbus is not running on : ' + ip)
        return
    printLine('[+] Connecting to ' + ip,bcolors.OKGREEN)
    report_log('[+] Connecting to ' + ip)
    ans = c.sr1(ModbusADU(transId=getTransId(),unitId=int(uid))/ModbusPDU03_Read_Holding_Registers(startAddr=int(startAddr,16),quantity=int('1')),timeout=timeout, verbose=0)
    ans = ModbusADU_Answer(str(ans))
    printLine('[+] Response is :',bcolors.OKGREEN)
    report_log('[+] Response is :')
    ans.show()
    modbus_report_log(ans)
    return

def ask_address():
    global startAddr
    startAddr = '0'
    address = raw_input("Enter the register address you want to read (default address is 0): ")
    # validate user input (the address)
    if (address != ''):
        startAddr = address

