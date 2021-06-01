class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state



class Singleton(Borg): #Inherigs from the Borg class
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.Update(kwargs)

    def __str__(self):

