from .character import Character
from ...dialogs.dialog import Dialog

class CharacterPlayer(Character):
    def __init__(self, name, health, items, isFrozen=False):
        super().__init__(name, health, items, isFrozen=isFrozen)
        self.name = super().name
        self.health = super().health
        self.items = super().items
        self.isFrozen = super().isFrozen
    
    def takeDecision(self):
        super().takeDecision() #TODO