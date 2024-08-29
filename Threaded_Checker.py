import requests
with open("codes.txt", "r") as file:
    codes = [line.strip() for line in file]

from colorama import Fore, Back, Style
import time
import threading
print(Fore.RED + r"""
 ____  __   __ _   _   ____ __        __   _     ____   _____ 
/ ___| \ \ / /| \ | | / ___|\ \      / /  / \   |  _ \ | ____|
\___ \  \ V / |  \| || |     \ \ /\ / /  / _ \  | |_) ||  _|  
 ___) |  | |  | |\  || |___   \ V  V /  / ___ \ |  _ < | |___ 
|____/   |_|  |_| \_| \____|   \_/\_/  /_/   \_\|_| \_\|_____|
                                                               
    """)
print(Style.RESET_ALL)
print(Fore.YELLOW + "Co-pilot is the one wrigint my co- No wait-")
print(Fore.GREEN + " ")
print(Fore.LIGHTCYAN_EX + "[XGPC Checker]")
print(Fore.LIGHTCYAN_EX + " ")
print(Style.RESET_ALL) 



if len(codes) == 0:
    print(Fore.RED + "No codes found in codes.txt")
    input("Press Enter to exit...")
    print(Style.RESET_ALL)
    exit()
print(Fore.LIGHTCYAN_EX + f"Loaded {len(codes)} codes")
print(Fore.LIGHTCYAN_EX + " ")
print(Style.RESET_ALL)
num_threads = int(input("Enter the number of threads. Max: " + str(len(codes)) + ", Don't use anything over 50. \n > ") )
input("Press Enter to start checking codes...")    

def checkcodes(codes):
    
    global invalid_count
    global valid_count
    global used_count
    valid_count = 0
    used_count = 0
    invalid_count = 0
    for code in codes:
        url = "https://emerald.xboxservices.com/xboxcomfd/buddypass/ValidateOfferRedeemer?market=US&offerId=" + code

        headers = {
            "your",
            "headers",
            "here"
            }
 

        response = requests.get(url, headers=headers)
        if response.text == "\"ClaimedOffersMaxed\"":
            used_count += 1
            print(Fore.YELLOW + f"- {code} is used")
        elif response.text == "\"OfferValid\"":
            valid_count += 1
            print(Fore.GREEN + f"+ {code} is eligible | saved to valid_codes.txt")
            with open("valid_codes.txt", "a") as file:
                file.write(code + "\n")
        elif response.text == "\"OfferNotFound\"":
            invalid_count += 1
            print(Fore.RED + f"- {code} is invalid") 
        elif response.text == "\"OfferAlreadyClaimed\"":
            invalid_count += 1
            print(Fore.RED + f"- {code} is used")
        else:
            print(Fore.RED + f"- {code} is {response.text}")   

    



# Divide the codes into equal chunks for each thread
chunk_size = len(codes) // num_threads
code_chunks = [codes[i:i+chunk_size] for i in range(0, len(codes), chunk_size)]

# Create a list to hold the thread objects
threads = []

# Define the checkcodes function to be executed by each thread
def checkcodes_thread(codes):
    checkcodes(codes)

# Create and start the threads
for chunk in code_chunks:
    thread = threading.Thread(target=checkcodes_thread, args=(chunk,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(Fore.RED + f"- Invalid Codes: {invalid_count}")
print(Fore.GREEN + f"+ Valid Codes: {valid_count}")
print(Fore.YELLOW + f"- Used Codes: {used_count}")
print(Style.RESET_ALL)
input("Press Enter to exit...")
print(Style.RESET_ALL)
exit()
