from interface import implements, Interface
from dialogs.action import Action

class BaseAction(implements(Action)):
    def __init__(self, command):
        self.command = command
    
    def execute(self):
        return self.command