from interface import implements, Interface

class IState(Interface):
    def update(self):
        pass
    def on_enter(self):
        pass
    def on_exit(self):
        pass

class StateStack:
    def __init__(self):
        self.states = { # Construtores de classe
                'dialog' : StartDialogueQueueActionDecorator,
                'combat' : CombatMainBlaBlaBla
            }
        self.stack = []
    
    def update(self):
        top = stack[-1]
        top.update()

    def push(self, state: string):
        stack += states[state]()

    def pop(self):
        top = stack[-1]
        del stack[-1]
        return top
    