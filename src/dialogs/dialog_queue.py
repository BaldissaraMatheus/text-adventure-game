from dialogs.dialog import Dialog
from dialogs.dialog_queue_progress_commands import DialogQueueProgressCommands

class DialogQueue:

    def __init__(self):
        self.queue = []
        self.commands = DialogQueueProgressCommands()

    def add_dialog(self, dialog: Dialog):
        self.queue.append(dialog)

    def execute(self):
        while (len(self.queue) != 0):
            command = self.queue[0].execute()
            if (command == self.commands.INTERRUPT):
                self.queue = []
            elif (command == self.commands.CONTINUE):
                self.queue.remove(self.queue[0])

