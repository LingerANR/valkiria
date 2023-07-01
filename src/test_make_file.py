import npyscreen
from  lme_rsa import LmeRsa


class MakeFileForm(npyscreen.ActionForm):
    def create(self):
        self.show_atx = 63
        self.show_aty = 1
        # self.file_name = self.add(FileNameBox, name="File Name", relx=2, rely=21, max_height=15, width=60, contained_widget_arguments={'name': ''})
        # self.file_name = self.add(npyscreen.MultiLineEditableBoxed, name = "File Name", max_height=6, editable=True)
        self.file_name = self.add(npyscreen.TitleText, name="File Name:")
        self.content = self.add(npyscreen.MultiLineEdit, value="", max_height=25)
        self.key_path = self.add(npyscreen.TitleText, name = "Key: ")

    def on_ok(self):
        # encrypt = EncryptForm()
        # key = encrypt.load_key(self.key_path.value)
        # self.encrypt(self.file_name.value, self.content.value, key)
        self.save_file(self.file_name.value, self.content.value, self.key_path.value)
        self.clear_form()

    def clear_form( self ):
        self.file_name.value = ""
        self.content.value = ""
        self.key_path.value = ""

    # def encrypt(self, file_name, content, key):
    #     key_data = Fernet(key)
    #     content_bytes = content.encode()
    #     encrypted_data = key_data.encrypt(content_bytes)
    #     encypted_file_path = file_name + ".lme"
    #     with open(encypted_file_path, "wb") as file_encrypted:
    #         file_encrypted.write(encrypted_data)
    #     npyscreen.notify_confirm("File encrypted and saved successfully.", "Success")
    #     self.parentApp.switchForm("MAIN")

    def save_file(self, file_name, content, key_encrypted):
        content_bytes = content.encode()
        file_path = ".files/" + file_name
        with open(file_path, "wb") as file:
            file.write(content_bytes)
        LmeRsa.encrypt(self, file_path, key_encrypted)
        npyscreen.notify_confirm("File saved", "Saved")

class FileNameBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.TitleText