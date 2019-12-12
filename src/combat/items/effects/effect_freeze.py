from interface import implements, Interface
from .effect import Effect

class EffectFreeze(implements(Effect)):
    def execute(self, target):
        char = target
        char.isFrozen = True
        return char