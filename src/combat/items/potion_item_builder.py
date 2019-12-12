from interface import implements, Interface

class PotionItemBuilder(implements(ItemBuilder)):
    def __init__(self):
        pass
    def build(self):
        return Item('Poção de vida', 'Suco de manga mágico' 1, 'Defensivo', EffectIncreaseHealth(self, 5))
