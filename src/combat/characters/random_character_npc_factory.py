from .cobra_character_builder import CobraCharacterBuilder
from .ninja_character_builder import NinjaCharacterBuilder
from .pato_sanguinario_character_builder import PatoSanguinarioCharacterBuilder
from random import randrange
from typing import List

class RandomCharacterNpcFactory():
    def __init__(self):
        pass
    def build(self):
        num = randrange(2)
        if (num == 0):
            return CobraCharacterBuilder().build()
        if (num == 1):
            return NinjaCharacterBuilder().build()
        if (num == 2):
            return PatoSanguinarioCharacterBuilder().build()
