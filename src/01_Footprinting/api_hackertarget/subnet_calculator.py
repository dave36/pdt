import sys
import requests
from src.util.validator import *
sys.path.append('src/04_Reporting/')
from report_log import *

def calc_subnet(target):
    """Function to calculate the subnet network of the target
    :return
        Return the response obtained
        Error if cannot be possible"""
    if (validate_ip(target)):
        url = "https://api.hackertarget.com/subnetcalc/?q=" + target
        request = requests.get(url)
        response = request.text
        report_log(response)
        return response
    return "Error"
