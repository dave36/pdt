import nmap

def scan_open_ports(target):
    try:
        scanner = nmap.PortScanner()
        scanner.scan(target, arguments='-sC -sV')
        result = scanner.csv()
    except:
        print("Nmap not installed")
    
    return result


