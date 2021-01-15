import unittest
from src.guest import Guest 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Pam Halpert")

    def test_guest_has_name(self):
        self.assertEqual("Pam Halpert", self.guest.name)