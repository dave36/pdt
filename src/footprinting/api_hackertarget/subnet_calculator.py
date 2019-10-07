import requests

def calc_subnet(target):
    url = "https://api.hackertarget.com/subnetcalc/?q=" + target
    request = requests.get(url)
    response = request.text
    return response



