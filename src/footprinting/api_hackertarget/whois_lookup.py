import requests

def whois_lookup():
	target = raw_input("Enter the domain or IPv4 target: ")
	url = "https://api.hackertarget.com/whois/?q=" + target
	request = requests.get(url)
	response = request.text
	print(response)
	raw_input("Press {return} to continue")
	return



