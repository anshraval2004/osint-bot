import requests
import pyfiglet
import os

# Screen clear karne ke liye
os.system('clear')

# 1. Bade words mein title
title = pyfiglet.figlet_format("BY CodeDebug")
print(title)

# 2. Channel link
print("------------------------------------------")
print("Made By @CodeDebug")
print("------------------------------------------\n")

# Input number
phone_number = input("Enter Indian Number (without +91): ")

# API Details
api_url = f"https://numbeer-info.vercel.app/api/lookup?numbere={phone_number}&key=SH4DAW-D4DY"

print("\n[+] Searching details, please wait...")

try:
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Data print karein (API response ke keys ke hisaab se adjust karein)
        print("\n--- RESULTS ---")
        for key, value in data.items():
            print(f"{key.upper()}: {value}")
    else:
        print("\n[!] Error: API se connect nahi ho paya ya key invalid hai.")

except Exception as e:
    print(f"\n[!] Kuch gadbad hui: {e}")

print("\n------------------------------------------")
print("Task Completed!")

