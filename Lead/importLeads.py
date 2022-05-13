import unittest

class TestImportLeads(unittest.TestCase):
    def test_importnewLead(self):
        print("New lead creation")
    def test_importeditLead(self):
        print("Lead address has to be changed")
    def test_importcloseLead(self):
        print("Lead is terminated")

if __name__=="__main__":
    unittest.main()