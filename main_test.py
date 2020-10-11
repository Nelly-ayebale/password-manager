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

        self.new_credential = Credential("Ayebale Nelly Abigail", "nellyayebale")

    def tearDown(self):
        '''
        This method runs each time after every test case.
        '''
        Credential.credentials_list = []

    def test_init(self):
        """
        Method to test if the ojects have been initalized properly.
        """
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
        test_credential = Credential("Diane", "dee420")
        test_credential.save_credential()

        self.assertEqual(len(Credential.credentials_list),2)

    def test_delete_credential(self):
        '''
        Test case to check whether credentials could be deleted from the credentials list.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Diane", "dee420")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)
    
    def test_find_by_username(self):
        '''
        Test case to test whether a user can find their credential by username
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Diane", "dee420")
        test_credential.save_credential()

        returned_account = Credential.find_by_username("Diane")
        self.assertEqual(returned_account.password, test_credential.password)

    def test_account_details_exist(self):
        '''
        method to check whether the account details of the credentials exist
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Diane", "dee420")
        test_credential.save_credential()

        account_exists = Credential.account_details_exist("Diane")
        self.assertTrue(account_exists)

    def test_authentic_details(self):
        self.new_credential.save_credential()
        test_credential = Credential("Diane", "dee420")
        test_credential.save_credential()

        authentic_account = Credential.authentication('Diane', 'dee420')
        self.assertEqual(authentic_account.username, test_credential.username)
        self.assertEqual(authentic_account.password, test_credential.password)
if __name__ ==  '__main__':
    unittest.main()