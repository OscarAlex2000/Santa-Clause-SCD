# Flores Sanchez Oscar Alexis
# Morones Hernandez David
# Ramirez Uriel

# Librerias 
from cmath import e
import threading
import time
import random
from servivo import *

# Semaforos
Sem_Santa = threading.Semaphore(0) # Santa semaforo
Sem_DuendesM = threading.Semaphore(3) # Elfos piden ayuda (3) semaforo
Sem_Duendes = threading.Semaphore(0) # Elfos ayudados
Sem_Renos = threading.Semaphore(0) # Reno semaforo

# Variables 
Num_Renos = 0 # Variable para contabilizar el número de renos que ha llegado
ren = 0 # Variable que contabiliza el numero total de renos para implementar el orden correcto de los print's
Num_Duendes = 0 # Variable para contabilizar el número de elfos que ha llegado
Duendes = 0 # Variable que contabiliza el trio de elos con problemas
turno = 1 # Variable que contabiliza los turnos de preguntas

# Constantes
Despierta = 7 # Numero de veces que Santa despierta
Ayuda = 3 # Numero de veces que los elfos piden ayuda
Renos = 9 # Numero total de renos
Elfos = 9 # Numero total de elfos
AyudaDu = 3 # Numero de elfos ayudados

Nombre_Renos = ["Rodolfo","Blitzen","Donder","Cupid","Comet","Vixen","Prancer","Dancer","Dasher"]
Nombre_Duendes = ["Snowball","Bushy","Pepper"]

class Main(Thread):

    def __init__(self, lbeing):
        self.__lbeing = lbeing

    def run(self):
        print(self.__lbeing.getName())

# Definición del proceso Santa: Santa duerme y lo despertarán cuando hallan llegado 3 duendes o 9 renos.
# Si 3 elfos piden ayuda, Santa les ayudará, liberará otros 3 duendes que pidan ayuda
# y despues liberará los 3 duendes ayudados. Si los 9 renos despiertan a Santa, Santa preparará el trineo
# y los liberará. Santa se despierta 7 veces, 1 por los renos y 6 por los duendes
def santa():
	global Renos
	global Duendes
	global turno
	print("----> Santa dice: Estoy cansado")
	print("----> Santa dice: Dormiré un rato")
	for i in range(Despierta):
		Sem_Santa.acquire() # Santa espera
		print("----> Santa dice: Estoy despierto!")
		if Duendes == AyudaDu:
			Duendes = 0
			print("----> Santa dice: ¿Necesitan ayuda?")
			for i in range(AyudaDu):
				print("----> Santa ayuda a {}".format(i + 1))
				Sem_Duendes.release() # Desbloqueas para la llegada de los 3 duendes
			print("----> Santa termina de ayudar a {}".format(i + 1))
			turno += 1
			for i in range(AyudaDu):
				Sem_Duendes.release()
		elif Num_Renos == Renos:
			Num_Renos = 0
			PreparaRegalos()
			for i in range(Renos):
				Sem_Renos.release()    

# Definicion del proceso de los renos: los renos van llegando y se van desbloqueando
# Cuando llegan los 9 renos despiertan a Santa
# Después Santa los prepara y los ata al trineo solo una vez, y los libera
def renos():
	global Num_Renos
	global ren

	num = Num_Renos
	Num_Renos += 1
	print("{}Aqui!".format(Nombre_Renos[num], ren))
	time.sleep(random.randit(5, 7))

	ren += 1
	if ren == 9:
		print("Los renos despiertan a Santa!!")
		print("Los renos {}, Yo soy ".format(Nombre_Renos[num], ren))
		Sem_Santa.release() # Santa se despierta
	else:
		print("Llega el reno ".format(Nombre_Renos[num]))
		Sem_Renos.acquire()
		print("{} Listo y atado".format(Nombre_Renos[num]))
		print("Ultimo reno {}".format(Nombre_Renos[num]))

# Definición del proceso de los duendes: Como se puede apreciar los elfos van llegando y pedirán ayuda dos veces cada uno.
# Una vez llegando 3 elfos, los siguientes que llegaran seran bloqueados, hasta que Santa los liberé
# Solo cuando 3 elfos pidan ayuda Santa se despertará
# Los 3 elfos que piden ayuda estaran bloqueados, hata que Santa los ayude y los liberé
# Cuando los elfos hayan sido ayudados 2 veces acabaran
def duendes():
	global Elfos
	global Num_Duendes

	num = Elfos
	Elfos += 1
	print("Hola, soy el duende {}".format(Nombre_Duendes[num]))

	for i in range(Ayuda):
		time.sleep(random.radiant(1,5))
		Sem_Duendes.acquire() # Deja pasar 3 duendes
		elf = Num_Duendes + 1
		Num_Duendes += 1
		if elf <= 3:
			print("El elfo {} dice: Tengo una pregunta. Estoy esperando".format(Nombre_Duendes[num], elf))
		elif elf == AyudaDu:
			print("El elfo {} dice: Tengo una pregunta. SAAANTAAAA!".format(Nombre_Duendes[num], elf))
			Sem_Santa.release()
		Sem_Duendes.acquire()
		print("El elfo {} esta siendo ayudado!".format(Nombre_Duendes[num]))
	print("El elfo {} termina".format(Nombre_Duendes[num]))

# Santa prepara el trineo y se va a dormir
def PreparaRegalos():
	print("----> Santa dice: ¿Están listos los juguetes? ")
	print("----> Santa carga los regalos")
	print("----> Santa dice: Hasta la próxima navidad!!")
	print("----> Santa duerme")
	
# Main
def main():

	# Array de hilos
    threads = []

	# Santa
	sant = threading.Thread(target=santa)
	threads.append(sant)

	# Elfos
	for i in range(Duendes):
		duend = threading.Thread(target=duendes)
		threads.append(duend)

	# Renos
	for i in range(Renos):
		rens = threading.Thread(target=duendes)
		threads.append(rens)

	# Iniciamos todos los hilos
	for t in threads:
		t.start()

	# Esperamos a que se completen todos los hilos
	for t in threads:
		t.join()

	print("La navidad terminó")

if __name__ == '__main__':
	main()


