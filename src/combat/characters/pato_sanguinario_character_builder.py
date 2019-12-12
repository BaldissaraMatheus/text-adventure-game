from ..items.item import Item
from ..items.espada_longa_item_builder import EspadaItemBuilder
from ..items.bomba_magica_item_builder import BombaMagicaItemBuilder
from typing import List

class PatoSanguinarioCharacterBuilder():
    def __init__(self):
        pass
    def build(self):
        espada = EspadaLongaItemBuilder().build()
        bombaMagica = BombaMagicaItemBuilder().build()
        return NpcCharacter('Pato Sanguinário', 15, [espada, bombaMagica])