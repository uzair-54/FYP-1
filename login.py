from getpass import getpass
from config import firebaseConfig
import pyrebase

config = firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("email: ")
password = input("pass: ")

# user = auth.create_user_with_email_and_password(email,password)

login = auth.sign_in_with_email_and_password(email,password)
print(0)