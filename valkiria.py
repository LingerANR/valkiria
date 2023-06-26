import os
from git import Repo
import requests
from colorama import init, Fore, Style
import time
import subprocess
import curses
import random

init()



def baner_2(version):
    banner1 = """
 ██▒   █▓ ▄▄▄       ██▓     ██ ▄█▀ ██▓ ██▀███   ██▓ ▄▄▄      
▓██░   █▒▒████▄    ▓██▒     ██▄█▒ ▓██▒▓██ ▒ ██▒▓██▒▒████▄    
 ▓██  █▒░▒██  ▀█▄  ▒██░    ▓███▄░ ▒██▒▓██ ░▄█ ▒▒██▒▒██  ▀█▄"""  
    banner3 = f"""
  ▒██ █░░░██▄▄▄▄██ ▒██░    ▓██ █▄ ░██░▒██▀▀█▄  ░██░░██▄▄▄▄██ 
   ▒▀█░   ▓█   ▓██▒░██████▒▒██▒ █▄░██░░██▓ ▒██▒░██░ ▓█   ▓██▒
   ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▒ ▓▒░▓  ░ ▒▓ ░▒▓░░▓   ▒▒   ▓▒█░
   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░░ ░▒ ▒░ ▒ ░  ░▒ ░ ▒░ ▒ ░  ▒   ▒▒ ░
     ░░    ░   ▒     ░ ░   ░ ░░ ░  ▒ ░  ░░   ░  ▒ ░  ░   ▒   
      ░        ░  ░    ░  ░░  ░    ░     ░      ░        ░  ░  {version}
     ░                                                       
      ====== KEEP YOUR SECRETS HIDDEN FROM THE WORLD ====="""

    print(Fore.LIGHTCYAN_EX + banner1  + Fore.LIGHTMAGENTA_EX + banner3)

def banner_3(version):
    banner = f"""
       _                           ..       ..         .                    .                
  u                      x .d88"  < .z@8"`        @88>                 @88>              
 88Nu.   u.               5888R    !@88E          %8P      .u    .     %8P               
'88888.o888c       u      '888R    '888E   u       .     .d88B :@8c     .          u     
 ^8888  8888    us888u.    888R     888E u@8NL   .@88u  ="8888f8888r  .@88u     us888u.  
  8888  8888 .@88 "8888"   888R     888E`"88*"  ''888E`   4888>'88"  ''888E` .@88 "8888" 
  8888  8888 9888  9888    888R     888E .dN.     888E    4888> '      888E  9888  9888  
  8888  8888 9888  9888    888R     888E~8888     888E    4888>        888E  9888  9888  
 .8888b.888P 9888  9888    888R     888E '888&    888E   .d888L .+     888E  9888  9888  
  ^Y8888*""  9888  9888   .888B .   888E  9888.   888&   ^"8888*"      888&  9888  9888  
    `Y"      "888*""888"  ^*888%  '"888*" 4888"   R888"     "Y"        R888" "888*""888" 
              ^Y"   ^Y'     "%       ""    ""      ""                   ""    ^Y"   ^Y'    {version}
              
                 ====== KEEP YOUR SECRETS HIDDEN FROM THE WORLD ====="""
    print(Fore.LIGHTGREEN_EX + banner)
def banner_1(version):
    banner = f"""
    ██╗   ██╗ █████╗ ██╗     ██╗  ██╗██╗██████╗ ██╗ █████╗
    ██║   ██║██╔══██╗██║     ██║ ██╔╝██║██╔══██╗██║██╔══██╗
    ██║   ██║███████║██║     █████╔╝ ██║██████╔╝██║███████║
    ╚██╗ ██╔╝██╔══██║██║     ██╔═██╗ ██║██╔══██╗██║██╔══██║
     ╚████╔╝ ██║  ██║███████╗██║  ██╗██║██║  ██║██║██║  ██║ 
      ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝  {version}
     
      ====== KEEP YOUR SECRETS HIDDEN FROM THE WORLD ====="""

    print(Fore.CYAN + banner)

def launcher():
    set_terminal_size()
    ruta_archivo = "run_app.py"
    os.system('python3 {}'.format(ruta_archivo))

def set_terminal_size():
    os.system("printf '\e[8;50;135t'")

def animate(duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        for char in '|/-\\':
            print("Launching Valkiria . . . " + char, end='\r') 
            time.sleep(0.1)  

def check_updates():
    # Ruta local del repositorio
    repo_path = '.'

    # Verificar si el repositorio existe
    if not os.path.exists(repo_path):
        print("El repositorio no existe en la ruta especificada.")
        return

    # Abrir el repositorio
    repo = Repo(repo_path)

    # Obtener el nombre de la rama actual
    current_branch = repo.active_branch.name
    # print("\nCurrent Branch: " + Style.BRIGHT + Fore.LIGHTYELLOW_EX + current_branch)
    remote_url = repo.remote().url

    # Extraer el nombre del usuario y el nombre del repositorio del URL remoto
    user_repo = remote_url.split(':')[-1].split('.git')[0]

    # Obtener la última confirmación en la rama actual
    latest_commit = repo.head.commit.hexsha

    # Obtener la última confirmación en la rama remota
    url = f"https://api.github.com/repos/{user_repo}/commits/{current_branch}"
    response = requests.get(url)
    if response.status_code == 200:
        remote_commit = response.json()['sha']
    else:
        print("Error al obtener la última confirmación en la rama remota.")
        return
    # Verificar si hay cambios en el repositorio
    if latest_commit != remote_commit:
        print("Status: " + Style.BRIGHT + Fore.LIGHTYELLOW_EX + "UPDATE AVAILABLE" + Style.RESET_ALL)
        # Realizar las acciones necesarias para actualizar el repositorio aquí
        choise = input("Do you want to update Valkiria? [yes/no]: ")
        if choise.lower() == "yes" or choise.lower() == "y":
            print("Updating Valkiria . . .")
            command = f"git pull origin {current_branch}"
            os.system(command)
            print("Updated!")
        else:
            pass 
    else:
        print("\nStatus: " + Style.BRIGHT + Fore.LIGHTYELLOW_EX + "OK")

# Ejecutar la función al iniciar el programa
if __name__ == '__main__':
    duracion = 2
    os.system('clear')
    os.system("printf '\e[8;24;100t'")
    banner_option = random.randint(1, 3)
    version = "v1.3.3"
    if banner_option == 1:
        banner_1(version)
    elif banner_option == 2:
        baner_2(version)
    else:
        banner_3(version)
    check_updates()
    animate(duration=duracion)
    launcher()