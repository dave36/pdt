title_description = ("""
\tWelcome to PDT!!
\tThe Pentesting Driven Tool for ICS
\t(Industrial Control System) and SCADA
\tAuthor: David Lorenzo
\tVisit: https://www.github.com/dave36/pdt\n\n""")

main_description = ("""
The easiest way of pentesting!\n""")

main_options = ['Footprinting',
             'Fingerprinting',
             'Exploitation',
             'Reports',
             'Update',
             'Help, Credits, and About',
             'Exit']


footprinting_description = ("""
Footprinting modules to obtain public information of the company""")

footprinting_options = ['Information of the organization',
             'DNS Lookup',
             'Reverse DNS Lookup',
             'Whois Lookup',
             'Subnet Lookup',
             'Zone transfer',
             'Back']

fingerprinting_description = ("""
Fingerprinting modules to obtain information of the target""")

fingerprinting_options = ['Open ports',
             'Protocol used',
             'Modbus',
             'Siemens S7',
             'To do',
             'Back']

fingerprinting_modbus_description = ("""
Fingerprinting modbus functions to interact with the Modbus devices and get some information of the target""")

fingerprinting_modbus_options = ['Modbus Information',
             'UID Scanner',
             'Enumeration Function on Modbus',
             'Read Coils',
             'Read Discrete Input',
             'Read Exception Status',
             'Read Holding Registers',
             'Read Inputs Registers',
             'Back']

fingerprinting_siemens_description = ("""
Fingerprinting siemens functions to interact with the Siemens S7 devices and get some information of the target""")

fingerprinting_siemens_options = ['Collect information about Siemens S7 PLCs',
             'Identify and enumerate Siemens S7 PLCs',
             'Scan Siemens S7',
             'Back']

exploitation_description = ("""
Modules to exploit the target""")

exploitation_options = ['Common ICS Default Passwords',
             'Modbus',
             'To do',
             'To do',
             'Back']

exploitation_modbus_description = ("""
Modbus modules to exploit the target""")

exploitation_modbus_options = ['Write Single Register',
             'Write Single Coil',
             'To do',
             'To do',
             'Back']

reports_description = ("""
Get the report of the results of the security audit""")

reports_options = ['Text Report',
             'HTML Report',
             'Back']

update_description = ("""
What do you want to update?""")

update_options = ['PDT',
             'Metasploit Modules',
             'Back']

help_description = ("""
The Pentesting Driven Tool (PDT)
\nAuthor: David Lorenzo
\nMore information at https://github.com/dave36/pdt
\nDo not use for ilegal purposes""")
             
help_options = []


