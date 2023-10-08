# identity.py
import os

def check_git_identity(scope='global'):
    email_config = f"git config --{scope} user.email"
    name_config = f"git config --{scope} user.name"
    email = os.popen(email_config).read().strip()
    name = os.popen(name_config).read().strip()
    return email and name

def set_git_identity(scope='global'):
    email = input("Enter your email: ")
    name = input("Enter your name: ")
    os.system(f"git config --{scope} user.email '{email}'")
    os.system(f"git config --{scope} user.name '{name}'")