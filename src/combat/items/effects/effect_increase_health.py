from interface import implements, Interface
from .effect import Effect

class EffectIncreaseHealth(implements(Effect)):
    def __init__(self, amount: int):
        self.amount = amount
    
    def execute(self, targets):
        for target in targets:
            target.health = target.health + amount