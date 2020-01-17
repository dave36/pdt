import unittest
from io import BytesIO as StringIO
import sys
from src.menu import *
from src.text import *
sys.path.append('src/01_Footprinting/')
from api_hackertarget.dns_info import *
from api_hackertarget.reverse_dns_info import *
from api_hackertarget.subnet_calculator import *
from api_hackertarget.whois_lookup import *
from api_hackertarget import *
from api_shodan.shodan_collector import shodan_search
from src.util.validator import *


### python -m unittest discover -s tests

class FootprintingTestSuite(unittest.TestCase):
    """Footprinting test cases."""

    """Test to check the function to obtain DNS info (class dns_info)"""
    def test_dns_info(self):
        target = "google.com"
        result = dns_info.obtain_dns_info(target)
        self.assertIsNotNone(result)

    """Test to check the function to find the reverse DNS records (class reverse_dns_info)"""
    def test_reverse_dns_info(self):
        target = "8.8.8.8"
        result = reverse_dns_info.obtain_reverse_dns_info(target)
        self.assertIsNotNone(result)
        self.assertTrue("dns.google" in result)

    """Test to check the function to determine the registered owner of a domain (class whois_lookup)"""
    def test_whois_lookup(self):
        target = "google.com"
        result = whois_lookup.whois_lookup(target)
        self.assertIsNotNone(result)
        self.assertTrue("GOOGLE.COM" in result)

    """Test to determine the properties of a network subnet given an IPv4 address (class zone_transfer) """
    def test_subnet_calculator(self):
        target = "8.8.8.8"
        result = subnet_calculator.calc_subnet(target)
        self.assertIsNotNone(result)
        self.assertTrue("Address" in result)
        self.assertTrue("Netmask" in result)

    """Test to determine the properties of a network subnet given an domain (class zone_transfer) """
    def test_subnet_calculator(self):
        target = "google.com"
        result = subnet_calculator.calc_subnet(target)
        self.assertIsNotNone(result)
        self.assertTrue("Error" in result)


if __name__ == '__main__':
    unittest.main()