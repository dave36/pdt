import shodan
import re
import pprint
from src.util.validator import *

SHODAN_API_KEY = "Y0uHNi8aarOWfzVMtVzbLgFzlUAMkid7"

api = shodan.Shodan(SHODAN_API_KEY)

def shodan_search(ip):
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


