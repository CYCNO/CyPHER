import requests
from tkinter import filedialog
from tkinter import Tk
from colorama import Fore, init
from utils import Error, clear_terminal, end_func

def uploadFile():
    clear_terminal()
    # Initialize Colorama
    init(autoreset=True)

    try:
        print(Fore.GREEN + """
            ___ _ _                    _                 _
           / __(_) | ___   /\ /\ _ __ | | ___   __ _  __| | ___ _ __
          / _\ | | |/ _ \ / / \ \ '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
         / /   | | |  __/ \ \_/ / |_) | | (_) | (_| | (_| |  __/ |
         \/    |_|_|\___|  \___/| .__/|_|\___/ \__,_|\__,_|\___|_|
                                |_|

                             - Upload File For Free and get a link of the file to download
            """)

        ask = input(Fore.RED + "     > Do You Wanna Select The File (y/n): ").strip().lower()
        if ask in ("y", "yes"):
            try:
                # Initialize Tkinter for file dialog
                root = Tk()
                root.withdraw()  # Hide the root window

                filepath = filedialog.askopenfilename()
                if not filepath:
                    print(Fore.RED + "     No File Selected")
                    return

                print(Fore.GREEN + "     File Selected: " + filepath)
                print(Fore.GREEN + "     Uploading...")

                url = "https://store2.gofile.io/contents/uploadfile"

                # Open the file in binary mode
                with open(filepath, "rb") as file:
                    # Prepare the payload for the POST request
                    files = {
                        'file': (filepath, file),
                    }

                    # Make the POST request to upload the file
                    response = requests.post(url, files=files)

                print()
                # Check if the request was successful
                if response.status_code == 200:
                    print(Fore.GREEN + "     File Uploaded Successfully.")
                    print(Fore.GREEN + "     Download Link - " + response.json()["data"]["downloadPage"])
                else:
                    print(Fore.RED + "     Failed to upload file. Status code: " + str(response.status_code))

            except Exception as e:
                print(Fore.RED + f"     An error occurred: {e}")
        elif ask in ("n", "no"):
            print(Fore.RED + "      No File Selected")
        else:
            print(Fore.RED + "      Invalid input. Please enter 'y' or 'n'.")
        end_func(uploadFile)
    except Exception as e:
        print(Fore.RED + f"     An error occurred: {e}")
