import unittest
from signup import validate_email, validate_pass

class TestSignUp(unittest.TestCase):

    def test_validate_email_valid(self):
        self.assertTrue(validate_email("johndoe123@gmail.com"))

    def test_validate_email_invalid(self):
        self.assertFalse(validate_email("john.doe123@.com"))
        self.assertFalse(validate_email("john.doe123@gmail"))
        self.assertFalse(validate_email("123john.doe@gmail.com"))
        self.assertFalse(validate_email("john.doe!@gmail.com"))

    def test_validate_pass_valid(self):
        self.assertTrue(validate_pass("Pa$$w0rd!123"))
        self.assertTrue(validate_pass("strong_password#1"))

    def test_validate_pass_invalid(self):
        self.assertFalse(validate_pass("password"))
        self.assertFalse(validate_pass("Pa$$word"))
        self.assertFalse(validate_pass("Pa$$w0rd!"))
        self.assertFalse(validate_pass("short#1"))
