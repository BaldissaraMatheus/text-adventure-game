from interface import implements, Interface
from .action import Action
from .action_decorator import ActionDecorator
from .dialog_queue import DialogQueue

class StartDialogQueueActionDecorator(ActionDecorator):
    def __init__(self, action: Action, queue: DialogQueue):
        super()
        self.action = action
        self.queue = queue
    
    def execute(self):
        self.queue.execute()
        return self.action.execute()