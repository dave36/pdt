import requests


def obtain_reverse_dns_info():
    target = raw_input("Enter the IPv4 target: ")
    url = "https://api.hackertarget.com/reversedns/?q="+target
    request = requests.get(url)

    response = request.text
    print(response)
    raw_input("Press {return} to continue")
    return
