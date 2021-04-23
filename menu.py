#Elaborado por: XXX
#Fecha de Creación: XX/XX/XXX X:XXpm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: X.X.X

#importanción de librerías
from funciones import *
""""funciones" es el archivo que contiene las funciones principales
a ser llamadas desde este archivo"""

#Definición de funciones
def opcionBisiesto():
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Booleano que indica si el año es bisiesto o no
    """
    print ("\n------------------------\n")
    print ("Prueba del año bisiesto\n")
    annio = int(input("Ingrese un año positivo: "))
    if esBisiesto(annio):# ==True:
        print ("El año es bisiesto.")
    else:
        print ("El año no es bisiesto.")
    return ""
    
def opcionMasCercanos():
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Indicar el número más cercano a 0
    """
    print ("\n------------------------\n")
    print ("Prueba de la recta numérica\n")
    n1 = int(input("Ingrese n1 : "))
    n2 = int(input("Ingrese n2 : "))
    n3 = int(input("Ingrese n3 : "))
    n4 = int(input("Ingrese n4 : "))
    print (masCercanos(n1, n2, n3, n4))
    return ""

def opcionPrimo():  #Llamará a una función recursiva
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Indica el valor booleano si el número es primo o no 
    """
    print ("\n------------------------\n")
    print ("Prueba del número primo\n")
    n = int(input("Ingrese n : "))
    print(str(n) + " es primo? " + str(esPrimo(n)))
    return ""

def opcionPotencia():   #Llamará a una función recursiva
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Texto completo que indica la potencia de un número. 
    """
    print ("\n------------------------\n")
    print ("Prueba de la potencia")
    a = int(input("Ingrese base : "))
    b = int(input("Ingrese exponente : "))
    print (str(a) + " elevando a la " +str(b) + " es " + str(potencia(a,b)))
    return ""
    
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print ("\n**************************\n")
    print ("Práctica de Funciones")
    print ("\n**************************\n")
    print ("1. Año Bisiesto")
    print ("2. Recta Numérica")
    print ("3. Aumento de tarifa de buses")
    print ("4. IMC")
    print ("5. Tabla de multiplicar")
    print ("6. Rango de tablas de multiplicar")
    print ("7. Suma acumulada")
    #Tablas Ml
    #Don Antonio
    print ("0. Terminar")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=7:   #ojo
        if opcion == 1:
            opcionBisiesto()
        elif opcion == 2 :
            opcionMasCercanos()
        elif opcion == 3:
            print ("... en construcción tarifa")
        elif opcion == 4:
            print ("... en construcción Desglose")
        elif opcion == 5:
            print ("... en construcción Horas")
        elif opcion == 6:   #luego se explicará recursividad
            opcionPrimo()    
        elif opcion == 7:   #luego se explicará recursividad
            opcionPotencia()
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu()


#Programa Principal
menu()


