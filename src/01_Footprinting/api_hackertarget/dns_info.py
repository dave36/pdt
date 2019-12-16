import requests


def obtain_dns_info(target):
    """Function to get the information of the DNS records for a domain
    :return
        No return. Output the results obtained"""
    # Request to the API to obtain the info
    url = "https://api.hackertarget.com/dnslookup/?q="+target
    request = requests.get(url)
    response = request.text
    return response
