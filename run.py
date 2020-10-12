#!/usr/bin/env python3.8
from main import Credential
from main import User
import random
import string

def create_credential(username, password):
    """
    Function to create a new credential
    """
    new_credential = Credential(username, password)
    return new_credential

def save_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()

def delete_credential(credential):
    """
    Function that deletes a credential
    """
    credential.delete_credential()

def find_credential(username):
    """
    Function that finds a credential by the username and returns that credential
    """
    return Credential.find_by_username(username)

def account_exist(username):
    """
    Function that checks whether the credential exists with that username
    """
    return Credential.account_details_exist(username)

def authenticate_details(username, password):
    """
    Function that checks whether the credentials are authentic
    """
    return Credential.authentication(username, password)

def display_credentials():
    """
    Function that returns saved credentials
    """
    return Credential.display_details()

def create_account(account_name, username, password):
    """
    Function to create a new account for the user
    """
    account = User(account_name, username, password)
    return account

def save_account(account):
    """
    Function that saves the account information
    """
    account.save_user_info()

def find_account(account_name):
    '''
    Function that finds an account by the account name and returns that account
    '''
    return User.find_by_account_name(account_name)

def check_account_exists(account_name):
    '''
    Function that checks whether the account exists with the name of the account_name
    '''
    return User.account_exists(account_name)

def display_accounts():
    '''
    Function that displays the accounts
    '''
    return User.display_accounts()

def generate_user_password(length):
    '''
    Function to generate a user a random password
    '''
    random_password =[]
    get_password = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits,length)
    random_password.append("".join(get_password))
    return random_password

def main():
        print("Hello Welcome to your Password Manager. What is your name?")
        user_name = input("Your Name:")

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                    print("Please use these short codes : cc - create credential,dc- display Credential, lo - login, fa -find account,del- delete Credential, ex -exit the account list")

                    short_code = input().lower()

                    if short_code == 'cc':
                       
                            print ("Enter a Username For Password Manager to get started:")
                            username = input()

                            print("Enter a Password For Password Manager to get started:")
                            password = input()

                           
                            save_credential(create_credential(username, password)) 
                            print ('\n')
                            print(f"Your Username: {username}, password: {password} credentials have been saved")
                            print ('\n')

                    elif short_code == 'lo':

                            print('Enter your Credentials for Password Manager to proceed :')
                            print("-"*10)

                            
                            print("Username:")
                            username = input()

                            print("Password:")
                            password = input()

                            information = authenticate_details(username, password)
                            if information == 0:
                                print("\n")
                                print("Sorry, Your username or password for Password manager is invalid")

                            elif information != 0:
                                print('\n')
                                print(f"Hello again {information.username}, What do you want to do today?")
                                print('\n')

                                while True:
                                    print("Please use short codes for faster service: cc - Create a new account, co - Copy to clipboard, dc - display credential, ex - exit account list:")
                                    short_code = input().lower()
                                    if short_code == 'cc':
                                        print('Create Account Option:')

                                        print("Account Name:")
                                        account_name = input()

                                        print("Username:")
                                        username = input()

                                        print('PLease dictate the length of your password')
                                        length = int(input())
                                        password = generate_user_password(length)
                                        print(f"Password Manager is recommending {password} for your {account_name} account!")
                                        save_account(create_account(account_name, username, password))
                                        
                                    elif short_code == 'dc':
                                        if display_accounts():
                                            print('Here is a list of all user accounts')
                                            print('\n')

                                            for account in display_accounts():
                                                print(f"The Account {account.account_name} has a username of {account.username} and the password is {account.password}")
                                                print('\n')
                                            
                                            
                                        else:
                                            print('\n')
                                            print(f'You dont seem to have any new credentials, {information.username}')
                                            print('\n')
                                        
                                       
                                    elif short_code == 'ex':
                                        print("Thankyou for using Password Manager, you have exited your user-account list!")
                                        break
                                        
                                    
                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"Username: {credential.username}. ")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')                        


                                   
                    elif short_code == 'fa':

                            print("Enter the Credential you want to search for")

                            search_credential = input()
                            if account_exist(search_credential):
                                
                                search_for_credential = find_credential(search_credential)
                                print(f"This Account {search_for_credential.username} exists with the password {search_for_credential.password} ")
                                print('-' * 20)

                                
                                    
                            else:
                                print("That credential does not exist")

                    elif short_code == 'del':

                            print("Enter the Credential you want to delete")

                            searching_credential = input()
                            if account_exist(searching_credential):
                                search_cred = find_credential(searching_credential)
                                search_cred.delete_credential()
                                print(f"This Account  {search_cred.username} has been deleted!")
                                print('-' * 20)

                                
                                    
                            else:
                                print("That credential does not exist")

                    elif short_code == "ex":
                            print("You have exited the credential list, Have a Nice day!")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()

        
