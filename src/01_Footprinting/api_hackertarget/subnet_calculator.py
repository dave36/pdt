import requests
from src.util.validator import *

def calc_subnet(target):
    if (validate_ip(target)):
        url = "https://api.hackertarget.com/subnetcalc/?q=" + target
        request = requests.get(url)
        response = request.text
        return response
    return "Error"
