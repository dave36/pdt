import requests


def obtain_zone_transfer(target):
    url = "https://api.hackertarget.com/zonetransfer/?q="+target
    request = requests.get(url)
    response = request.text
    return response
