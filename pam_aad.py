import json
import logging
import os
import sys
import adal

CODE_PROMPT = "Please use this one-time passcode (OTP) to sign in to your account: "
CONFIG_FILE = "/etc/pam_aad.conf"
DEBUG = False
HOST = "https://login.microsoftonline.com/"
RESOURCE = "https://graph.microsoft.com/"
SUBJECT = "Your one-time passcode for signing in via Azure Active Directory"
TTW = 5
USER_AGENT = "azure_authenticator_pam/1.0"
USER_PROMPT = "An email with a one-time passcode was sent to your email. \nEnter the code at https://aka.ms/devicelogin, then press enter.\n"
