from interface import implements, Interface

class EspadaItemBuilder(implements(ItemBuilder)):
    def __init__(self):
        pass
    def build(self):
        return Item('Espada', 'Uma espada sem nada de interessante.' 999, 'Ofensivo', EffectDecreaseHealth(self, 5))
