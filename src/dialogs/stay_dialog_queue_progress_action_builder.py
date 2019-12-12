from .dialog_queue_progress_action_builder import DialogQueueProgressActionBuilder

class StayDialogQueueProgressActionBuilder(DialogQueueProgressActionBuilder):
    def __init__(self, commands):
        super().__init__(commands)
        self.commands = super().commands
    
    def build(self):
        return super().build()