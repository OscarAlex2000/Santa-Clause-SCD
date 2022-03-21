from threading import Thread
from servivo import *


class Main(Thread):

    def __init__(self, lbeing):
        self.__lbeing = lbeing

    def run(self):
        print(self.__lbeing.getName())


def main():
    renos = [Reno("Rodolfo" + str(i)) for i in range(RENOS)]
    duendes = [Duende("Pedro" + str(i)) for i in range(DUENDES)]
    santa = Santa()
    hiloSanta = Main(santa)
    hiloSanta.run()
    print("Que me ves?", renos[0].is_on_vacation, len(duendes), sep=", ")


if __name__ == '__main__':
    main()
