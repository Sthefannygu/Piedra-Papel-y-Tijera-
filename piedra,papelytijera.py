#Creacion de juego 
import random
def iniciar_juego():
    while True:
     print("Hora de jugar Piedra , Papel o Tijera con el Hacker")
     print(" Digita 1 piedra ")
     print(" Digita 2 papel  ")
     print(" Digita 3 tijera ")
     va=input("Escoge una opcion : ")
     mieleccion=int(va)
     if mieleccion ==1:
            print("Tu sacaste  piedra")
     elif mieleccion ==2:
            print("Tu sacaste papel")
     elif mieleccion ==3:
        print("Tu sacaste tijera ")
     else : 
         print("Debes elegir un numero entre 1 y 3")
     elecciondecompu=random.randint(1,3)
     if elecciondecompu ==1:
            print("Hacker saco piedra")
     if elecciondecompu ==2:
            print("Hacker saco papel")
     if elecciondecompu ==3:
            print("Hacker saco tijera ")
     if (mieleccion==1 and elecciondecompu==3) or (mieleccion==2 and elecciondecompu==1) or (mieleccion==3 and elecciondecompu==2):
            print("Ganaste en hora buena")
     if (elecciondecompu==1 and mieleccion==3) or (elecciondecompu==2 and mieleccion==1) or ( elecciondecompu==3 and mieleccion==2):
            print("Perdiste sigue intentando")
     if elecciondecompu == mieleccion:
            print("Obtuvieron un Empate") 
         jugar_de_nuevo= input("Deseas intentarlo otra vez? (si/no):").lower()
     if jugar_de_nuevo == "no": 
         print("ADIOS")
         break
iniciar_juego()
