import sys
import requests
sys.path.append('src/04_Reporting/')
from report_log import *

def whois_lookup(target):
	"""Function to get the information of whois register
    :return
        Return the response obtained"""
	url = "https://api.hackertarget.com/whois/?q=" + target
	request = requests.get(url)
	response = request.text
	report_log(response)
	return response



