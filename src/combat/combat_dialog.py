from __future__ import print_function, unicode_literals

from dialogs.dialog_option import DialogOption
from examples import custom_style_1
from PyInquirer import prompt, style_from_dict


class CombatDialog:

    def __init__(self, message):
        self.message = message
        self.options = []

    def add_option(self, dialog_option: DialogOption):
        self.options.append(dialog_option)

    def execute(self):
        optionsCli = []
        for option in self.options:
            option_cli = {'name': option.text}
            optionsCli.append(option_cli)

        questions = [
            {
                'type': 'list',
                'message': self.message,
                'name': 'answers',
                'choices': optionsCli,
            },
        ]

        answer = prompt(questions, style=custom_style_1)['answers']

        return answer
