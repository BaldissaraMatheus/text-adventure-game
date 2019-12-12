from interface import implements, Interface
from .action import Action
from .action_decorator import ActionDecorator
from .dialog_queue import DialogQueue

class StartDialogQueueActionDecorator(ActionDecorator):
    def __init__(self, action: Action, queue: DialogQueue):
        super().__init__(action)
        self.action = super().action
        self.queue = queue
    
    def execute(self):
        return super().execute()