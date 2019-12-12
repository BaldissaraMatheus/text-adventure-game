from dialogs.dialog_queue_progress_action_builder import DialogQueueProgressActionBuilder
from dialogs.dialog_queue_progress_commands import DialogQueueProgressCommands
from dialogs.base_action import BaseAction

class StayDialogQueueProgressActionBuilder(DialogQueueProgressActionBuilder):
    def __init__(self):
        self.commands = DialogQueueProgressCommands()
    def build(self):
        return BaseAction(self.commands.STAY)
