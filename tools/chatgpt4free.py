import g4f
from g4f.client import Client
from g4f import Provider
from colorama import Fore, init
from g4f.gui import run_gui
import os
from utils import end_func, clear_terminal


def gpt():

    clear_terminal()
        # Initialize Colorama
    init(autoreset=True)

    print(Fore.GREEN+"""
        _________________________________________________________
        7     77     77      77  7  77     77  _  77     77     7
        |   __!|  -  |!__  __!|  !  ||  ___!|    _||  ___!|  ___!
        |  !  7|  ___!  7  7  !___  ||  __| |  _ \ |  __|_|  __|_
        |     ||  7     |  |     7  ||  7   |  7  ||     7|     7
        !_____!!__!     !__!     !__!!__!   !__!__!!_____!!_____!
                    - Run At Your Own Risk <<<<<<<<
        """)
    guiOrTerminal = input(Fore.GREEN+"      > You Want To Use In Terminal Or In Web (More Providers) (t/w): ")

    if guiOrTerminal == "t":
        if os.name == "nt":
            clear_terminal()
            print(Fore.GREEN+"""
                _________________________________________________________
                7     77     77      77  7  77     77  _  77     77     7
                |   __!|  -  |!__  __!|  !  ||  ___!|    _||  ___!|  ___!
                |  !  7|  ___!  7  7  !___  ||  __| |  _ \ |  __|_|  __|_
                |     ||  7     |  |     7  ||  7   |  7  ||     7|     7
                !_____!!__!     !__!     !__!!__!   !__!__!!_____!!_____!
                            - Run At Your Own Risk <<<<<<<<
                            /bye to quit

                """)

            while True:

                prompt = input(     "> ")

                if prompt == "/bye":
                    end_func(gpt)

                client = Client(provider=Provider.MetaAI)
                # Perform the chat completion request
                chat_completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": "Hello"}],
                    stream=True
                )

                for completion in chat_completion:
                    print(completion.choices[0].delta.content or "", end="", flush=True)

                print()
                print()
        else:
            print()
            print(Fore.RED+"        Linux and MacOS Have a little problem to run this tool in terminal You can only use Web Version.")
            end_func(gpt)
    elif guiOrTerminal == "w":
        print(Fore.GREEN+"      Starting Server...")
        print()
        run_gui()
        print(Fore.GREEN+"      Server Is finally stopped.")
        print()
        end_func(gpt)
    else:
        print(Fore.RED+"        Invalid Argument")
        print()
        end_func(gpt)
