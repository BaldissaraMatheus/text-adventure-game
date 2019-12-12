from interface import implements, Interface
from .effect import Effect

class EffectIncreaseHealth(implements(Effect)):
    def execute(self, targets):
        for target in targets:
            target.isFrozen = True