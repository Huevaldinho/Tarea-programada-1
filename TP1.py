#Elaborado por: Sebastián Bermúdez Acuña y Felipe Obando Arrieta
#Fecha de Creación: 12/04/21 7:43 PM
#Fecha de última Modificación: XX/XX/XX X:XXpm 
#Versión: 3.9.2

#Importación
import re
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
                return texto
#Murcielago
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
                return ""
            elif opcion==2:
                texto=validarTextoDecodificarMurcielago()#validar el texto a decodificar.
                print("\nTexto decodificado: \""+decodificarMurcielago(texto)+"\"")#llama la codificación e imprimer el return de la función.
                return ""
            else:#numero mayor a 1.
                print("Intente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("Intente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
            continue
#Validación
def validarTextoDecodificarMurcielago():
    aceptados=["7","b","3","d","5","f","8","h","4","j","k","6","0","n","ñ","9","p","q","2","s","t","1","v","w","x","y","z","*"]
    return validarTextoUniversal(aceptados)
#Proceso
def codificarMurcielago(texto):
    codificado=""#variable en blanco para guardar los cambios.
    for i in range(len(texto)):
        if texto[i]=="m":
            codificado+="0"
        elif texto[i]=="u":
            codificado+="1"
        elif texto[i]=="r":
            codificado+="2"
        elif texto[i]=="c":
            codificado+="3"
        elif texto[i]=="i":
            codificado+="4"
        elif texto[i]=="e":
            codificado+="5"
        elif texto[i]=="l":
            codificado+="6"
        elif texto[i]=="a":
            codificado+="7"
        elif texto[i]=="g":
            codificado+="8"
        elif texto[i]=="o":
            codificado+="9"
        elif texto[i]==" ":#espacio.
            codificado+="*"
        else:
            codificado+=texto[i]#otras letras que no se tienen que cambiar.
    return codificado.upper()
def decodificarMurcielago(texto):
    codificado=""#variable en blanco para guardar los cambios.
    for i in range(len(texto)):
        if texto[i]=="0":
            codificado+="m"
        elif texto[i]=="1":
            codificado+="u"
        elif texto[i]=="2":
            codificado+="r"
        elif texto[i]=="3":
            codificado+="c"
        elif texto[i]=="4":
            codificado+="i"
        elif texto[i]=="5":
            codificado+="e"
        elif texto[i]=="6":
            codificado+="l"
        elif texto[i]=="7":
            codificado+="a"
        elif texto[i]=="8":
            codificado+="g"
        elif texto[i]=="9":
            codificado+="o"
        elif texto[i]=="*":#espacio.
            codificado+=" "
        else:
            codificado+=texto[i]#otras letras que no se tienen que cambiar.
    return codificado.upper()
#Eucalipto
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
                return ""
            elif opcion==2:
                texto=validarTextoDecodificarEucalipto()#validar el texto a decodificar.
                print("\nTexto decodificado: \""+decodificarEucalipto(texto)+"\"")#llama la codificación e imprimer el return de la función.
                return ""
            else:#numero mayor a 1.
                print("Intente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
                continue
        except:#cualquier caracter diferente de numero.
            print("Intente de nuevo, según las instrucciones especificadas.\n1. Codificar.\n2. Decodificar.")
            continue
#validar
def validarTextoDecodificarEucalipto():
    aceptados=["4","b","3","d","1","f","g","h","6","j","k","5","m","n","ñ","9","7","q","r","s","8","2","v","w","x","y","z","°"]
    return validarTextoUniversal(aceptados)
#proceso
def codificarEucalipto(texto):
    codificado=""#variable en blanco para guardar los cambios.
    for i in range(len(texto)):
        if texto[i]=="e":
            codificado+="1"
        elif texto[i]=="u":
            codificado+="2"
        elif texto[i]=="c":
            codificado+="3"
        elif texto[i]=="a":
            codificado+="4"
        elif texto[i]=="l":
            codificado+="5"
        elif texto[i]=="i":
            codificado+="6"
        elif texto[i]=="p":
            codificado+="7"
        elif texto[i]=="t":
            codificado+="8"
        elif texto[i]=="o":
            codificado+="9"
        elif texto[i]==" ":#espacio.
            codificado+="°"
        else:
            codificado+=texto[i]#otras letras que no se tienen que cambiar.
    return codificado.upper()
def decodificarEucalipto(texto):
    codificado=""#variable en blanco para guardar los cambios.
    for i in range(len(texto)):
        if texto[i]=="1":
            codificado+="e"
        elif texto[i]=="2":
            codificado+="u"
        elif texto[i]=="3":
            codificado+="c"
        elif texto[i]=="4":
            codificado+="a"
        elif texto[i]=="5":
            codificado+="l"
        elif texto[i]=="6":
            codificado+="i"
        elif texto[i]=="7":
            codificado+="p"
        elif texto[i]=="8":
            codificado+="t"
        elif texto[i]=="9":
            codificado+="o"
        elif texto[i]=="°":#espacio.
            codificado+=" "
        else:
            codificado+=texto[i]#otras letras que no se tienen que cambiar.
    return codificado.upper()
#Cenit polar
#Entradas/salidas
def cenitPolar():
<<<<<<< Updated upstream
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
=======
    print("\n........................\n")
    print("Cenit Polar".center(24," "))
    print("\n........................\n")
    while True:
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        texto=input("Ingrese texto a codificar(solo letras minúsculas, espacios, comas. No se aceptan tildes.):")
=======
        texto=input("Ingrese texto a codificar(solo letras, espacios, comas. No se aceptan tildes.): ")
>>>>>>> Stashed changes
        texto.lower()#para también trabajar con letras mayúsculas.
        aceptados=["a","b","c","d","e","f","g","h","i","j","k","l","m","n\
","ñ","o","p","q","r","s","t","u","v","w","x","y","z",","," "]#Lista de caracteres permitidos.
        if texto == "":#si es vacío.
            continue
        elif texto==" ":#si es solo un espacio.
            continue
        else:
            algo=0#variable para contar si existe algún caracter que no es aceptado(numeros, puntos, etc...)
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
        texto=input("Ingrese texto a decodificar(solo letras o el caracter ¬. No se aceptan tildes): ")
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
#Código morse.
#Entrada
def iniciarCodigoMorse():
    """
    Función: Iniciar la códificación morse del texto a ingresar.
    Entrada: N/A. Dentro de esta función se solicita un texto, tiene que seguir las intrucciones.
    Salida: N/A.
    """
    print("\n======================================\n")
    print("Código Morse")
    print("\n======================================")
    while True:#ciclo infinito hasta que se ingrese correctamente un texto.
        try:
            eleccion=validarOpcion()
            if eleccion==1:#Codificar texto a código morse.
                print("\n¡¡Ha seleccionado la opción para códificar un texto a código morse!!\n")
                print("\nINSTRUCCIONES:\nEl texto a ingresar debe contener únicamente letras(mayúsculas, no se acepta la ñ ni tildes), espacios o numeros.(no se otro \
tipo de caracter especial). El texto no puede empezar por espacio.\n")
                texto=input("Ingrese texto a codificar: ")
                if validarCodigoMorse(texto):#Validar es true, codifique.
                    morse=codificarMorse(texto)#guarda el codigo morse.
                    imprimirCodigoMorse(morse)#llama funcion de salida para imprimir.
                    return ""
            #si el usuario ingresa 1 pero mete algo mal, lo devuelve a la elección porque puede que haya digitado mal.
            elif eleccion==2:
                print("\n¡¡Ha seleccionado la opción para decodificar un código morse!!\n")
                print("INSTRUCCIONES:\nEl código morse debe contener únicamente los siguientes caracteres: '.-|^'. Debe empezar\
 y terminar por '.' o '-'. Las letras deben llevar el caracter '^' entre cada una de ellas, excepto cuando después de una letra sigue un espacio\
, en ese caso no se coloca '^'. Los espacios se representan con el caracter '|', el código después del espacio o sea la que sigue\
 al '|' no debe contener el caracter '^'.")
                codificado=input("Ingrese su código morse, siga las instrucciones: ")#pide el código morse.
                if validarDecodificarMorse(codificado):#valida el código morse.
                    decodificado=decodificarMorse(codificado)#guarda la decodificación.
                    texto=imprimirDecodificacionMorse(decodificado)
                    imprimirDecodificacionMorse(texto)
                    return ""
            else:
                print("\INSTRUCCIONES PARA INGRESAR DATOS: \nEl código debe tener solo letras(sin la ñ), numeros y entre cada código de letra debe\
haber el siguiente caracter: '^' y para el espacio debe representarse con el caracter: '|'. ")
                codificado=input("Ingrese código morse para decodificarlo: ")
        except:
            print("\nIntente de nuevo.\n")#para vacío en la elección de codificar/decodificar.
            continue
#Salida codigo morse
def imprimirCodigoMorse(morse):#solo imprimer
    """
    Función: Mostrar el código morse.
    Entrada: 
    -morse(str): Código morse.
    Salida: N/A.
    """
    print(morse)
    return ""
def imprimirDecodificacionMorse(texto):
    """
    Función: Mostrar el texto decodificado.
    Entrada:
    -texto(str): Texto decodificado
    Salida:
    -""
    """
    print(texto)
    return ""
#validar opcion codigo morse
def validarOpcion():
    while True:
        opcion=int(input("\nDigite: 1 para codificar texto a código morse o 2 para decodificar código morse a texto: "))
        if opcion<1 or opcion>2:
            continue
        return opcion
#validar codificar morse
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
            print("Ha ingresado un caracter invalido.")
            return False
    return True
#validar decodificación morse.
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
        print("Debe ingresar el código morse.")
        return False
    if not texto:#Enter vacío.
        print("Debe ingresar el código morse.")
        return False
    if texto[0]=="^" or texto[0]=="|" or texto[-1]=="^" or texto[-1]=="|":#el primero y el último no pueden ser estos.
        print("Debe respetar las intrucciones.")
        return False
    for j in range(len(texto)):
        x=texto[j]
        if j==len(texto)-1:
            y=texto[j]
        else:
            y=texto[j+1]
        if (x=="^" and y=="|") or (y=="^" and x=="|"):
            return False
    for i in range(len(texto)):
        if texto[i] in caracteresValidos:
            continue
        else:
            print("Ha ingresado un caracter invalido.")
            return False
    return True
#Proceso codificar morse
def codificarMorse(codificar):
    """
    Función: Pasar un texto(letras minúsculas, numeros y espacios) a código morse.
    Entrada: 
    -codificar(str): Texto a codificar.
    Salida: 
    -morse(str): Código morse del texto ingresado. 
    """
    lista=[["A",".-"],["B","-..."],["C","-.."],["D","-.."],["E","."],["F","..-."],["G","--."],["H","....\
"],["I",".."],["J",".---"],["K","-.-"],["L",".-.."],["M","--"],["N","-."],["O","---"],["P",".--."],["Q","--.-"],["R",".-.\
"],["S","..."],["T","-"],["U","..-"],["V","...-"],["W",".--"],["X","-..-"],["Y","-.--"],["Z","--.."],["0","-----\
"],["1",".----"],["2","..---"],["3","...--"],["4","....-"],["5","....."],["6","-...."],["7","--..."],["8","---..\
"],["9","----."],[" ","|"]]#lista de caracteres aceptados.
    morse=""
    for letra in codificar:#saca letra
        for sublista in lista:#ciclo recorre lista.
            if letra==" " and morse[-1]=="^":#quita los techos antes del espacio.
                morse=morse[0:-1]#quita el techito del morse que está antes del espacio.
                continue#pasa a la siguiente sublista, porque no ha cambiado el pipe.
            if sublista[0]==letra:#saca el valor 0 de la sublista y compara la letra.
                morse+=sublista[1]#pega el valor del binario de la sublista.
                if sublista[1]=="|":#no pone techo despues de |
                    continue#pasa a la siguiente letra.
                morse+="^"#le pega techo al morse.
    morse=morse[0:-1]#quita el último techo.
    return morse
#proceso decodificar morse
def decodificarMorse(morse):
    """
    Función: Decodificar un código morse, debe seguir las restricciones que se le dicen en iniciarCodigoMorse().
    Entrada: 
    -morse(str): Código morse.
    Salida:
    -texto(str): Texto decodificado.
    """
    lista=[["A",".-"],["B","-..."],["C","-.-."],["D","-.."],["E","."],["F","..-."],["G","--."],["H","....\
"],["I",".."],["J",".---"],["K","-.-"],["L",".-.."],["M","--"],["N","-."],["O","---"],["P",".--."],["Q","--.-"],["R",".-.\
"],["S","..."],["T","-"],["U","..-"],["V","...-"],["W",".--"],["X","-..-"],["Y","-.--"],["Z","--.."],["0","-----\
"],["1",".----"],["2","..---"],["3","...--"],["4","....-"],["5","....."],["6","-...."],["7","--..."],["8","---..\
"],["9","----."],[" ","|"]]#lista de caracteres aceptados.
    if morse[-1]!="^":
        morse+="^"
    texto=""#guarda el texto.
    codigo=""#guarda los códigos morse.
    for caracter in morse:#saca caracter
        if caracter!="^" and caracter!="|":#Si el caracter que tiene es diferente de estos peguelo.
            codigo+=caracter#pega morse de letra.
            continue#continua con el siguiente caracter.
        for sublista in lista:#compara morse de letra con los que están en la lista
            if sublista[1]==codigo:#compara los el codigo con las sublistas.
                texto+=sublista[0]
                if caracter=="|":#si lo que tiene es | pegue un espacio.
                    texto+=" "#pega espacio
                codigo=""
    return texto
#Sufamelico
#Entrada
def iniciarSufamelico():
    """
    Función: Iniciar el proceso de codificación/decodificación Sufamelica.
    Entrada: N/A.
    Salida: N/A.
    """
    while True:#ciclo para obligar a que ingrese datos correctamente.
        try:#captura error vacío en opción.
            opcion=int(input("\nIngrese 1 para codificar o 2 para decodificar: "))#pide opción
            if opcion==1:#no se separa la validación porque el principal objetivo es el texto, las opciones son solo 2, hasta que no se ingrese bien no pasa.
                texto=input("\nIngrese texto a codificar (debe tener letras mayúsculas, espacios o comas)\
 no se acepta ningún otro tipo de caracter especial, incluyendo a la ñ y tildes: ")#mensaje para cuando esa 1, codificar
            elif opcion==2:#realmente las opciones son solo para el mensaje porque codifica/decodifica la misma función.
                texto=input("\nIngrese texto a decodificar(debe tener letras mayúsculas, espacios o comas)\
 no se acepta ningún otro tipo de caracter especial, incluyendo a la ñ y tildes: ")#mensaje para cuando esa 2, decodificar
            else:
                print("\nIntente de nuevo.\n")#otro número
                continue
        except:#si es vacío u otra cosa.
            print("\nIntente de nuevo.\n")
            continue#lo devuelve.
        if validarSufamelico(texto):#si ingresó 1 o 2 pide un texto y viene aqui para validar el texto.
            procesarSufamelico(texto)#si el texto es válido pasa a codificar/decodificar.
            return ""
        else:
            print("\nSiga las instrucciones para ingresar el texto.\n")#ingresó un texto inválido.
            continue#lo devuelve.
#Validar
def validarSufamelico(texto):
    """
    Función: Validar que el parámetro sea un texto con letra mayúsculas de la A-Z (no acepta caracteres especiales),
    puede contener espacios y comas.
    Entrada:
    -texto(str): Texto a validar.
    Salida:
    -True si cumple las condiciones.
    -False si no cumple las condiciones.
    """
    if texto==" ":#si es un espacio en blanco devuele False.
        print("Debe ingresar un texto.")
        return False
    if re.match("^[\sA-Z,]+$",texto):#Valida que solo contenga letra mayúsculas, espacio o comas.
        return True#si cumple.
    else:
        return False
#Proceso codifica/decodifica
def procesarSufamelico(texto):
    """
    Función: Codificar/decodificar el texto a Sufamelico.
    Entrada: 
    -texto(str): Texto a codificar/decodificar.
    Salida: N/A
    """
    lista=[["S","U"],["U","S"],["F","A"],["A","F"],["M","E"],["E","M"],["L","I"],["I","L"],["C","O"],["O","C"],]#lista para ir cambiando letras.
    todo=["S","U","F","A","M","E","L","I","C","O"]#si la letra no está aqui no va a cambiarlo.
    final=""#codificado/decodificado
    for letra in texto:#saca letra del texto para comparar con todas las sublistas.
        for sublista in lista: #saca todas las sublistas para buscar la letra en la posición 0 para cambiarla por la 1.
            if not letra in todo:#si la letra que tiene no es alguna de las que cambia, peguela y siga con la otra letra.
                final+=letra#pega letra que no tiene otra para cambiar.
                break#pasa a la siguiete letra del for.
            elif sublista[0]==letra:#si la letra que tiene coincide con alguna sublista en la posición 0.
                final+=sublista[1]#pegue la letra 1 de la sublista.
                break#pase a la siguiente
    return final
#Salida
def imprimirSufamelico(texto):
    """
    Función: Mostar el resultado de la codificación/decodificación del texto.
    Entrada:
    -texto(str): Texto codificado/decodificado.
    Salida: N/A.
    """
    print("Su texto es: "+texto)
    return ""
#Programa principal.
#eucalipto()
#murcielago()
#cenitPolar()
#iniciarCodigoMorse()
#iniciarSufamelico()