import os
import text
from footprinting.api_shodan.shodan_collector import shodan_search
from footprinting.api_hackertarget import *



### Every menu of the tool.
### Each one is going to be in a separate function to get a clean code!
def main_menu():
    """Function to display the options of the main menu"""
    # Show the main menu
    create_menu(text.main_description, text.main_options)
    try:
        while 1:
            choice = raw_input()

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
        choice = raw_input()
        if choice == '1':
            ip = raw_input("Enter the IPv4 target: ")
            shodan_search(ip)
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        if choice == '2':
            target = raw_input("Enter the domain target: ")
            print(dns_info.obtain_dns_info(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        if choice == '3':
            target = raw_input("Enter the IPv4 target: ")
            print(reverse_dns_info.obtain_reverse_dns_info(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        if choice == '4':
            target = raw_input("Enter the domain or IPv4 target: ")
            print(whois_lookup.whois_lookup(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        if choice == '5':
            target = raw_input("Enter the domain or IPv4 target: ")
            print(subnet_calculator.calc_subnet(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        if choice == '6':
            target = raw_input("Enter the domain target: ")
            print(zone_transfer.obtain_zone_transfer(target))
            raw_input("Press {return} to continue")
            footprinting_menu()
            return
        if choice == str(len(text.footprinting_options)):   # Dont need to know which is the last option
            break
    

def fingerprinting_menu():
    while 1:
        create_menu(text.fingerprinting_description, text.fingerprinting_options)
        choice = raw_input()
        if choice == '1':
            break
        if choice == str(len(text.fingerprinting_options)):   # Dont need to know which is the last option
            break


def exploitation_menu():
    while 1:
        create_menu(text.exploitation_description, text.exploitation_options)
        choice = raw_input()
        if choice == '1':
            break
        if choice == str(len(text.exploitation_options)):   # Dont need to know which is the last option
            break


def reports_menu():
    while 1:
        create_menu(text.reports_description, text.reports_options)
        choice = raw_input()
        if choice == '1':
            break
        if choice == str(len(text.reports_options)):   # Dont need to know which is the last option
            break


def update_menu():
    while 1:
        create_menu(text.update_description, text.update_options)
        choice = raw_input()
        if choice == '1':
            break
        if choice == str(len(text.update_options)):   # Dont need to know which is the last option
            break


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
    os.system("clear")
    # Output the title, description and options of the tool
    print_title()
    print(description)
    if len(options) > 1:        # To handle the menus that dont have any options
        print("Select from the menu:")
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

