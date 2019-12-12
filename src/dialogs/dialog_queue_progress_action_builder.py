from .base_action import BaseAction
from .dialog_queue_progress_commands import DialogQueueProgressCommands

class DialogQueueProgressActionBuilder:
    def __init__(self, commands: DialogQueueProgressCommands):
        self.commands = commands
    
    def build():
        #TODO
        built = BaseAction()
        return built