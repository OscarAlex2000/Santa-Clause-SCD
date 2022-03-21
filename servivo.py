'''Modulo con las clases de santa, reno y duende'''
RENOS = 9
DUENDES = 3


class __LivingBeing:
    def __init__(self, name):
        self.__lname = name

    def getName(self):
        return self.__lname


class Santa(__LivingBeing):
    is_sleeping = True

    def __init__(self):
        super().__init__("Santa Claus")


class Reno(__LivingBeing):
    is_on_vacation = True

    def __init__(self, name):
        super().__init__(name)


class Duende(__LivingBeing):
    def __init__(self, name):
        super().__init__(name)
