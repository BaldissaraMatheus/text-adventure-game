from __future__ import print_function, unicode_literals
from PyInquirer import prompt, style_from_dict
from examples import custom_style_1


class Dialog:

    def __init__(self, message):
        self.message = message
        self.options = []

    def add_option(self, dialog_option={'name': 'Continue'}):
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


# dialog_options = {'name': 'foi pra direita'}
# dialog_options2 = {'name': 'foi pra esquerda'}
# primeira_fase = Dialog(message='Para onde eu vou?')
# primeira_fase.add_option()
# primeira_fase.add_option(dialog_options)
# primeira_fase.add_option(dialog_options2)
# resposta = primeira_fase.execute()
# print(resposta)
