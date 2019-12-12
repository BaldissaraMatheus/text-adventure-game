from ..items.item import Item
from ..items.espada_item_builder import EspadaItemBuilder
from typing import List

class CobraCharacterBuilder():
    def __init__(self):
        pass
    def build(self):
        espada = EspadaItemBuilder().build()
        return NpcCharacter('Cobra', 10, [espada])