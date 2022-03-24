from threading import Thread
from servivo import *

Nombre_Renos = ["Rodolfo","Blitzen","Donder","Cupid","Comet","Vixen","Prancer","Dancer","Dasher"]
Nombre_Duendes = ["Snowball","Bushy","Pepper"]
Despierta = 5

Sem_Santa = threading.Semaphore(0)

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
    print("---> Santa dice: Estoy cansado, dormiré un rato")
    for i in range(Despierta):
        Sem_Santa.acquire() #Santa reposa
        print("----> Santa dice: Estoy despierto!")
    

if __name__ == '__main__':
    main()
