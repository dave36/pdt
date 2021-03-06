import os
import sys
from src.util.validator import *

sys.path.append('src/04_Reporting/')
from report_log import *

sys.path.append('lib/smod/')
from System.Core.Global import *
from System.Core.Colors import *
from System.Core.Modbus import *


startAddr = '0x0000'
quantity = '0x0004'

def printLine(str,color):
    if(str.find('[+]') != -1):
        print str.replace('[+]',color + '[+]' + bcolors.ENDC)
    elif(str.find('[-]') != -1):
        print str.replace('[-]',color + '[-]' + bcolors.ENDC)
    else:
        print str

def read_coils(ip, uid):
    """Function to read the value of the coil on the modbus UID device running
    :params
		ip - The address of the modbus device
		uid - The UID slave of modbus
    :return
        No return, just output the results"""
    if (ask_address() and is_valid_ipv4(ip) and is_valid_uid(uid)):
        c = connectToTarget(ip,502)
        report_log("Result of reading coils")
        if c == None:
            printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
            report_log('[-] Modbus is not running on : ' + ip)
            return
        printLine('[+] Connecting to ' + ip,bcolors.OKGREEN)
        report_log('[+] Connecting to ' + ip)
        ans = c.sr1(ModbusADU(transId=getTransId(),unitId=int(uid))/ModbusPDU01_Read_Coils(startAddr=int(startAddr,16),quantity=int(quantity,16)),timeout=timeout, verbose=1)
        ans = ModbusADU_Answer(str(ans))
        printLine('[+] Response is :',bcolors.OKGREEN)
        report_log('[+] Response is :')
        ans.show()
        modbus_report_log(ans)
        return

def ask_address():
    global startAddr
    global quantity
    address = raw_input("Enter the coil address you want to read: ")
    # validate user input (the address)
    if (is_valid_register(address)):
        startAddr = address
        return True
        #if int(address) > 0:
        #    quantity = address
        #else:
        #    quantity = '0x0001'
    else:
        return False

