import requests

def calc_subnet():
    target = raw_input("Enter the IPv4 target: ")
    url = "https://api.hackertarget.com/subnetcalc/?q=" + target
    request = requests.get(url)
    response = request.text
    print(response)
    raw_input("Press {return} to continue")
    return



