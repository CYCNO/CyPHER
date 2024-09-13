import requests
import gdshortener
from utils import Error, clear_terminal, end_func
from colorama import init, Fore

def urlShortner():
    clear_terminal()
    # Initialize Colorama
    init(autoreset=True)

    try:
        print(Fore.GREEN+"""
            _  _  ____  __      ____  _  _   __  ____  ____  __ _  ____  ____
           / )( \(  _ \(  )    / ___)/ )( \ /  \(  _ \(_  _)(  ( \(  __)(  _ \
           ) \/ ( )   // (_/\  \___ \) __ ((  O ))   /  )(  /    / ) _)  )   /
           \____/(__\_)\____/  (____/\_)(_/ \__/(__\_) (__) \_)__)(____)(__\_)


                     - change your lenghty url to short one.

                     available shortner - ulbvis.net, is.gd


            """)
        url = input(Fore.GREEN+"       > Enter Your Url That You Want To Short: ")
        print(Fore.GREEN+"""
                        1. ulvis.net
                        2. is.gd

                    """)
        domain = input(Fore.GREEN+"         > Select Url Shortner Domain: ")
        if domain == "1": ##ulvis.net
            response = requests.get("https://ulvis.net/api.php?url={}".format(url))
            print()
            print(Fore.GREEN+"      Url Shorted: "+ response.text)
#        elif domain == "3": # url.dev
        #    url3 = "https://url.api.stdlib.com/temporary@0.3.0/create/"
        #    data = {"url": url,'ttl': 604800}
        #    response2 = requests.post(url3, data=data).json()["link_url"]
        #    print(Fore.GREEN+"      Url Shorted: "+ response2)
        elif domain == "2": ## is.gd
            s = gdshortener.ISGDShortener()
            response3 = s.shorten(url)[0]
            print(Fore.GREEN+"      Url Shorted: "+ response3)
        else:
            print(Fore.RED+"        Invalid Argument")
        end_func(urlShortner)
    except Exception as e:
        Error(e)

### TODO - Add timing for expiry in url.dev
