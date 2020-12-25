import os
import getpass

def print_welcome():
    col = os.get_terminal_size().columns
    welcome_str = "Welcome: " + getpass.getuser()
    print(welcome_str.center(col))