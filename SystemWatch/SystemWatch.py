#importar los modulos

import tkinter as tk
import psutil
import datetime
import random
from playsound import playsound

#crear y configurar la ventana

wm = tk.Tk()
wm.config(bg='white')
wm.geometry('500x400')
wm.resizable(False, False)

wm.title('SystemWatch')

#obtener temperatura de la cpu

temperatura_cpu_label = tk.Label(wm, font=('Gotham', 16), bg='white')
temperatura_cpu_label.pack()

def obtener_temperatura_cpu():

    temperatura_data = psutil.sensors_temperatures().get('coretemp', [])

    wm.after(5000, obtener_temperatura_cpu)
    for current in temperatura_data:
        return temperatura_cpu_label.config(text=f'La temperatura de la cpu es: {current.current}°C')
obtener_temperatura_cpu()

#obtener el uso de la cpu

obtener_uso_label = tk.Label(wm, font=('Gotham', 17), bg='white')
obtener_uso_label.pack()

def obtener_uso_cpu():
    uso_cpu_data = psutil.cpu_percent()

    wm.after(1000, obtener_uso_cpu)
    obtener_uso_label.config(text=f'La frecuencia  del cpu Es: {uso_cpu_data}%')
obtener_uso_cpu()

#obtener el porcentaje de la bateria

bateria_label = tk.Label(wm, font=('Gotham', 15), bg='white')
bateria_label.pack()

def obtener_porcentaje_bateria():
    bateria_data = psutil.sensors_battery().percent

    wm.after(7000, obtener_porcentaje_bateria)
    bateria_label.config(text=f'La Carga de la bateria es: {bateria_data}%')
obtener_porcentaje_bateria()

#obtener la hora 

hora_label = tk.Label(wm, font=('Gotham', 16), bg='white')
hora_label.pack()

def obtener_hora():
    datetime_data = datetime.datetime.now().time()
    minutos = datetime_data.minute
    hora = datetime_data.hour
    segundo = datetime_data.second

    wm.after(1000, obtener_hora)
    hora_label.config(text=f'La  hora  actual Es: {hora}:{minutos}:{segundo}')
obtener_hora()

#obtener el numero de nucleos de procesador

numero_nucleos_label = tk.Label(wm, font=('Gotham', 15), bg='white')
numero_nucleos_label.pack()

def obtener_numeros_nucleos():
    numero_nucleos_data = psutil.cpu_count()

    numero_nucleos_label.config(text=f'El numero de Nucleos Es: {numero_nucleos_data}')
obtener_numeros_nucleos()

#crear un menu de temas

def temas_ventana():
    temas_wm = tk.Tk()
    temas_wm.title('Temas')
    temas_wm.overrideredirect(True)
    temas_wm.resizable(False, False)

    def cambiar_color(color, color_letra):
        wm.config(bg=color)
        temperatura_cpu_label.config(bg=color, fg=color_letra)
        obtener_uso_label.config(bg=color, fg=color_letra)
        bateria_label.config(bg=color, fg=color_letra)
        hora_label.config(bg=color, fg=color_letra)
        numero_nucleos_label.config(bg=color, fg=color_letra)
        opciones_boton.config(bg=color, fg=color_letra)
        temas_boton.config(bg=color, fg=color_letra)

    rojo = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='red', command=lambda: cambiar_color('red', 'black')).pack()

    amarillo = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='yellow', command=lambda: cambiar_color('yellow', 'black')).pack()

    azul = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='blue', command=lambda: cambiar_color('lightblue', 'black')).pack()

    verde = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='lightgreen', command=lambda: cambiar_color('lightgreen', 'black')).pack()

    marron = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='brown', command=lambda: cambiar_color('brown', 'black')).pack()

    negro = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='black', command=lambda: cambiar_color('black', 'white')).pack()

    purpura = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='purple', command=lambda: cambiar_color('purple', 'black')).pack()

    naranja = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='orange', command=lambda: cambiar_color('orange', 'black')).pack()

    blanco = tk.Button(temas_wm, text='    ', font=('Gotham', 20), bg='white', command=lambda: cambiar_color('white', 'black')).pack()

    quit_tema = tk.Button(temas_wm, text='Cerrar', font=('Gotham', 8),  bg='white', command=temas_wm.destroy).pack()

temas_boton = tk.Button(wm, font=('Gotham', 16), bg='white', text='Temas', command=temas_ventana)
temas_boton.place(y=360, x=401)

#inicio de sonido, imagenes, etc
    
def iniciar_sonido():
    try:
        playsound(random.choice(['Sonidos/Inicio.mp3', 'Sonidos/Inicio 2.mp3']))
        wm.iconphoto(True, tk.PhotoImage(file='Imagenes/Icon.png'))
    except:
        pass
iniciar_sonido()

#crear un bucle/mainloop

wm.mainloop()
#iniciar sonido de salida

try:
    playsound('Sonidos/Salida.mp3')
except:
    pass