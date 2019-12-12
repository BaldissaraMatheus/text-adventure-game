from interface import implements, Interface
from .action import Action

class ActionDecorator(implements(Action)):
    def __init__(self, action: Action):
        self.action = action
    
    def execute(self):
        return self.action.execute()