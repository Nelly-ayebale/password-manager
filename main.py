class Credential:
    credentials_list = []

    """
    Class that generates new instances of credentials
    """

    def __init__(self,account, username, password):
        self.account = account
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

    