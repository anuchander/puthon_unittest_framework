import unittest

def setUpModule():
    print("calling before module!")

def tearDownModule():
    print("calling after the module!")

class TestSFDCUnit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Setting up the envirnonment for the browser before class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Generating Reports after class")

    @classmethod
    def setUp(self) -> None:
        print("Launch the browser")

    @classmethod
    def tearDown(self) -> None:
        print("Closing my browser")

    def test_LoginError(self):
        print("Error message verified")
        self.assertEquals("salesforce", "salesforce", "Titles are not matching")

    @unittest.skipIf(2==1, "Remember me test is skipped!")
    def test_RememberMe(self):
        print("Remember me is verified")
        self.assertNotEqual("salesforce", "salesforce1", "Titles are matching for assertNotEqual")

    def test_Logout(self):
        print("Logged out of the application")
        a=None
        self.assertIsNone(a, "a=None, condition is not satisfied")
        self.assertTrue(2==2, "True condition is failed ")

if __name__=="__main__":
    unittest.main()
