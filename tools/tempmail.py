from colorama import Fore, init
from mailtm import Email
from utils import clear_terminal, end_func, Error

def tempmail():
    clear_terminal()
    init(autoreset=True)
    try:
        print(Fore.GREEN+"""
          ________________________________     _________________________
          7      77     77        77     7     7        77  _  77  77  7
          !__  __!|  ___!|  _  _  ||  -  |     |  _  _  ||  _  ||  ||  |
            7  7  |  __|_|  7  7  ||  ___!     |  7  7  ||  7  ||  ||  !___
            |  |  |     7|  |  |  ||  7        |  |  |  ||  |  ||  ||     7
            !__!  !_____!!__!__!__!!__!        !__!__!__!!__!__!!__!!_____!

                       - For New Mail Address Run The Tool Again
            """)


        # Get Domains
        mail = Email()

        # Make new email address
        mail.register()
        print(Fore.GREEN+"\n        Email Adress: " + str(mail.address))

        # Start listening
        mail.start(listener)
        print(Fore.GREEN+"\n        Waiting for new emails to come in Inbox...")
    except Exception as e:
        Error(e)
        end_func(tempmail)


def listener(message):
    print(Fore.GREEN+"\n        Subject: " + message['subject'])
    print(Fore.GREEN+"\n        Content: " + message['text'] if message['text'] else message['html'])
    print()

# TODO - add functionality to when press ctrl + c it call the tempmail() again without using sudo command
