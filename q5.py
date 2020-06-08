class DocumentState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Estado:', self, ' => documento agora está em', state.name)

            self.__class__ = state
        else:
            print('Estado:', self, ' => Trocar para o estado', state.name, 'não é possivel.')

    def __str__(self):
        return self.name


class Draft(DocumentState):
    name = "draft"
    allowed = ['moderation', 'published']


class Moderation(DocumentState):
    """ State of being powered on and working """
    name = "moderation"
    allowed = ['draft', 'published']


class Published(DocumentState):
    """ State of being in suspended mode after switched on """
    name = "published"
    allowed = ['draft']


class Document(object):
    """ A class representing a computer """

    def __init__(self, autor='user'):
        self.autor = autor
        # State of the computer - default is off.
        if self.autor == 'user':
            self.state = Moderation()
        elif self.autor == 'admin':
            self.state = Published()
        else:
            raise ValueError(autor)

    def change(self, state):
        """ Change state """
        self.state.switch(state)


doc = Document("admin")
doc.change(Draft)
doc.change(Moderation)
doc.change(Published)
doc.change(Moderation)
doc.change(Draft)
doc.change(Draft)

