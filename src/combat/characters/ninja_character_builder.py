from ..items.item import Item
from ..items.espada_item_builder import EspadaItemBuilder
from .character_npc import CharacterNpc
from typing import List

class NinjaCharacterBuilder():
    def __init__(self):
        pass
    def build(self):
        espada = EspadaItemBuilder().build()
        return CharacterNpc('Ninja', 15, [espada])