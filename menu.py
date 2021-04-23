#Elaborado por: XXX
#Fecha de Creación: XX/XX/XXX X:XXpm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: X.X.X

#importanción de librerías
from TP1 import *
#menú
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print ("\n**************************\n")
    print ("TAREA PROGRAMADA 1")
    print ("\n**************************\n")
    print ("1. Murciélago")
    print ("2. Eucalipto")
    print ("3. Cenit Polar")
    print ("4. Morse")
    print ("5. Sufamelico")
    print ("6. Deletreo")
    print ("0. Terminar")
    while True:
        try:
            opcion = int (input ("Escoja una opción: "))
            break
        except:
            print("Debe ingresar una opión")
            continue
    if opcion >=0 and opcion <=7:   #ojo
        if opcion == 1:
            eucalipto()
        elif opcion == 2 :
            murcielago()
        elif opcion == 3:
            cenitPolar()
        elif opcion == 4:
            iniciarCodigoMorse()
        elif opcion == 5:
            iniciarSufamelico() 
        elif opcion == 6:   #luego se explicará recursividad
            pass#falta la última
        else:#0 cerrar.
            return ""
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu()
#Programa Principal
menu()