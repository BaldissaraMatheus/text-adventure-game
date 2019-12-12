from interface import implements, Interface
from .effect import Effect

class EffectDecreaseHealth(implements(Effect)):
    def __init__(self, amount: int):
        self.amount = amount
    
    def execute(self, target):
        char = target
        char.health = char.health - amount
        return char