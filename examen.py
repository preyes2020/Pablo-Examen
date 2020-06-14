from tkinter import ttk
from tkinter import *
import math
import datetime

class Desk:
    def __init__(self, window):
      
        ancho = 500
        alto = 250
        
     
        self.wind = window

        
        self.wind.geometry(str(ancho)+'x'+str(alto))

        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Examen Final')
        

        frame = LabelFrame(self.wind, text = 'Bienvenido')
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 20)      
        
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
       
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, columnspan = 6)

        Label(frame, text = 'Apellido: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, columnspan = 6)

        Label(frame, text = 'Dia: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, columnspan = 6)

        Label(frame, text = 'Mes: ').grid(row = 4, column = 0)
        self.var4 = Entry(frame)
        self.var4.grid(row = 4, columnspan = 6)

        Label(frame, text = 'Año: ').grid(row = 5, column = 0)
        self.var5 = Entry(frame)
        self.var5.grid(row = 5, columnspan = 6)

        
        Button(frame, text = 'Funcion 1', command = self.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'Funcion 2', command = self.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'Funcion 3', command = self.funcion3).grid(row = 6, column = 2 , sticky = W + E)
        Button(frame, text = 'Funcion 4', command = self.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'Funcion 5', command = self.funcion5).grid(row = 6, column = 4 , sticky = W + E)
 


        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    
    def funcion1(self):
        dia=int(self.var3.get())
        mes=int(self.var4.get())
        anio=int(self.var5.get())
        bindia=format(dia, '0b' )
        binmes=format(mes, '0b')
        binanio=format(anio, '0b')
        hexdia=format(dia, '0x')
        hexmes=format(mes, '0x')
        hexanio=format(anio, '0x')

        self.message['text'] = ' {}/{}/{} =  {}/{}/{}'.format(dia,mes,anio,hexdia,hexmes,hexanio)


    def funcion2(self):
            
        dia=int(self.var3.get())
        mes=int(self.var4.get())
        anio=int(self.var5.get())
        fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
        fecha_de_hoy = datetime.datetime.now()
        diferencia = fecha_de_hoy - fecha_de_nacimiento
        dias_vividos = diferencia.days
        horas_vividas = diferencia.days * 24
        minutos_vividos = horas_vividas * 60
        segundos_vividos = minutos_vividos * 60

        self.message['text'] = 'Usted nació el {}/{}/{} y ha vivido {} horas'.format(dia,mes,anio,horas_vividas)

        #self.message['text'] = 'Usted nació {}/{}/{} \n a vivido {} dias \n que equivale: \n en horas {} \n en minutos {} \n en segundos {}'.format(dia,mes,anio,dias_vividos,horas_vividas,minutos_vividos, segundos_vividos)

    def funcion3(self):
        nombre=str(self.var1.get())
        apellido=str(self.var2.get())
        numero_nombre=int(len(nombre))
        numero_apellido=int(len(apellido))
        #if numero_nombre%2==0 and numero_apellido %2==0 :
        #    self.message['text'] = '{} {} su nombre es par y su apellido es par'.format(nombre,apellido)
        #elif numero_nombre%2==0 and numero_apellido %2==1:
        #    self.message['text'] = '{} {} su nombre es par y tu apellido es impar'.format(nombre,apellido)
        #elif numero_nombre%2==1 and numero_apellido %2==0:
        #    self.message['text'] = '{} {} su nombre es impar y tu apellido es par'.format(nombre,apellido)
        #else:
        #   self.message['text'] = '{} {} su nombre es impar y tu apellido es impar'.format(nombre,apellido)


        if numero_nombre%2==0 and numero_apellido %2==0:
            self.message['text'] = '{} {} su nombre junto a su apellido es par'.format(nombre,apellido)
        elif numero_nombre%2==0 and numero_apellido %2==1:
            self.message['text'] = '{} {} su nombre junto a su apellido es impar'.format(nombre,apellido)
        elif numero_nombre%2==1 and numero_apellido %2==0:
            self.message['text'] = '{} {} su nombre junto a su apellido es impar'.format(nombre,apellido)
        else:
            self.message['text'] = '{} {} su nombre junto a su apellido es impar'.format(nombre,apellido)

    def funcion4(self):
        nombre=str(self.var1.get())
        apellido=str(self.var2.get())
        cuenta = 0
        for carac in nombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in apellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        cuntal=len(nombre)
        cuntal1=len(apellido)
        consonante=cuntal+cuntal1-cuenta

        self.message['text'] = '{} {} tienen {} vocales y {} consonantes'.format(nombre, apellido,cuenta,consonante)
     

    def funcion5(self):
        nombre=str(self.var1.get())
        apellido=str(self.var2.get())
        cadena_invertida = ""
        cadena_invertida1= ""
        for letra in nombre:
            cadena_invertida = letra + cadena_invertida
        for letra1 in apellido:
            cadena_invertida1 = letra1 + cadena_invertida1
        self.message['text'] = '{} {} o al revez {} {}'.format(nombre,apellido,cadena_invertida,cadena_invertida1)

    

if __name__ == '__main__':
    
    window = Tk()
    
   
    app = Desk(window)

    
    window.mainloop()
