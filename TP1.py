#Importación
import re

#Cenit polar
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
                print("\nINSTRUCCIONES:\nEl texto a ingresar debe contener únicamente letras(minúsculas, no se acepta la ñ ni tildes), espacios o numeros.(no se otro \
tipo de caracter especial).\n")
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
    caracteresValidos=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," "]
    if texto==" ":#Si es un espacio vacío devuelva False.
        print("Debe ingresar texto.")
        return False
    if not texto:#Enter vacío.
        print("Debe ingresar texto.")
        return False
    for i in range(len(texto)):
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
    #Valor en morse de cada letra y número del alfabeto.
    a=".-"
    b="-..."
    c="-.-."
    d="-.."
    e="."
    f="..-."
    g="--."
    h="...."
    i=".."
    j=".---"
    k="-.-"
    l=".-.."
    m="--"
    n="-."
    o="---"
    p=".--."
    q="--.-"
    r=".-."
    s="..."
    t="-"
    u="..-"
    v="...-"
    w=".--"
    x="-..-"
    y="-.--"
    z="--.."
    uno=".----"
    dos="..---"
    tres="...--"
    cuatro="....-"
    cinco="....."
    seis="-...."
    siete="--..."
    ocho="---.."
    nueve="----."
    cero="-----"
    morse=""#para guardar la codificación.
    for contador in range(len(codificar)):
        if codificar[contador]=="a":
            morse+=a
        elif codificar[contador]=="b":
            morse+=b
        elif codificar[contador]=="c":
            morse+=c
        elif codificar[contador]=="d":
            morse+=d
        elif codificar[contador]=="e":
            morse+=e
        elif codificar[contador]=="f":
            morse+=f
        elif codificar[contador]=="g":
            morse+=g
        elif codificar[contador]=="h":
            morse+=h
        elif codificar[contador]=="i":#error con la i, era porque el contador se llamaba i y les estaba intentando asignar el número al morse.
            morse+=i
        elif codificar[contador]=="j":
            morse+=j
        elif codificar[contador]=="k":
            morse+=k
        elif codificar[contador]=="l":
            morse+=l
        elif codificar[contador]=="m":
            morse+=m
        elif codificar[contador]=="n":
            morse+=n
        elif codificar[contador]=="o":
            morse+=o
        elif codificar[contador]=="p":
            morse+=p
        elif codificar[contador]=="q":
            morse+=q
        elif codificar[contador]=="r":
            morse+=r
        elif codificar[contador]=="s":
            morse+=s
        elif codificar[contador]=="t":
            morse+=t
        elif codificar[contador]=="u":
            morse+=u
        elif codificar[contador]=="v":
            morse+=v
        elif codificar[contador]=="w":
            morse+=w
        elif codificar[contador]=="x":
            morse+=x
        elif codificar[contador]=="y":
            morse+=y
        elif codificar[contador]=="z":
            morse+=z
        elif codificar[contador]=="0":
            morse+=cero
        elif codificar[contador]=="1":
            morse+=uno
        elif codificar[contador]=="2":
            morse+=dos
        elif codificar[contador]=="3":
            morse+=tres
        elif codificar[contador]=="4":
            morse+=cuatro
        elif codificar[contadori]=="5":
            morse+=cinco
        elif codificar[contador]=="6":
            morse+=seis
        elif codificar[contador]=="7":
            morse+=siete
        elif codificar[contador]=="8":
            morse+=ocho
        elif codificar[contador]=="9":
            morse+=nueve
        if contador+1==len(codificar):#Si el que sigue es el total de len, o sea, ya no hay más porque el contador empezó en 0, salgase.
            break
        if codificar[contador+1]==" ":#si el que sigue es espacio pegue |.
            morse+="|"
        elif morse[-1]=="|":#Si lo que tiene de último el morse es |, no pegue ^.
            continue
        else:
            morse+="^"#si no significa que es letra, pegue ^.
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
    codigo=""#para ir sacando las letras, numeros, espacios.
    texto=""
    morse+="^"#Para poder incluir el último código que no se agarraría sin el ^
    for i in range(len(morse)):
        if morse[i]!="^" and morse[i]!="|":#es punto o guión
            codigo+=morse[i]#peguelo
        #if morse[i]=="|":#si es pipe 
          #  texto+=" "#pegue un espacio
        if morse[i]=="^" or morse[i]=="|":#si es ^
            if codigo==".-":
                texto+="a"
            elif codigo=="-...":
                texto+="b"
            elif codigo=="-.-.":
                texto+="c"
            elif codigo=="-..":
                texto+="d"
            elif codigo==".":
                texto+="e"
            elif codigo=="..-.":
                texto+="f"
            elif codigo=="--.":
                texto+="g"
            elif codigo=="....":
                texto+="h"
            elif codigo=="..":
                texto+="i"
            elif codigo==".---":
                texto+="j"
            elif codigo=="-.-":
                texto+="k"
            elif codigo==".-..":
                texto+="l"
            elif codigo=="--":
                texto+="m"
            elif codigo=="-.":
                texto+="n"
            elif codigo=="---":
                texto+="o"
            elif codigo==".--.":
                texto+="p"
            elif codigo=="--.-":
                texto+="q"
            elif codigo==".-.":
                texto+="r"
            elif codigo=="...":
                texto+="s"
            elif codigo=="-":
                texto+="t"
            elif codigo=="..-":
                texto+="u"
            elif codigo=="...-":
                texto+="v"
            elif codigo==".--":
                texto+="w"
            elif codigo=="-..-":
                texto+="x"
            elif codigo=="-.--":
                texto+="y"
            elif codigo=="--..":
                texto+="z"
            elif codigo==".----":
                texto+="1"
            elif codigo=="..---":
                texto+="2"
            elif codigo=="...--":
                texto+="3"
            elif codigo=="....-":
                texto+="4"
            elif codigo==".....":
                texto+="5"
            elif codigo=="-....":
                texto+="6"
            elif codigo=="--...":
                texto+="7"
            elif codigo=="---..":
                texto+="8"
            elif codigo=="----.":
                texto+="9"
            elif codigo=="-----":
                texto+="0"
            else:
                return "Ha ingresado un código incorrecto."
            codigo=""#no mover de arriba del |.
            if morse[i]=="|":#antes de llegar aquí, ya se pegó la letra que tenía, ahora pega el espacio.
                texto+=" "
            continue#siga sacando
    return texto
#Programa principal
cenitPolar()
iniciarCodigoMorse()