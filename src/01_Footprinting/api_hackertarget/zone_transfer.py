import sys
import requests
from src.util.validator import *
sys.path.append('src/04_Reporting/')
from report_log import *

def obtain_zone_transfer(target):
    if (validate_domain_name(target)):
        url = "https://api.hackertarget.com/zonetransfer/?q="+target
        request = requests.get(url)
        response = request.text
        report_log(response)
        return response
    return "Error"
