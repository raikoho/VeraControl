import subprocess
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

# Global variables
veracrypt_path = r"I:\ProtectedData\VeraCrypt-x64.exe"
volume_path = r"I:\test\test.hc"
mount_letter = "Z"
password = ""

# Functions 

def show_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
╔════════════════════════════════════════════╗
║   V E R A C R Y P T   C O N T R O L L E R  ║
╠════════════════════════════════════════════╣
║  Version 0.8 by Bohdan Misonh              ║
║  For automatic access to encoded disks     ║
╚════════════════════════════════════════════╝
""")

def set_password():
    global password, volume_path
    while True:
        print(f"🗂️  Selected encrypted volume:\n{Fore.YELLOW}→ {volume_path}")
        user_input = input("\n🔑 Enter VeraCrypt password for your encrypted volume (or '0' to select a different volume): ")
        if user_input.strip() == "0":
            change_hc_file()
        else:
            password = user_input
            break

def mount_volume():
    global mount_letter, volume_path, password
    mount_cmd = [
        veracrypt_path,
        "/v", volume_path,
        "/l", mount_letter,
        "/p", password,
        "/q", "/m", "rm", "/a"
    ]
    print(Fore.CYAN + f"⏳ Mounting '{os.path.basename(volume_path)}' as drive {mount_letter}: ...")
    start = time.time()
    try:
        subprocess.run(mount_cmd, check=True)
        print(Fore.GREEN + f"✅ Mounted successfully in {round(time.time() - start, 2)} seconds.")
    except subprocess.CalledProcessError:
        print(Fore.RED + "❌ Failed to mount. Check password, path or drive letter.")

def dismount_volume():
    global mount_letter
    dismount_cmd = [
        veracrypt_path,
        "/d", mount_letter,
        "/q"
    ]
    subprocess.run(dismount_cmd)
    print(Fore.MAGENTA + "🧹 Dismounted and cleaned up.")

def change_drive_letter():
    global mount_letter
    print(Fore.CYAN + "🔁 Drive letters available: " + Fore.YELLOW + "A–Z (except already used ones)")
    new_letter = input(Fore.YELLOW + "Enter new drive letter (e.g. Y): ").upper()
    if len(new_letter) == 1 and new_letter.isalpha():
        mount_letter = new_letter
        print(Fore.GREEN + f"✅ Mount drive letter changed to: {mount_letter}")
    else:
        print(Fore.RED + "❌ Invalid input. Use a single letter A–Z.")

def change_hc_file():
    global volume_path
    print(Fore.CYAN + "📁 Enter full path to your .hc file.")
    print("\nExample: \\\\192.168.1.10\\Shared\\securebox.hc")
    print("Note: You will need to enter the password for the new volume.")
    new_path = input(Fore.YELLOW + "Path to new .hc file: ").strip('" ')
    if os.path.exists(new_path) and new_path.lower().endswith('.hc'):
        volume_path = new_path
        print(Fore.GREEN + f"✅ Encrypted volume set to: {volume_path}")
        set_password()  # Ask password again after changing file
    else:
        print(Fore.RED + "❌ Invalid path or not a .hc file.")

def show_hidden_info():
    print(Fore.CYAN + "\n📜 Program Info & Usage Policy")
    print(Fore.LIGHTWHITE_EX + """
────────────────────────────────────────────
Program: Secure Volume Manager for VeraCrypt
────────────────────────────────────────────
Usage Policy:
• This program helps mount encrypted .hc containers via VeraCrypt
• Do not share passwords over chat or email
• Ensure only authorized users access encrypted volumes
• Container changes and password handling is your responsibility
• This tool is open for automation expansion

────────────────────────────────────────────
    """)

# Start
show_banner()
set_password()

while True:
    print(Fore.CYAN + "\n1. 🔓 Mount encrypted volume")
    print("2. 🔒 Dismount volume")
    print("3. 🔁 Change drive letter (current: " + Fore.YELLOW + mount_letter + Fore.CYAN + ")")
    print("4. 📂 Change encrypted file (.hc) (current: " + Fore.YELLOW + os.path.basename(volume_path) + Fore.CYAN + ")")
    print("5. 🚪 Exit")
    choice = input(Fore.WHITE + "\n👉 Choose option [1-5]: ").strip()

    if choice == "1":
        mount_volume()
    elif choice == "2":
        dismount_volume()
    elif choice == "3":
        change_drive_letter()
    elif choice == "4":
        change_hc_file()
    elif choice == "5":
        print(Fore.LIGHTBLACK_EX + "👋 Exiting VeraCrypt Terminal. Stay secure.")
        break
    elif choice == "6":  # Hidden
        show_hidden_info()
    else:
        print(Fore.RED + "❗ Invalid input. Please choose from 1 to 5.")
