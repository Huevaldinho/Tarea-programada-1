#Elaborado por: Sebastián Bermúdez Acuña y Felipe Obando Arrieta
#Fecha de Creación: XX/XX/XXX X:XXpm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: X.X.X

#importanción de librerías
import sys
sys.setrecursionlimit(5000)
from funciones import *
import re
#Validaciones, entradas y salidas
#Funciones universales
def validarTextoCodificarUniversal(): #esta funcion se puede usar para todos las codificaciones
    aceptados=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    return validarTextoUniversal(aceptados)
def validarTextoUniversal(aceptados):#validación para texto a codificar o decodificar que es universal.
    while True:
        texto=input("Ingrese texto a analizar según las instrucciones de cifrado: ")
        texto=texto.lower()#para también trabajar con letras mayúsculas.
        if texto == "":#si es vacío.
            continue
        elif texto==" ":#si es solo un espacio.
            continue 
        else:
            valido=True #variable para contar si existe algún caracter que no es aceptado(numeros, puntos, etc...)
            for i in range(len(texto)):     #saca cada uno de los caracteres
                if texto[i] in aceptados:       #compara el caracter con la lista de aceptados.
                    continue        #si está bien pasa al siguiente.
                else: 
                    valido=False      #si no está en la lista anota en el contador un 1  para posteriormente saber si hay que ingresar de nuevo el texto.
                    break       #se sale del ciclo for porque ya encontró algo malo.
            if valido==False: #si encontró algo malo lo devuelve al while, a ingresar de nuevo el texto.
                print("\nSu texto no es válido, intente de nuevo.\n")
                continue
            else:
                return texto
