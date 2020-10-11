#!/usr/bin/env python3.8
from main import Credential
from main import User

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

