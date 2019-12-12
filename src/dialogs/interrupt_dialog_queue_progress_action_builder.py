from .dialog_queue_progress_action_builder import DialogQueueProgressActionBuilder

class InterruptDialogQueueProgressActionBuilder(DialogQueueProgressActionBuilder):
    def __init__(self):
        super()
    def build(self):
        return BaseAction(self.commands.INTERRUPT)
