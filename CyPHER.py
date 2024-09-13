from tools import file_uploader, tempmail, url_shortner, chatgpt4free
from colorama import Fore, init
from utils import clear_terminal, readme

def main():
    clear_terminal()
    # Initialize Colorama
    init(autoreset=True)

    print(Fore.GREEN +"""
                        ·······································
                        :       ___     ___ _  _ ___ ___      :
                        :      / __|  _| _ \ || | __| _ \     :
                        :     | (_| || |  _/ __ | _||   /     :
                        :      \___\_, |_| |_||_|___|_|_\     :
                        :          |__/                       :
                        ·······································

                    1. Upload File                  2. ChatGptFree
                    3. Url Shortner                 4. Temp Mail

                    98. Readme                      99. Exit

        """)
    selectTool = input("       > Which Tool You Want To Use: ")

    if selectTool == "1":
        file_uploader.uploadFile()
    elif selectTool == "2":
        chatgpt4free.gpt()
    elif selectTool == "3":
        url_shortner.urlShortner()
    elif selectTool == "4":
        tempmail.tempmail()
    elif selectTool == "98":
        readme()
    elif selectTool == "99":
        quit()

main()
