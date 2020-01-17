import shodan
import re
from src.util.validator import *

SHODAN_API_KEY = "Y0uHNi8aarOWfzVMtVzbLgFzlUAMkid7"

api = shodan.Shodan(SHODAN_API_KEY)

#result = api.search('org:"Evil Corp" product:"nginx" country:"US"')

#for res in result['matches']:
#    print('IP: {}'.format(res['ip_str']))
#    print(res['data'])
#    print('')

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
    
    #86.135.127.30
    #results = api.host('91.228.91.251')
    #results = api.host('158.174.45.254')

    #print(results)

    if results['org'] != None:              print('Organization:\t' + results['org'])
    if results['country_name'] != None:     print('Country:\t' + results['country_name'])
    if results['city'] != None:             print('City:\t' + results['city'])
    if results['latitude'] != None:         print('Latitude:' + str(results['latitude']))
    if results['ip_str'] != None:           print('IP:\t' + results['ip_str'])


