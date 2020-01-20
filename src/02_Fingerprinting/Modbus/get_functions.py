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

def get_functions(ip, uid):
	c = connectToTarget(ip,502)
	report_log("Result of getting functions")
	if(c == None):
		printLine('[-] Modbus is not running on : ' + ip,bcolors.WARNING)
		report_log('[-] Modbus is not running on : ' + ip)
		return None
	printLine('[+] Looking for supported function codes on ' + ip,bcolors.OKGREEN)
	report_log('[+] Looking for supported function codes on ' + ip)
	for i in range(0,128): # Total of 127 (legal) function codes
		ans = c.sr1(ModbusADU(transId=getTransId(),unitId=int(uid))/ModbusPDU_Read_Generic(funcCode=i),timeout=1, verbose=0)
		# We are using the raw data format, because not all function
		# codes are supported out by this library.
		if ans:
			data = str(ans)
			data2 = data.encode('hex')
			returnCode = int(data2[14:16],16)
			exceptionCode = int(data2[17:18],16)

			if returnCode > 127 and exceptionCode == 0x01:
				# If return function code is > 128 --> error code
				printLine("[+] Function Code "+str(i)+" not supported.",bcolors.WARNING)
				report_log("[+] Function Code "+str(i)+" not supported.")
			else:
				if(function_code_name.get(i) != None):
					printLine("[+] Function Code "+str(i)+"("+function_code_name.get(i)+") is supported.",bcolors.OKGREEN)
					report_log("[+] Function Code "+str(i)+"("+function_code_name.get(i)+") is supported.")
				else:
					printLine("[+] Function Code "+str(i)+" is supported.",bcolors.OKGREEN)
					report_log("[+] Function Code "+str(i)+" is supported.")
		else:
			printLine("[+] Function Code "+str(i)+" is probably not supported.",bcolors.WARNING)
			report_log("[+] Function Code "+str(i)+" is probably not supported.")
	return

