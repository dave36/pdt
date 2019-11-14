import requests

def whois_lookup(target):
	url = "https://api.hackertarget.com/whois/?q=" + target
	request = requests.get(url)
	response = request.text
	return response



