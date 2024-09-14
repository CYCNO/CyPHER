from colorama import Fore
import os
import sys

def Error(e):
    print(Fore.RED + f"""
        Got an error - {e}

        If you think this is an error in the code. Please Create A Issue In Github Repo - https://github.com/CYCNO/CyPHER/issues.
""")

def clear_terminal():
    # Clear the terminal screen based on the operating system
    os_name = os.name
    if os_name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')

def end_func(funcname):
    print()
    homeOrRestart = input(Fore.RED + "     > Do You Want To Go Main Menu Or Restart this Tools (m/r): ")
    if homeOrRestart == "m":
        from CyPHER import main
        main()
    elif homeOrRestart == "r":
        funcname()
    else:
            print(Fore.RED + "      Invalid input. Please enter 'm' or 'r'.")
            end_func(funcname)


def readme():
    clear_terminal()
    print(Fore.GREEN+"""
                                    ______ _____  ___ _________  ___ _____
                                    | ___ \  ___|/ _ \|  _  \  \/  ||  ___|
                                    | |_/ / |__ / /_\ \ | | | .  . || |__
                                    |    /|  __||  _  | | | | |\/| ||  __|
                                    | |\ \| |___| | | | |/ /| |  | || |___
                                    \_| \_\____/\_| |_/___/ \_|  |_/\____/


                Hello users, I hope you will like the tools provided in this project. If
                you found any bug that you think is not caused by your side or is in the
                code, you can create a new issue in https://github.com/CYCNO/CyPHER/issues

                There is not much terms or condition because i dont like that, but please don't
                use this tools to bully, exploit or any type of bad stuff that violates any law,
                also you will be responsible for how you use these tool(s).

                If you are dev, and have some tool(s) created by you, that you think will be good
                for people, please add your tool(s) in this project by commiting your code and
                creating a pull request here - https://github.com/CYCNO/CyPHER/pulls
                And please don't obfuscate the code because this project is truly about opensource.

                At the last give us a star in github and enjoy the tools.

        """)
    end_func(readme)
