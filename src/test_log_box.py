import npyscreen

class LogBoxTitle(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEditable

    def update_logs( self ):
        with open("log.txt", "r") as file:
            logs = file.read().splitlines()
        self.entry_widget.values = logs
        self.entry_widget.start_display_at = len(logs) - self.entry_widget.height
        self.entry_widget.cursor_line = len(logs) - 1
        self.entry_widget.display()