import requests


def obtain_dns_info():
    target = raw_input("Enter the domain target: ")
    url = "https://api.hackertarget.com/dnslookup/?q="+target
    request = requests.get(url)

    response = request.text
    print(response)
    raw_input("Press {return} to continue")
    return
