import requests
from src.util.validator import *

def obtain_zone_transfer(target):
    if (validate_domain_name(target)):
        url = "https://api.hackertarget.com/zonetransfer/?q="+target
        request = requests.get(url)
        response = request.text
        return response
    return "Error"
