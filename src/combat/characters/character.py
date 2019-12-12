from ..items.item import Item
from typing import List

class Character:
    def __init__(self, name: str, health: int, items: List[Item], isFrozen=False): # Talvez o type hint de items como lista não funcione...
        self.name = name
        self.health = health
        self.items = items
        self.isFrozen = isFrozen
    
    def takeDecision(self):
        return #TODO