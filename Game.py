#Proyecto 2. Taller de Programacion.
#Kenneth Castillo Herrera 2019062984
#Camilo Jose Solís Gonzales 2019048742
import tkinter as tk
from tkinter import *
import json
from Main import *

#======================================================
class Funciones(object):
    def __init__(self):
        self.creditos

    #   Abre ventana de creditos
    def creditos(self):
        #   caracteristicas de la ventana 
        top = Toplevel() 
        top.title("Creditos")
        top.resizable(width=False,height=False)
        top.geometry("300x300")
        #   convertir el archivo en variable para ponerlo en la ventana
        leer_arch = open('Creditos.txt','r')
        texto = Text(top)
        #   Laprir el arrchivo .txt y ponerlo en la ventana
        texto.insert(END, leer_arch.read())
        texto.pack()
        #   loop
        top.mainloop()

    def Puntaje(self):
        #   caracteristicas de la ventana 
        top = Toplevel() 
        top.title("Puntaje")
        top.geometry("440x500")
        #   convertir el archivo en variable para ponerlo en la ventana
        leer_arch = open('Users.json','r')
        texto = Text(top)
        #   Laprir el arrchivo .txt y ponerlo en la ventana
        texto.insert(END, leer_arch.read())
        texto.pack()
        #   Loop
        top.mainloop()

    def Usuarios(self):
        #   caracteristicas de la ventana 
        top = Toplevel() 
        top.title("Usuarios")
        top.geometry("440x500")
        #   convertir el archivo en variable para ponerlo en la ventana
        leer_arch = open('Users.json','r')
        texto = Text(top)
        #   Laprir el arrchivo .txt y ponerlo en la ventana
        texto.insert(END, leer_arch.read())
        texto.pack()
        #   Loop
        top.mainloop()

#   ====================================================================================

#   ====================================================================================

#para llamar a las funciones
F = Funciones()
#   Clase de Menu en tkinter
class Main_tkinter():
    def __init__(self, master):
        
        ## Create labels, entries, buttons

        #   Pone el menu en la ventana
        master.title("Menu")
        #   Tamaño de la ventena
        master.minsize(700,650)

        label = tk.Label()
        label.place(relwidth=1, relheight=1)

        #Bottones
        button1 = tk.Button(text="Registrar Usuario", font=40, command= F.Usuarios)
        button1.place(relx=0.67,rely=0.50, relheight=0.1, relwidth=0.2)

        button2 = tk.Button(text="Ver Puntaje", font=40, command=F.Puntaje)
        button2.place(relx=0.67,rely=0.65, relheight=0.1, relwidth=0.2)

        button3 = tk.Button(text="Iniciar Partida",fg="green", font=40)
        button3.place(relx=0.13,rely=0.35, relheight=0.1, relwidth=0.2)

        button4 = tk.Button(text="Guardar Partida",fg="blue", font=40, command= F.Usuarios)
        button4.place(relx=0.4,rely=0.35, relheight=0.1, relwidth=0.2)

        button5 = tk.Button(text="Reiniciar Partida", font=40)
        button5.place(relx=0.67,rely=0.35, relheight=0.1, relwidth=0.2)

        button6 = tk.Button(text="Creditos",fg="brown", font=40, command=F.creditos)
        button6.place(relx=0.4,rely=0.85, relheight=0.1, relwidth=0.2)

        button7 = tk.Button(text="Salir", fg="red", font=40, command= quit)
        button7.place(relx=0.67,rely=0.85, relheight=0.1, relwidth=0.2)

        

        entry = Entry(master,bd=2)
        entry.place(relx=0.13,rely=0.50, relheight=0.1, relwidth=0.30)

        #text = Label(text=open("Creditos.txt","r"))0
        #text.place(x=100,y=400)

        label = Label(master, text="Tkinter", fg="red")
        label = Label(master, text="Helvetica", font=("Helvetica", 18))

        #button = tk.Button(text=" About ", font=21, command=winabout).place(x=290,y=600)

        #entry = tk.Entry( font=40)
        #entry.place(relx=0.2,rely=0.25,relheight=0.5, relwidth=0.65)

    def button_click(self):
        pass
        

class Window2:
    def __init__(self, master):
        pass
        

    def button_method(self):
        pass
        

def main(): 
    root = tk.Tk()
    print("True")
    app = Main_tkinter(root)
    root.mainloop()
    

main()

