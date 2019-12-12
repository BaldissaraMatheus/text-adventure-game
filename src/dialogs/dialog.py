from __future__ import print_function, unicode_literals

from .dialog_option import DialogOption
from examples import custom_style_1
from PyInquirer import prompt, style_from_dict


class Dialog:

    options = []

    def __init__(self, message):
        self.message = message
        self.options = []

    def add_option(self, dialog_option: DialogOption):
        options.append(dialog_option)

    def print(self):
        print(self.options)

    def execute(self):
        for opt in self.options:
            value_option = {'name': opt.text}
            self.options.append(value_option)

        questions = [
            {
                'type': 'list',
                'message': self.message,
                'name': 'answers',
                'choices': self.options,
            },
        ]

        answers = prompt(questions, style=custom_style_1)
        for opt in self.options:
            if self.message == opt.text:
                opt.execute()
