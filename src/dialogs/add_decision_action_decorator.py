from interface import implements, Interface
from .action import Action
from .action_decorator import ActionDecorator

class AddDecisionActionDecorator(ActionDecorator):
    def __init__(self, action: Action, decision: Decision):
        super().__init__(action)
        self.action = super().action
        self.decision = decision
    
    def execute(self):
        return super().execute()
    
