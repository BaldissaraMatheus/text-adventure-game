from .dialog_queue_progress_action_builder import DialogQueueProgressActionBuilder

class StayDialogQueueProgressActionBuilder(DialogQueueProgressActionBuilder):
<<<<<<< HEAD
    def __init__(self):
        super()
    def build(self):
        return BaseAction(self.commands.STAY)
=======
    def __init__(self, commands):
        super().__init__(commands)
        self.commands = super().commands
    
    def build(self):
        return super().build()
>>>>>>> b3e6aa38d5fe9e411de16e8236c6e6fc4d9c0e58