#•Murcielago
def murcielago():
    print(30*"•")
    print("\n"+"Código Murciélago".center(30," ")+"\n")
    print(30*"•")
    while True:
        try:
            opcion=int(input("\nIngrese 1 para codificar o 2 para decodificar: "))#obliga a ingresar 1 o 2 por el while try.
            if opcion==1:
                texto=validarTextoCodificarUniversal()#validar el texto a codificar.
                print("\nTexto codificado: \""+codificarMurcielago(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Murciélago-Cod",texto,codificarMurcielago(texto))
                return ""
            elif opcion==2:
                texto=validarTextoDecodificarMurcielago()#validar el texto a decodificar.
                print("\nTexto decodificado: \""+decodificarMurcielago(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Murciélago-Cod",texto,decodificarMurcielago(texto))
                return ""
            else:#numero mayor a 1.
                print("Intente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
            continue
#Validación
def validarTextoDecodificarMurcielago():
    aceptados=["7","b","3","d","5","f","8","h","4","j","k","6","0","n","ñ","9","p","q","2","s","t","1","v","w","x","y","z","*"]
    return validarTextoUniversal(aceptados)
#•Eucalipto
#entrada
def eucalipto():
    print(30*"•")
    print("\n"+"Código Eucalipto".center(30," ")+"\n")
    print(30*"•")
    while True:
        try:
            opcion=int(input("\nIngrese 1 para codificar o 2 para decodificar: "))#obliga a ingresar 1 o 2 por el while try.
            if opcion==1:
                texto=validarTextoCodificarUniversal()#validar el texto a codificar.
                print("\nTexto codificado: \""+codificarEucalipto(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Eucalipto-Cod",texto,codificarEucalipto(texto))
                return ""
            elif opcion==2:
                texto=validarTextoDecodificarEucalipto()#validar el texto a decodificar.
                print("\nTexto decodificado: \""+decodificarEucalipto(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Eucalipto-Cod",texto,decodificarEucalipto(texto))
                return ""
            else:#numero mayor a 1.
                print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
            continue
#validar
def validarTextoDecodificarEucalipto():
    aceptados=["4","b","3","d","1","f","g","h","6","j","k","5","m","n","ñ","9","7","q","r","s","8","2","v","w","x","y","z","°"]
    return validarTextoUniversal(aceptados)
#•Cenit polar
#Entradas/salidas
def cenitPolar():
    """
    Función: Solicitar opciones: codificar o decodificar Cenit Polar.
    Entradas: N/A. Dentro de la función se solicita 1 o 2, para codificar o decodificar
    respectivamente.
    Salidas: N/A. Se muestra el resultado de la codificación/decodificación.
    """
    print(30*"•")
    print("\n"+"Código Cenit Polar".center(30," ")+"\n")
    print(30*"•")
    while True:
        try:
            opcion=int(input("\nIngrese 1 para codificar o 2 para decodificar: "))#obliga a ingresar 1 o 2 por el while try.
            if opcion==1:
                texto=validarTextoCodificarUniversal()#validar el texto a codificar.
                print("\nTexto codificado: \""+codificarCenit(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Cenit Polar-Cod",texto,codificarCenit(texto))
                return ""
            elif opcion==2:
                texto=validarTextoCodificarUniversal()#validar el texto a decodificar.
                print("\nTexto decodificado: \""+decodificarCenit(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Cenit Polar-Cod",texto,decodificarCenit(texto))
                return ""
            else:#numero mayor a 1.
                print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
            continue
#•Código morse.
#Entrada
def iniciarCodigoMorse():
    """
    Función: Iniciar la códificación morse del texto a ingresar.
    Entrada: N/A. Dentro de esta función se solicita un texto, tiene que seguir las intrucciones.
    Salida: N/A.
    """
    print(30*"•")
    print("\n"+"Código Morse".center(30," ")+"\n")
    print(30*"•")
    while True:#ciclo infinito hasta que se ingrese correctamente un texto.
        try:
            opcion=int(input("\nIngrese 1 para codificar o 2 para decodificar: "))#obliga a ingresar 1 o 2 por el while try.
            if opcion==1:
                print("\nHa seleccionado la opción para códificar un texto a código morse.")
                print("\nINSTRUCCIONES:\nEl texto a ingresar debe contener únicamente letras (excepto la \"ñ\"), espacios o números")
                texto=input("\nIngrese texto a codificar: ")
                texto=texto.upper()
                if validarCodigoMorse(texto):#Validar es true, codifique.
                    print("Texto codificado: \""+codificarMorse(texto)+"\"")#guarda el codigo morse.
                    annadirBitacora("Morse-Cod",texto,codificarMorse(texto))
                    return ""
            elif opcion==2:
                print("\nHa seleccionado la opción para decodificar un código morse.")
                print("INSTRUCCIONES:\nEl código morse debe contener únicamente los siguientes caracteres: \".\", \"-\", \"|\", \"^\".\
 Las letras deben llevar el caracter \"^\" entre cada una de ellas, excepto cuando hay un espacio entre medio.\
 Los espacios se representan con el caracter \"|\".")
                texto=input("\nIngrese texto a decodificar: ")
                texto=texto.upper()
                if validarDecodificarMorse(texto):#Validar es true, codifique.
                    print("Texto decodificado: \""+decodificarMorse(texto)+"\"")#guarda el codigo morse.
                    annadirBitacora("Morse-Cod",texto,decodificarMorse(texto))
                    return ""
            else:#numero mayor a 1.
                print("Intente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("Intente de nuevo, según las instrucciones especificadasAAAAA")
            continue
#Validar codificar morse
def validarCodigoMorse(texto):
    """
    Función: Validar que el texto que se haya ingresado en la función iniciarCodigoMorse() cumpla con las restrucciones.
    Entrada:
    -texto(str): Texto que se quiere codificar.
    Salida:
    -True: Si el texto contiene solo letras minusculas, numeros y espacios.
    -False: Si el texto contiene un caracter diferente de letras minusculas, numeros y espacios.
    """
    caracteresValidos=[" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    if texto==" " or not texto:#Si es un espacio o vacío devuelva False.
        print("Debe ingresar texto.")
        return False
    for i in range(len(texto)):
        if texto[0]==" ":
            return False
        if texto[i] in caracteresValidos:
            continue
        else:
            print("\nHa ingresado un caracter invalido.")
            return False
    return True
#Validar decodificación morse.
def validarDecodificarMorse(texto):
    """
    Función: Validar que el código morse que se haya ingresado en la función iniciarCodigoMorse() cumpla con las restrucciones.
    Entrada:
    -texto(str): Texto que se quiere decodificar.
    Salida:
    -True: Si el texto contiene solo código morse.
    -False: Si el texto contiene un caracter diferente al . o - o ^ o |
    """
    caracteresValidos=[".","-","^","|"]
    if texto==" ":#Si es un espacio vacío devuelva False.
        print("\nDebe ingresar el código morse.")
        return False
    if not texto:#Enter vacío.
        print("\nDebe ingresar el código morse.")
        return False
    if texto[0]=="^" or texto[0]=="|" or texto[-1]=="^" or texto[-1]=="|":#el primero y el último no pueden ser estos.
        print("Debe respetar las intrucciones.")
        return False
    for j in range(len(texto)):
        x=texto[j]
        if j==(len(texto)-1):
            y=texto[j]
        else:
            y=texto[j+1]
        if (x=="^" and y=="|") or (y=="^" and x=="|"):
            print('ACAAAA')
            return False
    for i in range(len(texto)):
        if texto[i] in caracteresValidos:
            continue
        else:
            print("Ha ingresado un caracter invalido.")
            return False
    return True
#•Sufamelico
#Entrada
def iniciarSufamelico():
    """
    Función: Iniciar el proceso de codificación/decodificación Sufamelica.
    Entrada: N/A.
    Salida: N/A.
    """
    print(30*"•")
    print("\n"+"Código Sufamélico".center(30," ")+"\n")
    print(30*"•")
    while True:
        try:
            opcion=int(input("\nIngrese 1 para codificar o 2 para decodificar: "))#obliga a ingresar 1 o 2 por el while try.
            if opcion==1:
                texto=validarTextoCodificarUniversal()#validar el texto a codificar.
                texto=texto.upper()
                print("\nTexto codificado: \""+procesarSufamelico(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Sufamélico-Cod",texto,procesarSufamelico(texto))
                return ""
            elif opcion==2:
                texto=validarTextoUniversal()#validar el texto a codificar.
                texto=texto.upper()
                print("\nTexto decodificado: \""+procesarSufamelico(texto)+"\"")#llama la codificación e imprimer el return de la función.
                annadirBitacora("Sufamélico-Cod",texto,procesarSufamelico(texto))
                return ""
            else:#numero mayor a 1.
                print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("\nIntente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
            continue
#menú
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print ("\n"+50*"="+"\n")
    print ("Manual de códigos, claves y señales de pista".center(50," "))
    print ("\n"+50*"="+"\n")
    print ("\n1. Código Murciélago")
    print ("\n2. Código Eucalipto")
    print ("\n3. Código Cenit Polar")
    print ("\n4. Código Morse")
    print ("\n5. Código Sufamelico")
    print ("\n6. Código Deletreo")
    print ("\n0. Terminar")
    while True:
        try:
            opcion = int (input ("\nElija una opción: "))
            break
        except:
            print ("Opción inválida, indique una opción según las opciones indicadas.")
            continue
    if opcion >=0 and opcion <=7:   #ojo
        if opcion == 1:
            murcielago()
        elif opcion == 2 :
            eucalipto()
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
crearBitacora()
menu()