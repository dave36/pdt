"""
name='PDT',
version='0.1.0',
description='PDT, The Pentesting Driven Tool for ICS and SCADA',
long_description=readme,
author='David Lorenzo',
url='https://github.com/dave36'
"""

from src.menu import *
sys.path.append('src/04_Reporting/')
from report_log import *

# Reset the log for previous reports
reset_log()
# Show the main menu
main_menu()

