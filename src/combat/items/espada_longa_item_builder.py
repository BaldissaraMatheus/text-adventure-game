from interface import implements, Interface

class EspadaItemBuilder(implements(ItemBuilder)):
    def __init__(self):
        pass
    def build(self):
        return Item('Espada Longa', 'Uma espada muito braba' 999, 'Ofensivo', EffectDecreaseHealth(self, 10))
