import sys
import requests
from src.util.validator import *
sys.path.append('src/04_Reporting/')
from report_log import *

def obtain_zone_transfer(target):
    """Function to try to zone transfer the DNS and get the info about it
    :return
        Return the response obtained
        Error if cannot be possible"""
    if (validate_domain_name(target)):
        url = "https://api.hackertarget.com/zonetransfer/?q="+target
        request = requests.get(url)
        response = request.text
        report_log(response)
        return response
    return "Error"
