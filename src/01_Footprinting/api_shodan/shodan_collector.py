import shodan
import re
import pprint
from src.util.validator import *

SHODAN_API_KEY = "Y0uHNi8aarOWfzVMtVzbLgFzlUAMkid7"

api = shodan.Shodan(SHODAN_API_KEY)

def shodan_search(ip):
    """Function to get the information of public information using the Shodan API
    :return
        No return. Just output the results with pprint"""
    if (is_valid_ip(ip) == False):
        print("Invalid IPv4 format")
        return
    # Search Shodan
    try:
        results = api.host(ip)
    except:
        print("Something went wrong :(")
        return

    #print(results)
    pprint.pprint(results)


