import requests


def obtain_reverse_dns_info(target):
    url = "https://api.hackertarget.com/reversedns/?q="+target
    request = requests.get(url)
    response = request.text
    return response
