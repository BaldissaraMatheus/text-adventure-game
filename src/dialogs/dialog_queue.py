from dialogs.dialog import Dialog


class DialogQueue:

    def __init__(self):
        self.queue = []

    def add_dialog(self, dialog: Dialog):
        self.queue.append(dialog)

    def execute(self):
        for dialog in self.queue:
            dialog.execute()
