import requests 
import random
import time
from datetime import date 
import information
import functions

hoy_dia = date.today()

name = input('Introduce un nombre:')
contador_preguntas = 0

while True:
    
    message = input('Introduce un mensaje:')
    msg = message.lower()

    if ( msg == "hola"):
       print(functions.saludar(name))

    elif (msg == "que hora es"):
        print(functions.times()) 

    elif (msg == "estado de animo"):
        print(functions.mood())
    
    elif (msg == "cuenta un chiste"):
        print(functions.joke())
    
    elif (msg == "motivacion"):
      print(functions.motivation())

    elif  ( msg == "que dia es hoy"):
       print(functions.day())
    
    elif (msg == "tema"):
        tema = input('Introduce un tema para hablar:').lower()

        match tema:
            case "politica":
                print('Bot:!Encantado estoy de hablar de politica')
                
            case "amor":
                print('Bot:!Encantado estoy de hablar contigo de amor')
                
            case "negocios":
                print('Bot:!Encantado estoy de hablar contigo de negocios')
                
            case "dinero":
                print('Bot:!Encantado estoy de hablar contigo de dinero')
            
            case "salud":
                print('Bot:!Encantado estoy de hablar contigo de salud')
       
    elif (msg == "salir"):
        print(functions.despedida(name)) 
        break
    contador_preguntas += 1
print(f'El número de preguntas es: {contador_preguntas}')  