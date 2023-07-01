import setuptools

setuptools.setup(
    name="valkiria-proyect",
    version="2.3.3",
    author="Giovanni Vera (Linger)",
    description="""File encryption tool. This is a project, it is still in beta phase, 
                   the personal role is to help me understand modular programming and encryption algorithms.""",
    packages=setuptools.find_packages(),
    install_requires=[
        'colorama==0.4.0',
        'cryptography==3.4.8',
        'funcy==1.11',
        'GitPython==3.1.31',
        'npyscreen==4.10.5',
        'pycryptodome==3.7.0',
        'Requests==2.31.0',
        'rsa==4.9',
    ],
)

# Crear el directorio ".files" en el nivel de la carpeta raíz
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_dir, ".files")
if not os.path.exists(files_dir):
    os.makedirs(files_dir)
    print("[ + ] Files Directory Created!")
else:
    print("[ ! ] Files Directory already exist!")
