from interface import implements, Interface
from .action import Action

class BaseAction(implements(Action)):
    def __init__(self, command):
        self.command = command
    
    def execute(self):
        return "alguma string" #TODO