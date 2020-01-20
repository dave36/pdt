import sys
import requests
sys.path.append('src/04_Reporting/')
from report_log import *

def whois_lookup(target):
	url = "https://api.hackertarget.com/whois/?q=" + target
	request = requests.get(url)
	response = request.text
	report_log(response)
	return response



