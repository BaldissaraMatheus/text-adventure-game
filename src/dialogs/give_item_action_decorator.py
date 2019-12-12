from interface import implements, Interface
from .action import Action
from .action_decorator import ActionDecorator

class GiveItemActionDecorator(ActionDecorator):
    def __init__(self, action: Action, item: Item):
        super().__init__(action)
        self.action = super().action
        self.item = item
    
    def execute(self):
        return super().execute()