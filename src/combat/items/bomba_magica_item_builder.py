from interface import implements, Interface

class EspadaItemBuilder(implements(ItemBuilder)):
    def __init__(self):
        pass
    def build(self):
        return Item('Bomba mágica', 'Uma bomba congelante.' 999, 'Ofensivo', EffectFreeze(self))
