import unittest
from io import BytesIO as StringIO
import sys
sys.path.append('src/01_Footprinting/')
from api_hackertarget.dns_info import *
from api_hackertarget.reverse_dns_info import *

sys.path.append('src/02_Fingerprinting/')
from nmap_scan import *
from plc_scanner import *

### python -m unittest discover -s tests
### python -m unittest discover -s tests -p test_fingerprinting.py

class FingerprintingTestSuite(unittest.TestCase):
    """Footprinting test cases."""

    """Test to check the nmap scan to obtain the open ports"""
    #def test_nmap_scan(self):
    #    target = "127.0.0.1"
    #    result = scan_open_ports(target)
    #    self.assertIsNotNone(result)

    """Test to check the nmap scan to obtain the open ports with wrong string input"""
    #def test_nmap_scan_wrong_input(self):
    #    target = "a"
    #    result = scan_open_ports(target)
    #    self.assertIsNotNone(result)
    #    self.assertFalse("ports" in result["scan"])
    
    """Test to check the nmap scan to obtain the open ports with wrong integer input"""
    #def test_nmap_scan_wrong_input_2(self):
    #    target = "1231231"
    #    result = scan_open_ports(target)
    #    self.assertIsNotNone(result)
    #    self.assertFalse("ports" in result["scan"])
    
    """Test to check the plc scan to obtain the information about PLCs
        On this IP it wont't be running any PLC"""
    def test_plc_scan(self):
        target = "127.0.0.1"
        result = scan_plcs(target)
        self.assertIsNone(result)

    """Test to check the plc scan to obtain the information about PLCs with wrong string input"""
    def test_plc_scan_wrong(self):
        target = "a"
        result = scan_plcs(target)
        self.assertIsNone(result)

    """Test to check the plc scan to obtain the information about PLCs with wrong integer input"""
    def test_plc_scan_wrong_2(self):
        target = "123123"
        result = scan_plcs(target)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()