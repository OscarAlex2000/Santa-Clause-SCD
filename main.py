from threading import Thread
from servivo import *

Nombre_Renos = ["Rodolfo","Blitzen","Donder","Cupid","Comet","Vixen","Prancer","Dancer","Dasher"]
Nombre_Duendes = ["Snowball","Bushy","Pepper"]
Num_Renos = 0
Num_Duendes = 0
Despierta = 5

Sem_Santa = threading.Semaphore(0)
Sem_Duendes = threading.Semaphore(3)
Sem_Renos = threading.Semaphore(0)

class Main(Thread):

    def __init__(self, lbeing):
        self.__lbeing = lbeing

    def run(self):
        print(self.__lbeing.getName())

def santa():
	global Renos
	global Duendes
	global turno
	print("----> Santa dice: Dormiré un rato")
	for i in range(Despierta):
        Sem_Santa.acquire() #Santa reposa
        print("----> Santa dice: Estoy despierto!")
        if Duendes == AyudaDu:
		Duendes = 0
		print("----> Santa dice: ¿Necesitan ayuda?")
		for i in range(AyudaDu):
			print("----> Santa ayuda a {}".format(i + 1))
		Sem_Duendes.release()
		for i in range(AyudaDu)
	elif Num_Renos == Renos:
		Num_Renos = 0
		preparesleigh()
		for i in range(Renos):
			Sem_Renos.release()    

def renos():
	global Num_Renos
	global ren

	num = Num_Renos
	Num_Renos += 1
	print("		{}Aqui!".format(Nombre_Renos[num], ren))
	time.sleep(random.randit(5, 7))

	ren += 1
	if ren == 9:
		print("Los renos despiertan a Santa")
	Sem_Santa.relesase()
	else:
	print("Llegan los renos")
	print("Los renos están listos")

def main():
    renos = [Reno("Rodolfo" + str(i)) for i in range(RENOS)]
    duendes = [Duende("Pedro" + str(i)) for i in range(DUENDES)]
    santa = Santa()
    hiloSanta = Main(santa)
    hiloSanta.run()
    print("Que me ves?", renos[0].is_on_vacation, len(duendes), sep=", ")
    print("---> Santa dice: Estoy cansado, dormiré un rato")
    

if __name__ == '__main__':
    main()
