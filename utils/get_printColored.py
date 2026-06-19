# https://www.geeksforgeeks.org/python/print-colors-python-terminal/

def prRed(s: str): print("\033[91m {}\033[00m".format(s))
def prGreen(s: str): print("\033[92m {}\033[00m".format(s))
def prYellow(s: str): print("\033[93m {}\033[00m".format(s))
def prLightPurple(s: str): print("\033[94m {}\033[00m".format(s))
def prPurple(s: str): print("\033[95m {}\033[00m".format(s))
def prCyan(s: str): print("\033[96m {}\033[00m".format(s))
def prLightGray(s: str): print("\033[97m {}\033[00m".format(s))
def prBlack(s: str): print("\033[90m {}\033[00m".format(s))  # Corrected from 98 to 90 (standard ANSI)

# Calling the functions to print text in different colors
# prCyan("Hello World, ")
# prYellow("It's")
# prGreen("Geeks")
# prRed("For")
# prGreen("Geeks")