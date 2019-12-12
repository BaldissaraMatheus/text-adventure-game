from .effects.effect import Effect

class Item:
    def __init__(self, name: str, description: str, quantity: int, item_type: str, target: str, effect: Effect):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.type = item_type
        self.effect = effect
    
    def increase(self, quantity: int):
        self.quantity = self.quantity + quantity
    
    def decrease(self, quantity: int):
        self.quantity = self.quantity - quantity

    def use(self, target: Character):
        self.quantity -= 1
        return self.effect.execute(target)
    
    def readDescription(self):
        print(self.description)
