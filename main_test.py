import unittest
from main import Credential
from main import User

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

    def test_display_credentials(self):
        '''
        Test case to test whether the existing credentials can be displayed
        '''
        self.assertEqual(Credential.display_details(), Credential.credentials_list)

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours
    '''

    def setUp(self):
        '''
        This method runs each time before every test case.
        '''

        self.new_user = User("Slack","Ayebale Nelly Abigail", "password123")

    def tearDown(self):
        '''
        This method runs each time after every test case.
        '''
        User.user_list = []
    
    def test_init(self):
        """
        Method to test if the ojects have been initalized properly.
        """
        self.assertEqual(self.new_user.account_name, "Slack")
        self.assertEqual(self.new_user.username, "Ayebale Nelly Abigail")
        self.assertEqual(self.new_user.password, "password123")

    def test_save_user_info(self):
        '''
        Test case to test if accounts are being saved to the userlist.
        '''
        self.new_user.save_user_info()
        self.assertEqual(len(User.user_list),1)

    def test_find_by_account_name(self):
        '''
        Test case to test whether a user can find their account by account_name
        '''
        self.new_user.save_user_info()
        test_user = User("Twitter","Diane", "dee420")
        test_user.save_user_info()

        user_found = User.find_by_account_name("Twitter")
        self.assertEqual(user_found.username, test_user.username)

    def test_account_exist(self):
        '''
        method to check whether the account details of the User exist
        '''
        self.new_user.save_user_info()
        test_user = User("Twitter","Diane", "dee420")
        test_user.save_user_info()

        user_exists = User.account_exists("Twitter")
        self.assertTrue(user_exists)
    
    def test_display_accounts(self):
        '''
        Test case to test whether the accounts can be displayed
        '''
        self.assertEqual(User.display_accounts(), User.user_list)



if __name__ ==  '__main__':
    unittest.main()