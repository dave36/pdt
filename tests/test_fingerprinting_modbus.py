import unittest
from io import BytesIO as StringIO
import sys
sys.path.append('src/01_Footprinting/')
from api_hackertarget.dns_info import *
from api_hackertarget.reverse_dns_info import *

sys.path.append('src/02_Fingerprinting/')
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

### python -m unittest discover -s tests
### python -m unittest discover -s tests -p test_fingerprinting_modbus.py

class FingerprintingModbusTestSuite(unittest.TestCase):
    """Fingerprinting Modbus test cases."""

    """Test to check the nmap scan to discover modbus port 502 information"""
    def test_discover_modbus(self):
        target = "127.0.0.1"
        result = discover_modbus(target)
        self.assertIsNotNone(result)

    """Test to check the nmap scan to discover modbus port 502 information wrong string input"""
    def test_discover_modbus_wrong_input(self):
        target = "a"
        result = discover_modbus(target)
        self.assertIsNotNone(result)
        self.assertFalse("ports" in result["scan"])
    
    """Test to check the nmap scan to discover modbus port 502 information with wrong integer input"""
    def test_discover_modbus_wrong_input_2(self):
        target = "1231231"
        result = discover_modbus(target)
        self.assertIsNotNone(result)
        self.assertFalse("ports" in result["scan"])

    """Test to check the UID scanner to know the slaves of modbus available
        On this local IP it won't be running any slave"""
    def test_uid_scanner(self):
        target = "127.0.0.1"
        result = scan_uid(target)
        self.assertIsNone(result)
    
    """Test to check the UID scanner with wrong integer input"""
    def test_uid_scanner_wrong_input(self):
        target = "12312"
        result = scan_uid(target)
        self.assertIsNone(result)
    
    """Test to check the UID scanner with wrong string input"""
    def test_uid_scanner_wrong_input_2(self):
        target = "a"
        result = scan_uid(target)
        self.assertIsNone(result)

    """Test to check the function enumerator of Modbus
        It will be None because Modbus is not running locally"""
    def test_get_functions_modbus(self):
        target = "127.0.0.1"
        uid = "1"
        result = get_functions(target,uid)
        self.assertIsNone(result)

    """Test to check the function enumerator of Modbus with wrong input ip and uid"""
    def test_get_functions_modbus_wrong_input(self):
        target = "113"
        uid = "a"
        result = get_functions(target,uid)
        self.assertIsNone(result)

    """Test to check the function enumerator of Modbus with wrong input uid"""
    def test_get_functions_modbus_wrong_input_2(self):
        target = "127.0.0.1"
        uid = "9999999"
        result = get_functions(target,uid)
        self.assertIsNone(result)

    """Test to check the read discrete input of Modbus
        It won't be be running any Modbus instance on this IP locally so it would be None"""
    def test_read_discrete_input(self):
        target = "127.0.0.1"
        uid = "1"
        result = read_discrete_input(target,uid)
        self.assertIsNone(result)

    """Test to check the read discrete input of Modbus with wrong ip input"""
    def test_read_discrete_input_wrong_input(self):
        target = "ad"
        uid = "1"
        result = read_discrete_input(target,uid)
        self.assertIsNone(result)

    """Test to check the read discrete input of Modbus with wrong uid input"""
    def test_read_discrete_input_wrong_input_2(self):
        target = "127.0.0.1"
        uid = "asdas"
        result = read_discrete_input(target,uid)
        self.assertIsNone(result)

    """Test to check the read exceptios status of Modbus
        It won't be be running any Modbus instance on this IP locally so it would be None"""
    def test_read_exception_status(self):
        target = "127.0.0.1"
        uid = "1"
        result = read_exception_status(target,uid)
        self.assertIsNone(result)

    """Test to check the read discrete input of Modbus with wrong ip input"""
    def test_read_exception_status_wrong_input(self):
        target = "a"
        uid = "1"
        result = read_exception_status(target,uid)
        self.assertIsNone(result)

    """Test to check the read discrete input of Modbus with wrong uid input"""
    def test_read_exception_status_wrong_input_2(self):
        target = "127.0.0.1"
        uid = "asd"
        result = read_exception_status(target,uid)
        self.assertIsNone(result)

    def test_ask_address(self):
        # Initialize variables to handle input and output to test
        input_test = StringIO(str("1"))
        out_test = StringIO()
        # Store the input and output
        sys.stdin = input_test
        sys.stdout = out_test
        # Function to test
        self.assertTrue(ask_address())

    def test_ask_address_wrong_input(self):
        # Initialize variables to handle input and output to test
        input_test = StringIO(str("a"))
        out_test = StringIO()
        # Store the input and output
        sys.stdin = input_test
        sys.stdout = out_test
        # Function to test
        self.assertFalse(ask_address())

if __name__ == '__main__':
    unittest.main()