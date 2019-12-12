from interface import implements, Interface
from .item_builder import ItemBuilder

class BombaMagicaItemBuilder(implements(ItemBuilder)):
    def __init__(self):
        pass
    def build(self):
        return Item('Bomba mágica', 'Uma bomba congelante.', 4, 'Ofensivo', EffectFreeze(self))
