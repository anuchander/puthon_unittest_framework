import unittest

class TestTransferLeads(unittest.TestCase):
    def test_transfernewLead(self):
        print("New transfer lead creation")
    def test_transfereditLead(self):
        print("Transfer lead address has to be changed")
    def test_transfercloseLead(self):
        print("transfer Lead is terminated")

if __name__=="__main__":
    unittest.main()