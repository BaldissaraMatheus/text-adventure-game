from .character import Character

class CharacterNPC(Character):
    def __init__(self, name, health, items, isFrozen=False):
        super()
        self.name = name
        self.health = health
        self.items = items
        self.isFrozen = isFrozen
    
    def takeDecision(self):
        super()