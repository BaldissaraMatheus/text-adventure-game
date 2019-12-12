from .action import Action


class DialogOption:
    def __init__(self, text: string, action: Action):
        self.text = text
        self.action = action

    def execute(self):
        return self.action.execute()
