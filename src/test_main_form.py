import npyscreen
from  test_encrypt_form import EncryptForm
import os
import logging
from test_log_box import LogBoxTitle as LogBox

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

class MainForm( npyscreen.FormBaseNew ):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.should_exit = False

    def while_waiting(self):
        npyscreen.notify_wait("Update")
        self.log_box.update_logs()
        self.display() 

    def create(self):
        self.name = "Valkiria Main"
        self.art_box = self.add(npyscreen.BoxTitle, max_height=9, rely=1, width=60, editable=False)
        self.art_box.values = [
            "██╗   ██╗ █████╗ ██╗     ██╗  ██╗██╗██████╗ ██╗ █████╗ ",
            "██║   ██║██╔══██╗██║     ██║ ██╔╝██║██╔══██╗██║██╔══██╗",
            "██║   ██║███████║██║     █████╔╝ ██║██████╔╝██║███████║",
            "╚██╗ ██╔╝██╔══██║██║     ██╔═██╗ ██║██╔══██╗██║██╔══██║",
            " ╚████╔╝ ██║  ██║███████╗██║  ██╗██║██║  ██║██║██║  ██║",
            "  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝",
            " TUI Encryption Tool        BY        LingerANR "]
    
        self.logs = []
        # Mover de posicion los botones
        self.add(npyscreen.ButtonPress, name="Encrypt a file", rely=11, when_pressed_function=self.show_encrypt_form)
        self.add(npyscreen.ButtonPress, name="Decrypt a file",rely=12, max_height=2, width=30, when_pressed_function=self.show_decrypt_form)
        self.add(npyscreen.ButtonPress, name="Make File",rely=13, max_height=2, width=30, when_pressed_function=self.show_make_file_form)
        self.add(npyscreen.ButtonPress, name="Read File",rely=14, max_height=2, width=30, when_pressed_function=self.show_read_form)
        # self.add(npyscreen.ButtonPress, name="Generate Key",rely=14, max_height=2, width=30, when_pressed_function=self.add_log)
        self.add(npyscreen.ButtonPress, name="Exit",rely=15, max_height=2, width=30, when_pressed_function=self.action_exit)
        self.log_box = self.add(LogBox, name="Logs", relx=2, rely=17, max_height=19, width=60, editable=True)
        self.add_handlers({
            "^E": self.show_encrypt_form,
        })

    # Revisar los logs
    def add_log( self ):
        logging.info("Entre en el metodo add_log, LOG = " + log)
        self.logs.append(log)
        logging.info(self.logs)

    def action_exit( self ):
        quit()

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
        # experimento
        self.log_box.update_logs()
    
    # Limpiar el codigo
    def beforeEditing( self ):
        self.log_box.update_logs()

# class LogBoxTitle(npyscreen.BoxTitle):
#     _contained_widget = npyscreen.MultiLineEditable

#     def update_logs( self ):
#         with open("log.txt", "r") as file:
#             logs = file.read().splitlines()
#         self.entry_widget.values = logs
#         self.entry_widget.start_display_at = len(logs) - self.entry_widget.height
#         self.entry_widget.cursor_line = len(logs) - 1
#         self.entry_widget.display()
