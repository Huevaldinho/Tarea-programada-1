#Importación
import re

#Entradas/salidas
def cenitPolar():
    """
    Función: Solicitar opciones: codificar o decodificar Cenit Polar.
    Entradas: N/A. Dentro de la función se solicita 1 o 2, para codificar o decodificar
    respectivamente.
    Salidas: N/A. Se muestra el resultado de la codificación/decodificación.
    """
    print("........................")
    print("\nCenit Polar\n")
    print("........................")
    while True:#Obliga ingresar 1 o 2.
        try:
            opcion=int(input("Ingrese 1 para codificar o 2 para decodificar: "))#obliga a ingresar 1 o 2 por el while try.
            if opcion==1:
                texto=validarTextoCodificar()#validar el texto a codificar.
                print("Texto codificado: "+codificarCenit(texto))#llama la codificación e imprimer el return de la función.
                return ""
            elif opcion==2:
                texto=validarTextoDecodificar()#validar el texto a decodificar.
                print("Texto decodificado: "+decodificarCenit(texto))#llama la codificación e imprimer el return de la función.
                return ""
            else:#numero mayor a 1.
                print("Intente de nuevo,Digite 1. Codificar. o 2. Decodificar.")
        except:#cualquier caracter diferente de numero.
            print("Intente de nuevo, Digite 1. Codificar. o 2. Decodificar.")
            continue
#Validaciones
def validarTextoCodificar():#validación para texto a codificar.
    """
    Función: Validar que el texto que se solicita cumpla con las restrucciones.(Sólo acepta
    letras, comas y espacios. NO acepta numeros o cualquier otro caracter.)Hasta que no se
    ingrese de manera correcta el texto no se sale de la función.
    Entrada: N/A. Se solicita un texto dentro de la función.
    Salida:
    -texto(str): Texto ingresado, este si cumple con las restrucciones.
    """
    while True:
        texto=input("Ingrese texto a codificar(solo letras, espacios, comas. No se aceptan tildes.):")
        texto.lower()#para también trabajar con letras mayúsculas.
        aceptados=["a","b","c","d","e","f","g","h","i","j","k","l","m","n\
","ñ","o","p","q","r","s","t","u","v","w","x","y","z",","," "]#Lista de caracteres permitidos.
        if texto == "":#si es vacío.
            continue
        elif texto==" ":#si es solo un espacio.
            continue 
        else:
            algo=0#varaible para contar si existe algún caracter que no es aceptado(numeros, puntos, etc...)
            for i in range(len(texto)):#saca cada uno de los caracteres
                if texto[i] in aceptados:#compara el caracter con la lista de aceptados.
                    continue#si está bien pasa al siguiente.
                else:#si no está en la lista anota en el contador un 1  para posteriormente saber si hay que ingresar de nuevo el texto.
                    algo=1#algún caracter no permitido.
                    break#se sale del ciclo for porque ya encontró algo malo.
            if algo>=1:#si encontró algo malo lo devuelve al while, a ingresar de nuevo el texto.
                continue
            else:#todo lo ingresado está en la lista de aceptados.(letras minusculas o ¬.)
                return texto#devuelve el texto para procesarlo.
def validarTextoDecodificar():#validación para texto a decodificar.
    """
    Función: Validar que el texto que se solicita cumpla con las restrucciones. Hasta que no se
    ingrese de manera correcta el texto no se sale de la función.
    Entradas: N/A. Dentro de la función se solicita un texto (Solo acepta letras y el caracter ¬).
    Salidas:
    -texto(str): Texto ingresado, este si cumple con las restricciones.
    """
    while True:
        texto=input("Ingrese texto a decodificar(solo letras o el caracter ¬. No se aceptan tildes):")
        texto.lower()
        aceptados=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","¬"]
        if texto == "":#si es vacío.
            continue
        elif texto==" ":#si es solo un espacio.
            continue 
        else:
            algo=0#varaible para contar si existe algún caracter que no es aceptado(numeros, espacios,puntos, etc...)
            for i in range(len(texto)):#saca cada uno de los caracteres
                if texto[i] in aceptados:#compara el caracter con la lista de aceptados.
                    continue#si está bien pasa al siguiente.
                else:#si no está en la lista anota en el contador un 1  para posteriormente saber si hay que ingresar de nuevo el texto.
                    algo=1#algún caracter no permitido.
                    break#se sale del ciclo for porque ya encontró algo malo.
            if algo>=1:#si encontró algo malo lo devuelve al while, a ingresar de nuevo el texto.
                continue
            else:#todo lo ingresado está en la lista de aceptados.(letras minusculas, espacios y coma.)
                return texto#devuelve el texto para procesarlo.
#Procesos
def codificarCenit(texto):
    """
    Función: Codificar el texto en cenit polar.
    Entrada:
    -texto(str): Texto validado, debe ser letras (sin tilde y minúsculas)
,espacios y comas.
    Salida:
    -codificado(str): Texto codificado en cenit polar.
    """
    codificado=""#variable en blanco para guardar los cambios.
    for i in range(len(texto)):
        if texto[i]=="c":
            codificado+="p"
        elif texto[i]=="e":
            codificado+="o"
        elif texto[i]=="n":
            codificado+="l"
        elif texto[i]=="i":
            codificado+="a"
        elif texto[i]=="t":
            codificado+="r"
        elif texto[i]=="p":
            codificado+="c"
        elif texto[i]=="o":
            codificado+="e"
        elif texto[i]=="l":
            codificado+="n"
        elif texto[i]=="a":
            codificado+="i"
        elif texto[i]=="r":
            codificado+="t"
        elif texto[i]==" ":#espacio.
            codificado+="¬"
        elif texto[i]==",":#quita la coma.
            continue
        else:
            codificado+=texto[i]#otras letras que no se tienen que cambiar.
    return codificado
def decodificarCenit(texto):
    """Función: Decodificar el texto codificado en cenit polar.
    Entrada:
    -texto(str): Texto validado, debe ser letras (sin tilde y minúsculas) y el caracter ¬.
    Salida:
    -decodificado(str): Texto decodificado en cenit polar.
    """
    decodificado=""#variable en blanco para guardar los cambios.
    for i in range(len(texto)):
        if texto[i]=="c":
            decodificado+="p"
        elif texto[i]=="e":
            decodificado+="o"
        elif texto[i]=="n":
            decodificado+="l"
        elif texto[i]=="i":
            decodificado+="a"
        elif texto[i]=="t":
            decodificado+="r"
        elif texto[i]=="p":
            decodificado+="c"
        elif texto[i]=="o":
            decodificado+="e"
        elif texto[i]=="l":
            decodificado+="n"
        elif texto[i]=="a":
            decodificado+="i"
        elif texto[i]=="r":
            decodificado+="t"
        elif texto[i]=="¬":
            decodificado+=" "
        else:
            decodificado+=texto[i]#otras letras que no se tienen que cambiar.
    return decodificado
cenitPolar()