from typing import List

class combat:
    def __init__(self, enemies: List[CharacterNpc], player: CharacterPlayer):
        self.enemies = enemies
        self.player = player
    
    def execute():
        characters = List[player, enemies]
        size = len(characters)
        top = 0

        while (len(self.enemies) != 0 && self.player.health != 0):
           if (top == size):
               top = 0 

            if (characters[top].isFrozen == True):
                characters[top].isFrozen = False
            else:
                if (characters[top] == self.player):
                    dialog = CombatDialog('Faça sua escolha:')
                    for item in self.player.items:
                        option = DialogOption(item.name + ' - ' + item.description, 'sair')
                        dialog.add_option(option)
                    answer = dialog.execute()
                    # print(answer)
                    for item in self.player.items:
                        optionText = item.name + ' - ' + item.description
                        if (option == answer):
                            if (item.type == 'defensive'):
                                self.player = item.execute(self.player)
                            else:
                                characters[1] = item.execute(characters[1])
                        break
                    # Disparar acao
                else:
                    # Escolhe item aleatório
                    num = randrange(len(characters[top].items) - 1)
                    item = characters[top].items[num]
                    print(characters[top].name + ' usou ' + item.name + '!')
                    if (item.type == 'ofensive'):
                        self.player = item.execute(self.player)
                    else:
                        characters[top] = item.execute(characters[top])
            for char in characters:
                print(char.nome + ' - ' char.health + 'HP')
            for char in characters:
                if (char.health <= 0):
                    if (char == player):
                        break;
                    else:
                        self.characters.remove(char)
            top += 1

                    