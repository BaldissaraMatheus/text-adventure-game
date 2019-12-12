from __future__ import print_function, unicode_literals
from PyInquirer import prompt, style_from_dict, Token, Separator
from examples import custom_style_1


class Dialog:

    def __init__(self, message):
        self.message = message
        self.options = [{'name': 'Continue'}]

    def add_option(self, dialog_option):
        self.options.append(dialog_option)

    def execute(self):
        questions = [
            {
                'type': 'list',
                'message': self.message,
                'name': 'answers',
                'choices': self.options,
            },
        ]

        answers = prompt(questions, style=custom_style_1)
        return answers


dialog_options = {'name': 'foi pra direita'}

primeira_fase = Dialog(message='Para onde eu vou?')
primeira_fase.add_option(dialog_options)
primeira_fase.execute()


# message = 'Para onde eu vou?'

# dialog_options = [
#     {'name': 'foi pra direita'},
#     {'name': 'foi pra esquerda'},
#     {'name': 'foi pra cima'},
# ]

# questions = [
#     {
#         'type': 'list',
#         'message': message,
#         'name': 'answers',
#         'choices': dialog_options,
#     },
# ]

# print('Agora vamos pro seguinte: \n')
# answers = prompt(questions, style=custom_style_1)
