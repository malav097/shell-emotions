import os, getpass 


def print_welcome():
    try:
        col = os.get_terminal_size().columns
    except:
        col = 80
    welcome_str = "Welcome: " + getpass.getuser()
    print(welcome_str.center(col))