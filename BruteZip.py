#!/usr/bin/env python3
import os
import sys
import subprocess
import concurrent.futures
import time
# Colors
GREEN = "\033[1;92m"
CYAN = "\033[1;96m"
MAGENTA = "\033[1;35m"
YELLOW = "\033[1;33m"
RED = "\033[1;91m"
BLUE = "\033[1;94m"
RESET = "\033[0m"

def anime(text):
    for txt in text:
        sys.stdout.write(txt)
        sys.stdout.flush()
        time.sleep(0.04)

# Default Wordlist Path
AUTO_WORDLIST = "/data/data/com.termux/files/home/PDF-Unlocker/wordlist.txt"

# Number of threads (Increase for more speed)
MAX_THREADS = os.cpu_count() * 2  # Uses double the CPU cores for fast execution

# Banner
def show_banner():
    os.system("clear")
    print(f"""{GREEN}
__________                __         __________.__
\______   \_______ __ ___/  |_  ____ \____    /|__|_____
 |    |  _/\_  __ \  |  \   __\/ __ \  /     / |  \____ \\
 |    |   \ |  | \/  |  /|  | \  ___/ /     /_ |  |  |_> >
 |______  / |__|  |____/ |__|  \___  >_______ \|__|   __/
        \/                         \/        \/   |__|
{RESET}""")
    # पहले बिना कलर के टेक्स्ट को सेंटर करो
    # पहले बिना कलर के टेक्स्ट को सेंटर करो
    text1 = "★ BruteZip - ZIP/7z Brute-Force Tool ★".center(55) 

    # अब स्टार को ग्रीन, टेक्स्ट को मैजेंटा और बाकी को Cyan करो
    text1 = text1.replace("★", f"{GREEN}★{CYAN}")  
    text1 = text1.replace("BruteZip - ZIP/7z Brute-Force Tool", f"{MAGENTA}BruteZip - ZIP/7z Brute-Force Tool{CYAN}")

    # एनिमेशन के साथ प्रिंट करो
    anime(f"{CYAN}{text1}{RESET}")

    # **नई लाइन डालने के लिए `print()`**
    print()

    # दूसरे टेक्स्ट को सेंटर करो
    text2 = "Coded by: Rakibul | GitHub: Rakibul0909".center(55)

    # "Rakibul" को ग्रीन और "GitHub: Rakibul0909" को येलो करो
    text2 = text2.replace("Rakibul", f"{GREEN}Rakibul{MAGENTA}", 1)  
    text2 = text2.replace("GitHub: Rakibul0909", f"{YELLOW}GitHub: Rakibul0909{MAGENTA}")

    # एनिमेशन के साथ प्रिंट करो
    anime(f"{MAGENTA}{text2}{RESET}\n\n\n")

# Password testing function (Multi-threaded)
def test_password(file_path, password):
    password = password.strip()
    print(f"{BLUE}Trying password: {password}{RESET}", flush=True)

    try:
        result = subprocess.run(["7z", "t", file_path, f"-p{password}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        if result.returncode == 0:
            print(f"\n{GREEN}[✓] Password Found: {password}{RESET}\n")
            os._exit(0)  # Stop execution if password is found
    except subprocess.CalledProcessError:
        pass  # Ignore errors for wrong passwords

# Brute-Force Function (Optimized Multi-threading)
def brute_force_p7zip(file_path, wordlist):
    if not os.path.exists(file_path):
        print(f"{RED}[×] Error: File not found!{RESET}")
        sys.exit(1)

    if not os.path.exists(wordlist):
        print(f"{RED}[×] Error: Wordlist not found!{RESET}")
        sys.exit(1)

    # Read passwords
    with open(wordlist, "r", encoding="utf-8") as wl:
        passwords = [password.strip() for password in wl.readlines()]
    print ()
    print(f"{GREEN}[+] Starting Brute-Force Attack ....{RESET}\n")

    # Use ThreadPoolExecutor for fast parallel processing
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(lambda p: test_password(file_path, p), passwords)

    print(f"{RED}[×] Password Not Found!{RESET}\n")
    sys.exit(1)

# Main Function
if __name__ == "__main__":
    show_banner()

    print(f"{CYAN}[1] Start Brute force attack{RESET}")
    print(f"{CYAN}[2] Exit{RESET}")

    option = input(f"\n{GREEN}Set option ⟩ {RESET}")

    if option == "1":
        print(f"\n{CYAN}[1] Use Auto Wordlist{RESET}")
        print(f"{CYAN}[2] Use Custom Wordlist{RESET}")
        print(f"{CYAN}[3] Exit{RESET}")

        wordlist_option = input(f"\n{GREEN}Set option ⟩ {RESET}")

        if wordlist_option == "1":
            file_path = input(f"\n{MAGENTA}➤ Enter the ZIP/7z file path ⟩ {RESET}")
            brute_force_p7zip(file_path, AUTO_WORDLIST)

        elif wordlist_option == "2":
            file_path = input(f"\n{MAGENTA}➤ Enter the ZIP/7z file path ⟩ {RESET}")
            print()
            wordlist = input(f"{MAGENTA}➤ Enter the wordlist file path ⟩ {RESET}")
            brute_force_p7zip(file_path, wordlist)

        elif wordlist_option == "3":
            print(f"{RED}Exiting...{RESET}")
            sys.exit(0)

        else:
            print(f"{RED}Invalid option! Please choose 1, 2, or 3.{RESET}")
            sys.exit(1)

    elif option == "2":
        print(f"{RED}Exiting...{RESET}")
        sys.exit(0)

    else:
        print(f"{RED}Invalid option! Please choose 1 or 2.{RESET}")
        sys.exit(1)
