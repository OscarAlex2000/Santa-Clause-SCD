#create window tkinder
from tkinter import *

from concurrent.futures import ThreadPoolExecutor

class Santa:
    def __init__(self):
        self.duende = ThreadPoolExecutor()
        self.reno = ThreadPoolExecutor()
        self.numD = 0
        self.numR = 0

    def getD(self):
        return str(self.numD)
    
    def getR(self):
        return str(self.numR)

    def Duende(self):
        self.numD = 0
        self.cambioDuende()
        
    def Renos(self):
        print("daadas")
        self.numR = 0
        self.cambioReno()

    def crear_Duende(self):
        #actualizar raiz
        
        if self.numD < 2:
            self.numD += 1
            D.set("Duendes: "+str(self.numD))
        elif self.numD == 2:
            self.duende.submit(self.Duende)
            D.set("Duendes: 0")
    
    def crear_Renos(self):
        if self.numR < 4:
            self.numR += 1
            R.set("Renos: "+str(self.numR))
        elif self.numR == 4:
            self.duende.submit(self.Renos)
            R.set("Renos: 0")
    
    def cambioDuende(self):
        raiz.state(newstate = "withdraw")
        duendeV.state(newstate = "normal")
        duendeV.after(10000, san.retornoD)
    
    def cambioReno(self):
        raiz.state(newstate = "withdraw")
        renosV.state(newstate = "normal")
        renosV.after(10000, san.retornoR)

    def retornoD(self):
        raiz.state(newstate = "normal")
        duendeV.state(newstate = "withdraw")
    
    def retornoR(self):
        raiz.state(newstate = "normal")
        renosV.state(newstate = "withdraw")

#def update(ind):
#    """ Actualiza la imagen gif """
#    frame = frames[ind]
#    ind += 1
#    if ind == framesNum:
#        ind = 0
#    label.configure(image=frame)
#    raiz.after(200, update, ind) # Numero que regula la velocidad del gif

if __name__ == "__main__":
    # Crear ventana
    san = Santa()
    #create window
    raiz = Tk()
    #framesNum = 30 # Numero de frames que tiene el gif
    #archivo = "santa_dormido.gif"
    
    # Lista de todas las imagenes del gif
    #frames = [PhotoImage(file=archivo, format='gif -index %i' %(i)) for i in range(framesNum)]
    #label = Label(raiz)
    #label.pack()
    #raiz.after(27, update, 29)
    raiz.title("Papa noel")
    raiz.state(newstate = "normal")
    raiz.geometry("576x500")
    #agregar imagen
    imagen = PhotoImage(file="santa_dormido.gif")
    #agregar label
    Label(raiz, image=imagen).place(x=0, y=0)
    #agregar boton
    boton = Button(raiz, text="Salir", command=raiz.quit)
    boton.place(x=0, y=450)
    #agregar boton con proceso
    boton2 = Button(raiz, text="Crear duende", command=san.crear_Duende)
    boton2.place(x=300, y=400)
    boton3 = Button(raiz, text="Crear Reno", command=san.crear_Renos)
    boton3.place(x=300, y=440)
    #agregar boton con evento
    D = StringVar()
    R = StringVar()
    D.set("Duendes: 0")
    R.set("Renos: 0")
    #crear label con texto
    Label(raiz, textvariable=D).place(x=100, y=450)
    Label(raiz, textvariable=R).place(x=100, y=470)

    duendeV = Toplevel()
    duendeV.title("Duendes")
    duendeV.state(newstate = "withdraw")
    duendeV.geometry("400x400")
    #agregar imagen
    imagenV1 = PhotoImage(file="santayduendes.gif", format="gif -index 0")

    #agregar label
    Label(duendeV, image=imagenV1).place(x=0, y=0)
    
    renosV = Toplevel()
    renosV.title("Renos")
    renosV.state(newstate = "withdraw")
    renosV.geometry("400x200")
    #agregar imagen
    imagenV = PhotoImage(file="santarenos.gif")
    #agregar label
    Label(renosV, image=imagenV).place(x=0, y=0)
    
    duendeV.mainloop()
    renosV.mainloop()
    #mainloop
    raiz.mainloop()

    