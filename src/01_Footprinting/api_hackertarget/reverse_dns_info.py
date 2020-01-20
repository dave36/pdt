import sys
import requests
from src.util.validator import *
sys.path.append('src/04_Reporting/')
from report_log import *

def obtain_reverse_dns_info(target):
    if (validate_ip_and_domain_name(target) == True):
        url = "https://api.hackertarget.com/reversedns/?q="+target
        request = requests.get(url)
        response = request.text
        report_log(response)
        return response
    return "Error"
