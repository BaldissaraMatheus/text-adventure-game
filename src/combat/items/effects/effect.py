from interface import implements, Interface

class Effect(Interface):
    def execute(self, targets):
        pass