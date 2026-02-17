import information
import random
import time
from datetime import date
 
hoy_dia = date.today()

#functions
def saludar(name):
     return f"Bot!: ¡ENCANTADO DE PODER SALUUDARTE! {name}" 

def times():
    ahora = time.gmtime()
    return f"Bot:! Son las {ahora.tm_hour}:{ahora.tm_min}:{ahora.tm_sec}"

def mood():
    return f"Bot!: Hoy me siento {random.choice(information.estados_animo)}"

def joke():
    return f"Bot:! El chiste de hoy {random.choice(information.chistes)}"

def motivation():
    return f"Bot:!La frase de motivación de hoy {random.choice(information.frases_motivacion)}"

def day():
    return f"Bot!: Hoy es día: {hoy_dia.day}/{hoy_dia.month}/{hoy_dia.year}"

def despedida(name):
    return f"Bot:! Hasta la próxima {name}"