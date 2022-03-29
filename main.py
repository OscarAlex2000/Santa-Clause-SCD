import threading
import time
import random
from servivo import *

Nombre_Renos = ["Rodolfo","Blitzen","Donder","Cupid","Comet","Vixen","Prancer","Dancer","Dasher"]
Nombre_Duendes = ["Snowball","Bushy","Pepper"]
Num_Renos = 0
ren = 0
Num_Duendes = 0
Duendes = 0
Despierta = 5
Ayuda = 3

Renos = 9
AyudaDu = 3

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
		Prepararegalo()
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
	Sem_Santa.release()
	else:
	print("Llegan los renos")
	print("Los renos están listos")

def duendes():
	global ContDu
	global elfs

	num = ContDu
	ContDu += 1
	print("Los duendes dicen hola")

	for i in range(Ayuda):
		time.sleep(random.radiant(1,5))
		Sem_Duendes.acquire()
		elf = elfs + 1
		elfs += 1
		if elf <= 3:
			print("Necesitamos ayuda!")
			Sem_Santa.release()
		Sem_Duendes.acquire()
		print("Los duendes están siendo ayudados")

def PreparaRegalos():
	print("----> Santa carga los regalos")
	print("----> Hasta la próxima navidad!!")
	print("----> Santa duerme")
	
def main():
    threads = []

	sant = threading.Thread(target=santa)
	threads.append(sant)

	for i in range(Duendes):
		duend = threading.Thread(target=duendes)
		threads.append(duend)

	for i in range(Renos):
		duend = threading.Thread(target=duendes)
		threads.append(Renos)

	for t in threads:
		t.start()

	for t in threads:
		t.join()

	print("La navidad terminó")
    
if __name__ == '__main__':
    	main()
