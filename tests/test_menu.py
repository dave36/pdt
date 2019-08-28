import unittest
#from io import StringIO
from io import BytesIO as StringIO
import sys
from src.menu import *
from src.text import *

### python -m unittest discover -s tests

class MenuTestSuite(unittest.TestCase):
    """Menu test cases."""

    def test_create_main_menu(self):
        # Store the standard output to assert the result then
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        # Function to test (creation of the main menu)
        create_menu(main_description, main_options)
        # Assertions to know that is the main menu
        self.assertTrue("Footprinting" in capturedOutput.getvalue())
        self.assertTrue("Fingerprinting" in capturedOutput.getvalue())
        self.assertTrue("Exploitation" in capturedOutput.getvalue())
        self.assertTrue("Help" in capturedOutput.getvalue())

    def test_create_footprinting_menu(self):
        # Store the standard output to assert the result then
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        # Function to test (creation of the footprinting menu)
        create_menu(footprinting_description, footprinting_options)
        # Assert that we are in the footprinting menu
        self.assertTrue("Footprinting modules" in capturedOutput.getvalue())
    
    def test_footprinting_menu(self):
        # Initialize variables to handle input and output to test
        input_test = StringIO(str(len(footprinting_options))) # The last option breaks the menu
        out_test = StringIO()
        # Store the input and output
        sys.stdin = input_test
        sys.stdout = out_test
        # Function to test
        footprinting_menu()
        # Assert that we are not in another choice
        self.assertTrue("Welcome" in out_test.getvalue().strip())
        self.assertTrue("Footprinting" in out_test.getvalue().strip())
    

    def test_create_fingerprinting_menu(self):
        # Store the standard output to assert the result then
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        # Function to test (creation of the footprinting menu)
        create_menu(fingerprinting_description, fingerprinting_options)
        # Assert that we are in the footprinting menu
        self.assertTrue("Fingerprinting modules" in capturedOutput.getvalue())
    

    def test_fingerprinting_menu(self):
        # Initialize variables to handle input and output to test
        input_test = StringIO(str(len(fingerprinting_options))) # The last option breaks the menu
        out_test = StringIO()
        # Store the input and output
        sys.stdin = input_test
        sys.stdout = out_test
        # Function to test
        fingerprinting_menu()
        # Assert that we are not in another choice
        self.assertTrue("Welcome" in out_test.getvalue().strip())
        self.assertTrue("Fingerprinting" in out_test.getvalue().strip())


    def test_create_exploitation_menu(self):
        # Store the standard output to assert the result then
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        # Function to test (creation of the footprinting menu)
        create_menu(exploitation_description, exploitation_options)
        # Assert that we are in the footprinting menu
        self.assertTrue("Fingerprinting modules" in capturedOutput.getvalue())



if __name__ == '__main__':
    unittest.main()