import information
import requests
import API
import random
import time
from datetime import date
 
hoy_dia = date.today()

#functions
def saludar(name):
     return f"Bot!: ¡ENCANTADO DE PODER SALUUDARTE! {name}" 

def times():
    respuesta = requests.get(API.url_time)
    data = respuesta.json()
    hora = data['hour']
    minuto = data['minute']
    segundo = data['seconds']
    return f"Bot!: Son las {hora:02}:{minuto:02}:{segundo:02}"

def mood():
    respuesta = requests.get(API.url_mod)
    data = respuesta.json()
    frase = data['affirmation']
    return f"Bot!: Hoy me siento {frase}"

def joke():
    respuesta = requests.get(API.url_joke)
    data = respuesta.json()
    
    if data["type"] == "single":
        return f"Bot:!{data['joke']}"
    else:
        return f"Bot:!{data['setup']}"


def motivation():
    respuesta = requests.get(API.url_motivation, timeout=5)

    if respuesta.status_code == 200:
        print(respuesta.text)
        datos = respuesta.json()
        quote = datos.get("quote")
        autor = datos.get("auyor")
        return f'Bot!: "{quote}" - {autor}'       


def day():
    respuesta = requests.get(API.url_day)
    data = respuesta.json()
    day = data['day']
    month = data['month']
    year = data['year']
    return f"Bot:! Hoy es día: {day}/{month}/{year}" 

def despedida(name):
    return f"Bot:! Hasta la próxima {name}"    