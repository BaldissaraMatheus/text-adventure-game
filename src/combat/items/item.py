from .effects.effect import Effect

class Item:
    def __init__(self, name: str, description: str, quantity: int, item_type: str, target: str, effect: Effect):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.item_type = item_type
        self.target = target
        self.effect = effect
    
    def increase(self, quantity: int):
        self.quantity = self.quantity + quantity
        if self.quantity <= 0:
            #TODO: remove from inventory
            pass
    
    def use(self, character: Character): #ideia: (self, user: Character, targets)
        #TODO
        return
