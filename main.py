class Credential:
    credentials_list = []

    """
    Class that generates new instances of credentials
    """

    def __init__(self, username, password):
        
        self.username = username
        self.password = password

    def save_credential(self):
        """
        save_credential method saves the credential objects into the empty credential list
        """

        Credential.credentials_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes the credential that the user no longer needs
        """
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        """
        This method takes in an account and matches an account that matches that account.

        Args:
            account: Account to search for
        Returns:
        The aacount that matches the account searched for.
        """

        for account in cls.credentials_list:
            if account.username == username:
                return account
    
    @classmethod
    
    def account_details_exist(cls, username):
        """
        Method that checks if the account exists
        """
        for account in cls.credentials_list:
            if account.username == username:
                return True

        return False
    
    @classmethod
    def authentication(cls, username, password):

        for authentic in cls.credentials_list:
            if authentic.username == username and authentic.password == password:
                return authentic 

    
    @classmethod
    def display_details(cls):
        '''
        Method that displays existing credentials.
        '''
        return cls.credentials_list

    