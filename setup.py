import os
import time
from modules.lme_rsa import LmeRsa


def check_directory():
    existing_dirs = 0
    if os.path.exists(".files") and os.path.isdir(".files"):
        print("[+] Files directory OK")
        existing_dirs += 1
    else:
        print("[x] Files Directory not Found.")
        print("[!] Creating directory . . .")
        os.system('mkdir .files')
        print("[+] DONE.")

    if os.path.exists(".fernet") and os.path.isdir(".fernet"):
        print("[+] Fernet directory OK")
        existing_dirs += 1
    else:
        print("[x] Fernet Directory not Found.")
        print("[!] Creating directory . . .")
        os.system('mkdir .fernet')
        print("[+] DONE.")

    if os.path.exists(".rsa") and os.path.isdir(".rsa"):
        print("[+] RSA directory OK")
        existing_dirs += 1
    else:
        print("[x] RSA Directory not Found.")
        print("[!] Creating directory . . .")
        os.system('mkdir .rsa')
        print("[+] DONE.")
    return existing_dirs

def install_requirements():
    os.system('pip3 install -r requirements.txt')

def generate_keys():
    lme_rsa = LmeRsa
    keys = lme_rsa.generate_key_pair()
    if keys:
        print("[+] Keys Created!")
    print("[!] Encrypting Fernet Key . . .")
    fernet_encrypted = lme_rsa.encrypt_fernet_key(".fernet/lme.key")
    if fernet_encrypted:
        print("[+] Fernet Key Encrypted!")

def warning():
    message = """
    IMPORTANT: Keep your RSA Private key safe, since it is used to access the Fernet key.

    [!] .files ---> Where the files Created with Valkyrie are saved
    [!] .fernet ---> Where the Fernet key (lme.key) is stored
    [!] .rsa ---> Where the RSA keys (.pem) are stored

    [!] To run the program from Now you must execute 'python3 valkiria.py'

    Any inconvenience please report it to the github repository:
    [+] https://github.com/LingerANR/valkiria"""

def run_valkiria_launcher(option):
    if option.lower() == 'yes' or option.lower() == 'y':
        os.system('python3 valkiria.py')
    else:
        print("[+] Installation complete, good luck :) ")
        exit()


os.system('clear')
print("Welcome! Let's setup Valkiria!\n")
existing_dirs = check_directory()

if existing_dirs == 3:
    print("\nIt seems that the directories have been created.")
    choise = input("Do you want to run Valkiria? [yes/no]: ")
    if choise.lower() == "yes" or choise.lower() == 'y':
        os.system('python3 valkiria.py')
    else:
        choise2 = input("Do you want to run the Requirements file? [yes/no]: ")
        if choise2.lower() == "yes" or choise2.lower() == 'y':
            install_requirements()
        else:
            print("ok bye :)")
else:
    install_requirements()
    generate_keys()
    warning()
    run = input("\n Run Valkiria? [yes/no]: ")
    run_valkiria_launcher(run)