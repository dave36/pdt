import os
from os import system, name
import text
import sys
sys.path.append('src/01_Footprinting/')
from api_shodan.shodan_collector import *
from api_hackertarget.dns_info import *
from api_hackertarget.reverse_dns_info import *
from api_hackertarget.subnet_calculator import *
from api_hackertarget.whois_lookup import *
from api_hackertarget.zone_transfer import *

#if name == 'posix':
sys.path.append('src/02_Fingerprinting/')
from nmap_scan import *
from plc_scanner import *
from Modbus.discover_modbus import *
from Modbus.uid_scanner import *
from Modbus.get_functions import *
from Modbus.read_coils import *
from Modbus.read_discrete_input import *
from Modbus.read_exception_status import *
from Modbus.read_holding_register import *
from Modbus.read_input_register import *
from Siemens.discover_siemens import *
from Siemens.enumerate_siemens import *
from Siemens.s7_scan import *

sys.path.append('src/03_Exploitation/')
from Default_passwords.parser_passwords import *
from Modbus_Exp.write_single_register import *
from Modbus_Exp.write_single_coils import *
from Siemens_Exp.s7_pwd_hashes_extractor import *

sys.path.append('src/04_Reporting/')
from report_log import *

### Every menu of the tool.
### Each one is going to be in a separate function to get a clean code!
def main_menu():
    """Function to display the options of the main menu"""
    # Show the main menu
    create_menu(text.main_description, text.main_options)
    try:
        while 1:
            choice = raw_input("(pdt) > ")
            # Parts of the pentesting
            # Choice 1: Footprinting
            if choice == '1':
                footprinting_menu()
            # Choice 2: Fingerprinting
            if choice == '2':
                fingerprinting_menu()
            # Choice 3: Exploitation
            if choice == '3':
                exploitation_menu()
            # Choice 4: Reports
            if choice == '4':
                reports_menu()
            # Choice 5: Update
            if choice == '5':
                update_menu()
            # Choice 6: Help
            if choice == '6':
                help_menu()
            # Choice 7: Stop the program
            if choice == '7':
                break
            # Else: Every different input will show the main menu again
            else:
                main_menu()
                return

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")


