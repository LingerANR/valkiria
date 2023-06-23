import os
from git import Repo
import requests
from colorama import init, Fore, Style
import time
import subprocess
import curses

init()

def start_valkiria():
    banner = """
    ██╗   ██╗ █████╗ ██╗     ██╗  ██╗██╗██████╗ ██╗ █████╗
    ██║   ██║██╔══██╗██║     ██║ ██╔╝██║██╔══██╗██║██╔══██╗
    ██║   ██║███████║██║     █████╔╝ ██║██████╔╝██║███████║
    ╚██╗ ██╔╝██╔══██║██║     ██╔═██╗ ██║██╔══██╗██║██╔══██║
     ╚████╔╝ ██║  ██║███████╗██║  ██╗██║██║  ██║██║██║  ██║ 
      ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝  v1.1.0
     
      ====== KEEP YOUR SECRETS HIDDEN FROM THE WORLD ====="""

    print(Fore.CYAN + banner)

def launcher():
    colunmas = 132
    filas = 24
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
            print(char, end='\r')  # Imprimir en la misma línea
            time.sleep(0.1)  # Retraso para el efecto de animación

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
    print(current_branch)
    # Obtener la URL del repositorio remoto
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
        print("¡Hay cambios en el repositorio!")
        # Realizar las acciones necesarias para actualizar el repositorio aquí
    else:
        print("El repositorio está actualizado.")

# Ejecutar la función al iniciar el programa
if __name__ == '__main__':
    duracion = 3
    os.system('clear')
    start_valkiria()
    check_updates()
    print("starting valkiria . . . ")
    animate(duration=duracion)
    launcher()