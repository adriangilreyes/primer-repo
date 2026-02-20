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

    match message:
        case "hola":
            print(functions.saludar(name))

        case "que hora es":
            print(functions.times())
        
        case "estado de animo":
            print(functions.mood())
        
        case "cuenta un chiste":
            print(functions.joke())

        case "motivacion":
            print(functions.motivation())
        
        case "que dia es hoy":
            print(functions.day())
    
        case "tema":
           tema = input('Introduce un tema para hablar:').strip().lower()
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
                
                case "ia":
                    print('Bot:!Estoy encantado de hablar contigo de  IA') 
                
                case _:
                   print('Bot:! No conozco ese tema')
            
        case "salir":
            print(functions.despedida(name)) 
            break

        case _:
            print('Bot:!No entiendo tu mensaje')    

    contador_preguntas += 1
print(f'El número de preguntas es: {contador_preguntas}')      