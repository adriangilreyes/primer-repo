import requests 
import random
import time
from datetime import date 


hoy_dia = date.today()

estados_animo = ["Alegre","Entusiasmado","Motivado","Optimista","Inspirado","Energético",
                           "Agradecido","Orgulloso","Tranquilo","Confiado",
"Relajado","Concentrado","Pensativo","Curioso","Indiferente",
                             "Sereno","Reflexivo","Calmado","Cansado",
"Dramatico","Sarcastico","Rebelde","Misterioso","Filosofico",
                             "Existencial","Caotico","Creativo","Burlon","Inspirado por el cafe"]

chistes = [
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
    "¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!",
    "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!",
    "¿Qué hace una vaca cuando sale el sol? Sombra.",
    "¿Cuál es el colmo de Aladdín? Tener mal genio.",
    "¿Por qué el libro de matemáticas estaba triste? ¡Porque tenía muchos problemas!",
    "¿Qué le dice un semáforo a otro? No me mires, me estoy cambiando.",
    "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
    "¿Qué le dijo un jardinero a otro? ¡Disfruta mientras puedas, que la primavera la sangre altera!",
    "¿Cómo organizan los gatos su fiesta? ¡Miau-sica, miau-comida y miau-diversión!",
    "¿Qué hace una computadora cuando tiene hambre? ¡Se come un byte!",
    "¿Qué le dice un zapato a otro? ¡Nos vemos en el camino!",
    "¿Cuál es el colmo de un electricista? Que le dé miedo la oscuridad.",
    "¿Qué hace un pez? ¡Nada!"
]

frases_motivacion = [
    "No sueñes tu vida, vive tu sueño.",
    "El éxito no es para los que piensan que pueden, sino para los que actúan.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "No te rindas, el principio siempre es lo más difícil",
    "Cree en ti y todo será posible.",
    "El único límite eres tú mismo.",
    "Haz hoy lo que otros no hacen para lograr mañana lo que otros no logran.",
    "La perseverancia convierte lo imposible en posible.",
    "No cuentes los días, haz que los días cuenten.",
    "El fracaso es solo la oportunidad de empezar de nuevo con más experiencia.",
    "Si quieres algo que nunca tuviste, debes hacer algo que nunca hiciste.",
    "El éxito se construye con pequeños pasos constantes.",
    "Sé fuerte, sé valiente, sé tú.",
    "No importa lo lento que vayas, lo importante es no detenerte.",
    "Hoy es el primer día del resto de tu vida"
]

name = input('Introduce un nombre:')
contador_preguntas = 0

while True:
    
    message = input('Introduce un mensaje:')
    msg = message.lower()

    if ( msg == "hola"):
        print(f"Bot!: ¡ENCANTADO DE PODER SALUUDARTE! {name}")

    elif (msg == "que hora es"):
        ahora = time.gmtime()
        print(f'Bot:! Son las {ahora.tm_hour}:{ahora.tm_min}:{ahora.tm_sec}')

    elif (msg == "estado de animo"):
        print(f'Bot!: Hoy me siento {random.choice(estados_animo)}')
    
    elif (msg == "cuenta un chiste"):
        print(f'Bot:! El chiste de hoy {random.choice(chistes)}')
    
    elif (msg == "motivacion"):
        print(f'Bot:!La frase de motivación de hoy {random.choice(frases_motivacion)}')

    elif  ( msg == "que dia es hoy"):
        print(f"Bot!: Hoy es día: {hoy_dia.day}/{hoy_dia.month}/{hoy_dia.year}")
    
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
        print(f'Bot:! Hasta la próxima {name}')
        break

    contador_preguntas += 1
print(f'El número de preguntas {contador_preguntas}') 