from .character import Character

class CharacterNPC(Character):
    def __init__(self, name, health, items, isFrozen=False):
        super()
        self.name = super().name
        self.health = super().health
        self.items = super().items
        self.isFrozen = super().isFrozen
    
    def takeDecision(self):
        super()