import unittest
from main import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential class behaviours
    '''

    def setUp(self):
        '''
        This method runs each time before every test case.
        '''

        self.new_credential = Credential("Slack", "Ayebale Nelly Abigail", "nellyayebale")

    def tearDown(self):
        '''
        This method runs each time after every test case.
        '''
        Credential.credentials_list = []

    def test_init(self):
        """
        Method to test if the ojects have been initalized properly.
        """

        self.assertEqual(self.new_credential.account_name, "Slack")
        self.assertEqual(self.new_credential.username, "Ayebale Nelly Abigail")
        self.assertEqual(self.new_credential.password, "nellyayebale")

    def test_save_credential(self):
        '''
        Test case to test if credentials are being saved to the credentials list.
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        Test case to test whether user can save mulitple credentials in the credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Diane", "dee420")
        test_credential.save_credential()

        self.assertEqual(len(Credential.credentials_list),2)

    def test_delete_credential(self):
        '''
        Test case to check whether credentials could be deleted from the credentials list.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Diane", "dee420")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)
if __name__ ==  '__main__':
    unittest.main()