def footprinting_menu():
    while 1:
        create_menu(text.footprinting_description, text.footprinting_options)
        choice = raw_input("(pdt/footprinting) > ")
        # Choice 1: Public information available on Shodan
        if choice == '1':
            ip = raw_input("Enter the IPv4 target: ")
            shodan_search(ip)
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        # Choice 2: DNS information
        if choice == '2':
            target = raw_input("Enter the domain target: ")
            print(obtain_dns_info(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        # Choice 3: Reverse DNS information
        if choice == '3':
            target = raw_input("Enter the domain or IPv4 target: ")
            print(obtain_reverse_dns_info(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        # Choice 4: Whois record information
        if choice == '4':
            target = raw_input("Enter the domain or IPv4 target: ")
            print(whois_lookup(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        # Choice 5: Calculate subnet range and some information
        if choice == '5':
            target = raw_input("Enter the domain or IPv4 target: ")
            print(calc_subnet(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        # Choice 6: DNS info about zone transfer
        if choice == '6':
            target = raw_input("Enter the domain target: ")
            print(obtain_zone_transfer(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        # Last choice: Back to the main menu
        if choice == str(len(text.footprinting_options)):   # Dont need to know which is the last option
            break
    

def fingerprinting_menu():
    while 1:
        create_menu(text.fingerprinting_description, text.fingerprinting_options)
        choice = raw_input("(pdt/fingerprinting) > ")
        # Choice 1: Scan open ports on the target
        if choice == '1':
            target = raw_input("Enter the IPv4 target: ")
            print(scan_open_ports(target))
            raw_input("Press {return} to continue")
            fingerprinting_menu()
            return
        # Choice 2: Scan PLCs
        if choice == '2':
            target = raw_input("Enter the IPv4 target: ")
            scan_plcs(target)
            raw_input("Press {return} to continue")
            fingerprinting_menu()
            return
        # Choice 3: Load the fingerprinting modbus menu
        if choice == '3':
            fingerprinting_modbus_menu()
        # Choice 4: Load the fingerprinting siemens menu
        if choice == '4':
            fingerprinting_siemens_menu()
        if choice == str(len(text.fingerprinting_options)):   # Dont need to know which is the last option
            break


def fingerprinting_modbus_menu():
    while 1:
        create_menu(text.fingerprinting_modbus_description, text.fingerprinting_modbus_options)
        choice = raw_input("(pdt/fingerprinting/modbus) > ")
        # Choice 1: Modbus information (with nmap nse script)
        if choice == '1':
            target = raw_input("Enter the IPv4 target: ")
            discover_modbus(target)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 2: Get all the UIDs available (slaves on Modbus)
        if choice == '2':
            target = raw_input("Enter the IPv4 target: ")
            scan_uid(target)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 3: Get the functions on Modbus
        if choice == '3':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            get_functions(target, uid)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 4: Read holding registers
        if choice == '4':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            read_holding_register(target, uid)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 5: Read coils
        if choice == '5':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            read_coils(target, uid)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 6: Read status of discrete inputs
        if choice == '6':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            read_discrete_input(target, uid)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 7: Read inputs registers
        if choice == '7':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            read_input_register(target, uid)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Choice 8: Read exception status
        if choice == '8':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            read_exception_status(target, uid)
            raw_input("Press {return} to continue")
            fingerprinting_modbus_menu()
            return
        # Last option: Back
        if choice == str(len(text.fingerprinting_modbus_options)):   # Dont need to know which is the last option
            break


def fingerprinting_siemens_menu():
    while 1:
        create_menu(text.fingerprinting_siemens_description, text.fingerprinting_siemens_options)
        choice = raw_input("(pdt/fingerprinting/siemens_s7) > ")
        # Choice 1: Discover siemens S7 devices
        if choice == '1':
            target = raw_input("Enter the IPv4 target: ")
            discover_siemens(target)
            raw_input("Press {return} to continue")
            fingerprinting_siemens_menu()
            return
        # Choice 2: Enumerate siemens S7 devices
        if choice == '2':
            target = raw_input("Enter the IPv4 target: ")
            enumerate_siemens(target)
            raw_input("Press {return} to continue")
            fingerprinting_siemens_menu()
            return
        # Choice 3: S7 scan
        if choice == '3':
            target = raw_input("Enter the IPv4 target: ")
            scan_siemens(target)
            raw_input("Press {return} to continue")
            fingerprinting_siemens_menu()
            return
        if choice == str(len(text.fingerprinting_siemens_options)):   # Dont need to know which is the last option
            break


def exploitation_menu():
    while 1:
        create_menu(text.exploitation_description, text.exploitation_options)
        choice = raw_input("(pdt/exploitation) > ")
        # Choice 1: Common ICS Default Passwords
        if choice == '1':
            print_default_passwords()
            raw_input("Press {return} to continue")
            exploitation_menu()
            return
        # Choice 2: Load the exploitation modbus menu
        if choice == '2':
            exploitation_modbus_menu()
        # Choice 3: Load the exploitation siemens menu
        if choice == '3':
            exploitation_siemens_menu()
        if choice == str(len(text.exploitation_options)):   # Dont need to know which is the last option
            break

def exploitation_modbus_menu():
    while 1:
        create_menu(text.exploitation_modbus_description, text.exploitation_modbus_options)
        choice = raw_input("(pdt/exploitation/modbus) > ")
        # Choice 1: Write single register
        if choice == '1':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            write_single_register(target, uid)
            raw_input("Press {return} to continue")
            exploitation_modbus_menu()
            return
        # Choice 2: Write single coil
        if choice == '2':
            target = raw_input("Enter the IPv4 target: ")
            uid = raw_input("Enter the UID Modbus: ")
            write_single_coils(target, uid)
            raw_input("Press {return} to continue")
            exploitation_modbus_menu()
            return
        if choice == str(len(text.exploitation_modbus_options)):   # Dont need to know which is the last option
            break

def exploitation_siemens_menu():
    while 1:
        create_menu(text.exploitation_siemens_description, text.exploitation_siemens_options)
        choice = raw_input("(pdt/exploitation/siemens) > ")
        # Choice 1: Extract password hashes
        if choice == '1':
            file = raw_input("Enter the path to the PLF file: ")
            extract_s7_password_hashes(file)
            raw_input("Press {return} to continue")
            exploitation_siemens_menu()
            return
        if choice == str(len(text.exploitation_siemens_options)):   # Dont need to know which is the last option
            break

def reports_menu():
    while 1:
        create_menu(text.reports_description, text.reports_options)
        choice = raw_input("(pdt/reports) > ")
        # Choice 1: Text report
        if choice == '1':
            show_report()
            raw_input("Press {return} to continue")
            reports_menu()
            return
        if choice == str(len(text.reports_options)):   # Dont need to know which is the last option
            break


def update_menu():
    while 1:
        print("Updating from GitHub...")
	os.system("git pull")
	raw_input("\nPress {return} to continue")
	return

def help_menu():
    create_menu(text.help_description, text.help_options)
    raw_input("\nPress {return} to continue")
    return



def create_menu(description, options):
    """Function to create a menu to be displayed in the user's prompt
    :params
        description - The description of the menu
        options - The several choices of the menu
    :return
        No return, just output the menu to the user"""

    # Clean the prompt
    # for windows
    if name == 'nt':
        os.system('cls')
    # for mac and linux (os.name is 'posix')
    else:
        os.system('clear')
    # Output the title, description and options of the tool
    print_title()
    print(description)
    if len(options) > 1:        # To handle the menus that dont have any options
        print("Choose a number from the menu:")
        for i in range (len(options)):
            print("\t" + str(i+1) + "- " + options[i])
    return


def print_title():
    """Auxiliary function to display the title of the tool"""
    print("""
                .---. .-.   .-----.
                :   : :  ;  `-. .-'
                :---' :   :   : :
                :     :   :   : :
                :     :_.'    :_:   """)
    print(text.title_description)

