from ..items.item import Item
from typing import List

class Character:
    def __init__(self, name: str, health: int, items: List[Item], isFrozen=False):
        self.name = name
        self.health = health
        self.items = items
        self.isFrozen = isFrozen
    
    def takeDecision(self):
        pass