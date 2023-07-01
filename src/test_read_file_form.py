import npyscreen
import os
import textwrap

class ReadFile(npyscreen.Form):
    def afterEditing(self):
        self.file_content.values = ''
        self.parentApp.switchForm('MAIN')

    def create(self):
        self.show_atx = 63
        self.show_aty = 1
        self.file_content = self.add(npyscreen.MultiLineEdit, value='', editable=True, scroll_exit=True)
        # self.file_content = self.add(npyscreen.BoxTitle,
        #                              name="Archivo",
        #                              max_width=self.columns - 5,
        #                              max_height=self.lines - 5,
        #                              editable=False)

    def load_file_content(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        # self.file_content.value = content
        lines = content.split('\n')
        wrapped_lines = []
        for line in lines:
            wrapped_lines.extend(textwrap.wrap(line, self.file_content.width))
        wrapped_content = '\n'.join(wrapped_lines)
        self.file_content.value = wrapped_content
        os.remove(file_path)

    # def beforeEditing(self):
    #     # Obtener el ancho de la ventana
    #     window_width = self.columns - 8  # Restar el ancho de los márgenes

    #     # Dividir el texto en líneas envueltas
    #     wrapped_lines = textwrap.wrap(self.file_content.value, width=window_width + 1)

    #     # Actualizar el contenido del widget con las líneas envueltas
    #     self.file_content.values = wrapped_lines
        