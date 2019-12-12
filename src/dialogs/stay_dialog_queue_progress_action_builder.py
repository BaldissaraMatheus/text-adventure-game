from .dialog_queue_progress_action_builder import DialogQueueProgressActionBuilder

class StayDialogQueueProgressActionBuilder(DialogQueueProgressActionBuilder):
    def __init__(self):
        super()
    def build(self):
        return BaseAction(self.commands.STAY)
