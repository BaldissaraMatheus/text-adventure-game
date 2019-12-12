from interface import implements, Interface
from .item_builder import ItemBuilder
from .item import Item
from .effects.effect_decrease_health import EffectDecreaseHealth

class EspadaItemBuilder(implements(ItemBuilder)):
    def __init__(self):
        pass
    def build(self):
        # return Item('Espada', 'Uma espada sem nada de interessante.', 999, 'Ofensivo', EffectDecreaseHealth(5))
        return ''
