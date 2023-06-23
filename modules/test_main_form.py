import npyscreen
from modules.test_encrypt_form import EncryptForm
import os
import logging
import threading
import time
import signal

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

class MainForm( npyscreen.FormBaseNew ):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.should_exit = False

    def create(self):
        
        #  Las siguientes lineas sirven para mostarr el formulario en determinada posicion de la terminal
        # self.show_atx = 20
        # self.show_aty = 5
        self.art_box = self.add(npyscreen.BoxTitle, max_height=9, rely=1, width=60, editable=False)
        self.art_box.values = [
            "██╗   ██╗ █████╗ ██╗     ██╗  ██╗██╗██████╗ ██╗ █████╗ ",
            "██║   ██║██╔══██╗██║     ██║ ██╔╝██║██╔══██╗██║██╔══██╗",
            "██║   ██║███████║██║     █████╔╝ ██║██████╔╝██║███████║",
            "╚██╗ ██╔╝██╔══██║██║     ██╔═██╗ ██║██╔══██╗██║██╔══██║",
            " ╚████╔╝ ██║  ██║███████╗██║  ██╗██║██║  ██║██║██║  ██║",
            "  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝",
            " RSA-FERNET Encryption Tool        BY        LingerANR "]
    
        self.logs = []
        self.add(npyscreen.ButtonPress, name="Encrypt a file", when_pressed_function=self.show_encrypt_form)
        self.add(npyscreen.ButtonPress, name="Decrypt a file",rely=11, max_height=2, width=30, when_pressed_function=self.show_decrypt_form)
        self.add(npyscreen.ButtonPress, name="Make File",rely=12, max_height=2, width=30, when_pressed_function=self.show_make_file_form)
        self.add(npyscreen.ButtonPress, name="Read File",rely=13, max_height=2, width=30, when_pressed_function=self.show_read_form)
        self.add(npyscreen.ButtonPress, name="Generate Key",rely=14, max_height=2, width=30, when_pressed_function=self.add_log)
        self.add(npyscreen.ButtonPress, name="Exit",rely=15, max_height=2, width=30, when_pressed_function=self.action_exit)
        self.log_box = self.add(LogBoxTitle, name="Logs", relx=2, rely=21, max_height=15, width=60, editable=True)
        self.add_handlers({
            "^E": self.show_encrypt_form,
        })

    def add_log( self ):
        logging.info("Entre en el metodo add_log, LOG = " + log)
        self.logs.append(log)
        logging.info(self.logs)

    def action_exit( self ):
        self.exit()

    def show_encrypt_form( self, *args, **kwargs ):
        logging.info("Entre al encrypt...")
        inner_form = self.parentApp.getForm('ENCRYPT')
        inner_form.edit()

    def show_make_file_form( self ):
        logging.info("Entre al a MAKE FILE...")
        inner_form = self.parentApp.getForm('MAKE')
        inner_form.edit()

    def show_read_form( self, *args, **kwargs ):
        inner_form = self.parentApp.getForm('READER')
        inner_form.edit()

    def show_decrypt_form( self, *args, **kwargs ):
        inner_form = self.parentApp.getForm('DECRYPT')
        inner_form.edit()

    def afterEditing( self ):
        logging.info("Entre a afterEditing...")

    # def on_ok(self):
    #     selected_choice = self.choice.get_selected_objects()[0]
    #     if selected_choice == 'Encrypt':
    #         self.parentApp.getForm('ENCRYPT').file_path.value = ""
    #         self.parentApp.getForm('ENCRYPT').key_path.value = ""
    #         self.parentApp.switchForm("ENCRYPT")
    #     elif selected_choice == 'Decrypt':
    #         self.parentApp.getForm('DECRYPT').file_path.value = ""
    #         self.parentApp.getForm('DECRYPT').key_path.value = ""
    #         self.parentApp.switchForm("DECRYPT")
    #     elif selected_choice == 'Make File':
    #         self.parentApp.getForm('MAKE').file_name.value = ""
    #         self.parentApp.getForm('MAKE').content.value = ""
    #         self.parentApp.getForm('MAKE').key_path.value = ""
    #         self.parentApp.switchForm("MAKE")
    #     elif selected_choice == 'Generate Key':
    #         LmeRsa.generate_key_pair()
    #         npyscreen.notify_confirm(f"Keys created.", "Key File Success")

    def beforeEditing( self ):
        # with open("log.txt", "r") as file:
        #     logs = file.read().splitlines()
        # self.log_box.update_logs(logs)
        self.log_box.update_logs()

class LogBoxTitle(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEditable

    def update_logs( self ):
        with open("log.txt", "r") as file:
            logs = file.read().splitlines()
        self.entry_widget.values = logs
        logging.info("INDEX: " + str(len(logs)))
        self.entry_widget.start_display_at = len(logs) - self.entry_widget.height
        self.entry_widget.cursor_line = len(logs) - 1
        self.entry_widget.display()
