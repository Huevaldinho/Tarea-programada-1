#Elaborado por: XXX
#Fecha de Creación: XX/XX/XXX X:XXpm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: X.X.X

#importación de librerías
import sys
sys.setrecursionlimit(5000)

#Definición de funciones
def calcularTarifa(pactual,pporc):
        """
        Funcionamiento:Calcular el aumento de la tarifa de buses
        Entradas:
        - montoActual(int) costo actual,
        - porcentaje(int)valor de aumento
        Salidas: monto aumentado (float), monto con el incremento. 
        """
        aumento=(pactual*pporc)/100
        nuevo=pactual+aumento
        #return pactual+((pactual*pporc)/100)
        return nuevo
    
def calcularTarifaAux(pactual,pporc):
        #Funcionamiento:Validar las entradas para el calculo de aumento
        #Entradas:montoActual(int), porcentaje(int)
        #Salidas: monto aumentado (float)
        if isinstance(pactual,int) and isinstance(pporc,int):
                if pactual>0 and pporc>0:
                        return calcularTarifa(pactual,pporc)
                else:
                        return "Los valores "+str(pactual)+","+str(pporc)+ ": deben ser mayores a 0."
        else:
               return "Los datos de ingreso deben ser de tipo entero."   
def esBisiesto(a):
    """
    Funcionamiento: Analiza si un año es bisiesto o no. 
    Entrada: a(int)Recibe el año a analizar
    Salida: True/False si corresponde a un año bisiesto o no
    """
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def masCercanos(n1, n2, n3, n4):
    """
    Funcionamiento: Determina el número más cercano a cero sin importar si es positivo o negativo. 
    Entrada: Recibe 4 números enteros del usuario.
    Restricciones : Los cuatros números pueden ser negativos, cero, positivos
    Salida: Devuelve una hilera o texto con el número más cercano. 
    """
    dn1 = abs(n1)
    dn2 = abs(n2)
    dn3 = abs(n3)
    dn4 = abs(n4)

    distanciaMenor = min(dn1,dn2,dn3,dn4)

    hilera = "Números más cercanos al cero: \n"      # \ : alt+92
    if distanciaMenor == dn1:
        hilera += str(n1)

    if distanciaMenor == dn2:
        hilera += " " + str(n2)

    if distanciaMenor == dn3:
        hilera += " " + str(n3)

    if distanciaMenor == dn4:
        hilera += " " + str(n4)

    return hilera


def potencia(a,b):
    """
    Funcionamiento:  
    Entradas: 
    Salidas: 
    """
    if a==0 and b==0:
        return "Error"
    elif a==0:
        return a
    elif b==0:
        return 1
    elif b <0:
        return 1 / potencia(a, -b)
    else:
        return a * potencia (a, b-1)

def esPrimoAux(n, divisor):
    """
    Funcionamiento: 
    Entradas: 
    Salidas: 
    """
    if divisor < n//2:
        if n%divisor ==0:
            return False
        else:
            return esPrimoAux(n, divisor+2)
    else:
        return True

def esPrimo(n):
    """
    Funcionamiento:   
    Entradas: 
    Salidas: 
    """
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        divisor=3
        return esPrimoAux(n, divisor)


def primosEntre(desde, hasta):
    """
    Funcionamiento:  Encuentra todos los primos encontrados en un rango.  
    Entrada: Se reciben dos valores enteros que representan un rango.
    Salida: Devolver los números primos contenidos en ese rango
    Restricción : desde < hasta y desde >= 2
    """
    if desde ==  2:
        return str(desde) + " " + primosEntre(desde+1, hasta)
    elif desde %2==0:
        return primosEntre(desde+1, hasta)
    else:
        if desde <= hasta:
            if esPrimo(desde) == True:
                return str(desde) + " " + primosEntre(desde+2, hasta)
            else:
                return primosEntre(desde+2, hasta)
        else:
            return ""
           
#Tarea Iteración Numérica
#Elaborado por: Sebastián Bermúdez Acuña, Kenneth Chacon, Mariángeles Carranza Varela, Yessenia Solano Retana
#Fecha de Creación: 23/3/21 11:22am 
#Fecha de última Modificación: 24/3/21 10:50pm
#Versión: 3.9.2

#Reto 2. Mostrar los valores pares de la cifra numérica.
"""
Funcionamiento: Reciba una cifra numérica y devuelve los elementos pares que componen la cifra numérica.
Entradas: Número Entero
Salidas: Los números pares del número entero
"""
def esPar(pnum):
    if pnum%2==0:
        return True
    else:
        return False
def mostrarPares(pnumero):
    while pnumero!=0:
        digito=pnumero%10
        if esPar(digito)==True:
            return digito
        pnumero//=10
#Reto 3. Encontrar al menos un cero en un número  
"""
Funcionamiento: Recibe una cifra numérica y devuelve si posee un cero o no.
Entradas: Número Entero
Salidas: Indica si el número posee un cero o no
"""
def encontrarAlmenosUnCero(pnumero):
    while pnumero<=0:
        if pnumero==0:
            return True
            break
        else:
            return False
        pnumero=pnumero//10
    return ""
#Reto 5. Contar cantidad de apariciones
"""
Funcionamiento: Determina la cantidad de veces que aparece un número en una cifra numérica.
Entradas: Número entero y el dígito de ese número que desea contar
Salidas: La cantidad de veces que aparece el dígito solicitado en el número entero
"""
def contarRepeticiones(pnum, pnumBuscar):
    i=0
    while pnum!=0:
        digito=pnum%10
        if digito==pnumBuscar:
            i=i+1
        pnum=pnum//10
    print("La cantidad de veces que aparece",pnumBuscar,"es",i," veces")
    return ""
#Reto 7. Elevar un número a una potencia dada
"""
Funcionamiento: Permite elevar un número entero a una potencia indicada.
Entradas: Número entero y el exponente que se le quiere asignar a ese número
Salidas: El resultado de la potencia
"""
def elevarNumeroValidar(pbase,pexponente):
    if pbase>=0:
        if pexponente>=0:
            return elevarNumero(pbase,pexponente)
        else:
            print("Los datos no son positivos")
            return ""
    else:
        print("Los datos no son números positivos")
        return ""

def elevarNumero(pbase,pexponente):
    elevar=pbase**pexponente
    print("El resultado de el número es:", elevar)
    return ""
#Reto 9. Sumar digitos multiplos
"""
Funcionamiento: Recibe un número y un dígito, que retorna la suma de todos sus dígitos, siempre y cuando esos dígitos 
sean múltiplos del dígito especificado por el segundo parámetro.
Entradas: Número Entero y el número del cual se quieren sumar sus múltiplos
Salidas: La suma de los números que son múltiplos del solicitado
"""
def sumarDigitosValidar(pnum,pdigito):
    if pnum>=0:
        if pdigito>=0:
            return sumarDigitosMultiplos(pnum,pdigito)
        else:
            print("Los datos no son positivos")
            return ""
    else:
        print("Los datos no son números positivos")
        return ""
def sumarDigitosMultiplos(pnum,pdigito):
    suma=0
    while pnum!=0:
        resultado=pnum%10
        if resultado%pdigito==0:
            suma=suma+resultado
        pnum=pnum//10
    print(suma)
    return ""
#Reto 11. Convertir a decimal
"""
Funcionamiento: Reciba una cifra numérica binaria y retorna su correspondiente representación decimal.
Entradas: Número binario
Salidas: Número convertido a decimal
"""
def convertirDecimalValidar(pbinario):
    num=pbinario
    largo=len(str(pbinario))
    while largo!=0:
        digito=num%10
        if digito!=0 and digito!=1:
            print("Número no binario")
            return ""
        num=num//10
        largo-=1
    convertirDecimal(pbinario)
    return ""
def convertirDecimal(pbinario):
    i=0
    n=0
    baseDiez=0
    while pbinario>0:
        digito=pbinario%10
        if digito==1:
            n=2**i
            baseDiez=baseDiez+n
        i=i+1
        pbinario=pbinario//10
    print("El valor de el número en base decimal es: ",baseDiez)
    return ""
    
#Elaborado por: Felipe Obando Arrieta y Sebastián Bermúdez
#Fecha de creación: 18/03/2021 7:50 PM
#Última modificación: 27/03/2021 5:15 PM
#Versión: 3.9.2

#Funcion Clasificar los triangulos
"""
Funcionamiento: Te dice el tipo de triangulo según tus angulos.
Entradas: Los 3 ángulos del triángulo
Salidas: Indica el tipo de triángulo entre acutángulo, obstusángulo o rectángulo
"""
def clasiTriangulo(pangulo1,pangulo2,pangulo3):
    if pangulo1<90 and pangulo2<90 and pangulo3<90:#Acutangulo
        print("Su triangulo es un triángulo acutángulo")
        return ""
    elif pangulo1==90 or pangulo2==90 or pangulo3==90:#Rectangulo
        print("Su triángulo es un triángulo rectángulo")
        return ""
    elif pangulo1>90 or pangulo2>90 or pangulo3>90:#Obtusangulo
        print("Su triángulo es un triángulo obtusángulo")
        return ""
#Función Tablas de Multiplicar
"""
Funcionamiento: Multiplica del 1 al 10 el número solicitado
Entradas: El número del cual desea la tabla
Salidas: Resultado de las multiplicaciones del 1 al 10
"""
def multiplicador(n):
    i = 1
    while i<=10:
        tabla=(n*i)
        print(str(n)+"*"+str(i)+"="+str(tabla))
        i=i+1
    return ""
#Función Producción de Fábricas
"""
Función: Calcular la producción anual de cada fábrica, la clave da la fábrica que más produjo en el año e imprime si la fábrica produjo más de $3 000 000 en julio
Entradas: La cantidad total de fábricas, la producción de cada más de cada fábrica
Salidas: Producción anual, la fábrica con más ingresos e identifica si ganó más de $3 000 000 en julio
"""
def produccionFabricas (nFabricas):
    mayoprodu=0
    if nFabricas<=100:
        i=1 #i es la primer fábrica
        while i<=nFabricas:
            try:
                fabricaX=int(input("Digite el ID de la fábrica: "))
            except:
                print("Debe ingresar solo numeros enteros positivos")
                produccionFabricas(nFabricas)
            totanual=0
            j=1
            if fabricaX<0 or fabricaX>nFabricas:
                print("Digite datos válidos")
                return""
            while j<=12:
                ProdMesX=int(input("Digite la producción de la fábrica "+str(fabricaX)+" en el mes "+str(j)+": "))
                totanual=totanual+ProdMesX
                if j==7 and ProdMesX>=3000000:
                    print("\nLa fábrica "+str(fabricaX)+" produjo más de $3.000.000 en el mes de julio\n")
                j+=1
            if mayoprodu<totanual:
                mayoprodu=totanual
                clave=fabricaX
            print("La producción de la última fábrica en el año  es de $ "+str(totanual))
            i+=1
        print("La fábrica que más produjo en el año es: "+str(clave)+" con una producción de $ "+str(mayoprodu))
    return""
    produccionFabricas()

#Tarea Práctica Inicial TStrings
#Elaborado por: Sebastián Bermúdez
#Fecha de creación: 31/03/2021 6:51 PM
#Última modificación: 02/04/2021 6:04 PM
#Versión: 3.9.2

#Ejercicio 1. El número de la suerte:
"""
Función: Sumar valores numéricos de una frase
Entradas: Una frase
Salidas: La suma de los números en esa frase
"""
def numeroSuerte(pcadena):
    indice=0
    suma=0
    while indice<len(pcadena):
        caracter=pcadena[indice]
        if caracter.isdigit()==True:
            suma+=int(caracter)
        indice+=1
    return "\nSu número de la suerte es "+str(suma)+"\n"
#Ejercicio 2. Cantidad de vocales y consonantes:
"""
Función: Cuenta el total de vocales y consonantes de una palabra
Entradas: Palabra exacta
Salidas: Total de vocales y consonantes
"""
def cantidadVocales(pcadena):
    contadorA=0
    contadorE=0
    contadorI=0
    contadorO=0
    contadorU=0
    contadorCons=0
    indice=0
    while indice<len(pcadena):
        caracter=pcadena[indice]
        if caracter=="a":
            contadorA+=1
        elif caracter=="e":
            contadorE+=1
        elif caracter=="i":
            contadorI+=1
        elif caracter=="o":
            contadorO+=1
        elif caracter=="u":
            contadorU+=1
        else:
            contadorCons+=1
        indice+=1
    return contadorA+contadorE+contadorI+contadorO+contadorU
def cantidadVocalesConsonantesValidar(pcadena):
    if pcadena.isalpha()==True:
        return cantidadVocalesConsonantes(pcadena)
    else:
        print("\nSolo puede digitar palabras exactas\n")
        return""
#Ejercicio 3. La palabra es palíndroma:
"""
Función: Verifica si una palabra es palindroma o no
Entradas: Palabra exacta
Salidas: Dice si es palíndroma o no
"""
def palabraPalindroma(pstring):
    indice=0
    length=len(pstring)-1
    while indice<=(length+2)/2:
        if pstring[indice]==pstring[length]:
            contador=True
        else:
            contador=False
            print("\nNo es una palabra palíndroma\n")
            break
        indice+=1
        length-=1
    if contador==True:
        return True
def palabraPalindromaValidar(pvstring):
    if pvstring.isalpha()==True:
        pvstring=pvstring.lower()
        return palabraPalindroma(pvstring)
    else:
        print("\nSolo puede digitar palabras exactas\n")
        return""
#Ejercicio 4. Reconociendo las vocales:
"""
Función: Extraer las vocales de una frase
Entradas: Una frase cualquiera
Salidas: La frase sin las vocales incluidas previamente en la misma
"""
def reconocerVocales(pstring):
    indice=0
    mensaje=""
    contadorVocales=0
    while indice<len(pstring):
        caracter=pstring[indice]
        if caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u":
            contadorVocales+=1
        elif caracter=="á" or caracter=="é" or caracter=="í" or caracter=="ó" or caracter=="ú":
            contadorVocales+=1
        elif caracter=="A" or caracter=="E" or caracter=="I" or caracter=="O" or caracter=="U":
            contadorVocales+=1
        elif caracter=="Á" or caracter=="É" or caracter=="Í" or caracter=="Ó" or caracter=="Ú":
            contadorVocales+=1
        else:
            mensaje+=caracter
        indice+=1
    return print("\n"+mensaje+"\n")
#Ejercicio 5. Cadena espejo:
"""
Función: Mostrar una palabra escrita del revés
Entradas: Una palabra cualquiera
Salidas: La palabrad igitada escrita al revés
"""
def cadenaEspejo(pcadena):
    mensaje=""
    length=len(mensaje)-1
    while len(pcadena)>len(mensaje):
        mensaje+=pcadena[length]
        length-=1
    return print ("\n"+mensaje+"\n")
#Ejercicio 6. Analizador de texto:
"""
Función: Contar las palabras y caracteres de un texto
Entradas: Un texto cualquiera
Salidas: El total de palabras y caracteres en el texto
"""
def analizadorTexto (pstring):
    print("\nCantidad de palabras: "+str(len(pstring.split()))+"\n")
    print("\nCantidad de caracteres: "+str(len(pstring)))
    return""

#Laboratorio Strings 1
#Elaborado por: Sebastián Bermúdez Acuña
#Fecha de creación: 10/04/2021 3:32 PM
#Última modificación: 10/04/2021 10:04 PM
#Versión: 3.9.2

#Reto 1: Análisis de la URL
def analisisURL (pstring):
    '''
    Funcionamiento: Divide la URL en protocolo de carga, formato y dominio de la página. Digita cada uno de los caracteres del dominio de la página.
    Entradas: Función tipoArchivoValidacion
    Salidas: El protocolo de carga, formato y dominio de página escrito por separado. Caracteres del dominio de la página
    '''
    separador=pstring.partition("www.")
    protocolo, formato, dominio = separador
    print("Protocolo de carga: {0}\nFormato de página: {1}\nDominio de la página: {2}".format(protocolo, formato, dominio))
    dominioContador=str({0}).format(dominio)
    for i in range(len(dominioContador)):
        print(dominioContador[i])
#Reto 2: Dime tu nombre de archivo y te digo en qué tipo de archivo trabajas.
def tipoArchivo(pstring):
    '''
    Funcionamiento: Dice el tipo de archivo y los programas para ejecutarlo
    Entradas: Función tipoArchivoValidacion
    Salidas: Nombre de tipo del archivo y los programas para crearlo o visonarlo
    '''
    lista=["ace", "doc", "exe", "log", "pdf"]
    archivoImagen=["bmp", "gif", "jpg"]
    archivoAudio=["ogg","mp3"]
    separador=pstring.split(".")
    if separador[-1] in archivoImagen:
        formaArchivo="archivo de imagen"
        programa="Visor de imágenes, Xnview, Acdsee"
    elif separador[-1] in archivoAudio:
        formaArchivo="archivo de audio"
        programa="Reproductores de audio"
    elif separador[-1]==lista[0]:
        formaArchivo="archivo comprimido"
        programa="WinAce, Winrar, Izarc"
    elif separador[-1]==lista[1]:
        formaArchivo="documento de texto"
        programa="Word, Wordpad, Openoffice"
    elif separador[-1]==lista[2]:
        formaArchivo="aplicación"
        programa="Autoejecutable"
    elif separador[-1]==lista[3]:
        formaArchivo="archivo de texto"
        programa="Bloc de notas, Wordpad"
    elif separador[-1]==lista[4]:
        formaArchivo="documento de texto"
        programa="Adobe Acrobat Reader"
    return "\nSu archivo es de tipo "+formaArchivo+" y su(s) programa(s) para crearlo o visionarlo es(son): "+programa
#Reto 3: Juguemos a ser Scrabble
def scrabble(pstring):
    '''
    Funcionamiento: Cuenta los puntos según los caracteres de una palabra con las leyes del juego "scrabble"
    Entradas: Función scrabbleValidación
    Salidas: Los puntos totales según la palabra
    '''
    lista=["e", "i", "o", "u"]
    contador=0
    for i in range(len(pstring)):
        if pstring[i] in lista:
            if pstring[i]==lista[0]:
                contador+=2
            elif pstring[i]==lista[1]:
                contador+=3
            elif pstring[i]==lista[2]:
                contador+=4
            elif pstring[i]==lista[3]:
                contador+=5
        else:
            contador+=1
    return "\nGanó "+str(contador)+" puntos\n"
#Reto 4: Ubicando a los nuevos ingresos
def ubicacionAulasTEC(pstring):
    '''
    Funcionamiento: Dice la ubicación del aula digitada según el mapa del TEC
    Entradas: Función ubicacionAulasTECvalidacion
    Salidas: Ubicación del aula digitada según el mapa del TEC
    '''
    noroeste=["A","B","E"]
    suroeste=["C","D","I"]
    sureste=["F","G","H"]
    if pstring[0] in noroeste:
        return "Su aula se ubica en la zona noroeste del TEC.\n¡Bienvenido!"
    elif pstring[0] in suroeste:
        return "Su aula se ubica en la zona suroeste del TEC.\n¡Bienvenido!"
    elif pstring[0] in sureste:
        return "Su aula se ubica en la zona sureste del TEC.\n¡Bienvenido!"
    else:
        return "Su aula no pertence al TEC. Revise de nuevo"
#Práctica de listas I
#Elaborado por: Sebastián Bermúdez Acuña y Felipe Obando Arrieta
#Fecha de creación: 20/04/2021 7:52 AM
#Última modificación: 20/04/2021 12:04 PM
#Versión: 3.9.2

#Reto 1
def separarListas (lista):
    listaPar=[]
    listaImpar=[]
    for i in range (len(lista)):
        if esPar(lista[i]): #Funcion de archivo funciones
            listaPar.append(lista[i])
        else:
            listaImpar.append(lista[i])
    listaResultado=[listaPar,listaImpar]
    return listaResultado
#Reto 2
def buscarElemento (lista,indice):
    contador=0
    for i in range(len(lista)):
        if lista[i]==indice:
            contador+=1
    return contador
#Reto 3
def extraerVocales(lista):
    listaVocales=["a","e","i","o","u"]
    listaResultado=[]
    for i in range(len(lista)):
        if lista[i] in listaVocales:
            listaResultado.append(lista[i])
    return listaResultado
#Reto 4
def listaRandom(indice):
    lista=[]
    for i in range(indice):
        numero=random.randint(1,99)
        lista.append(numero)
    mayor=0
    for j in range(len(lista)):
        if lista[j]>mayor:
            mayor=lista[j]
    menor=100
    for k in range(len(lista)):
        if lista[k]<menor:
            menor=lista[k]
    return "Se generó la lista "+str(lista)+" el mayor es: "+str(mayor)+", el menor es: "+str(menor)+", hay una diferencia de: "+str(mayor-menor)
#Reto 5
def agregarEnlista(lista,elemento1,elemento2):
    for i in range(len(lista)):
        if lista[i]==elemento1:
            lista.insert(i+1,elemento2)
    if lista[len(lista)-1]==elemento1:
        lista.append(elemento2)
    return lista
#Reto 6
def eliminarRepetidos(lista):
    listaNueva=[]
    for i in range(len(lista)):
        if not lista[i] in listaNueva:
            listaNueva.append(lista[i])
    return listaNueva
#Reto 7
def sucesionULAM(numero):
    lista=[numero]
    while numero!=1:
        if esPar(numero):
            numero//=2
            lista.append(numero)
        else:
            numero=(numero*3)+1
            lista.append(numero)
    return lista
#Reto 8
def alternativos(lista):
    for i in range(len(lista)-1):
        if esPar(lista[i]) and not esPar(lista[i+1]):
            continue
        elif not esPar(lista[i]) and esPar(lista[i+1]):
            continue
        else:
            return False
    return True
#Reto 9
def listaAscendente(lista):
    for i in range(len(lista)-1):
        if lista[i]<=lista[i+1]:
            continue
        else:
            return False
    return True
#Reto 10
def replicar(lista,indice):
    listaNueva=[]
    for i in range (len(lista)):
        for j in range (indice):
            listaNueva.append(lista[i])
    return listaNueva
#Reto 11
def diferenciaConjuntos (listaA,listaB):
    AmenosB=[]
    BmenosA=[]
    for i in range(len(listaA)):
        if listaA[i] in listaB:
            continue
        else:
            AmenosB.append(listaA[i])
    for j in range (len(listaB)):
        if listaB[j] in listaA:
            continue
        else:
            BmenosA.append(listaB[j])
    return "A-B: "+str(AmenosB)+" B-A: "+str(BmenosA)
#Reto 12
def unionConjuntos (listaA,listaB):
    union=listaA+listaB
    return eliminarRepetidos(union) #Funcion del reto 6
#Reto 13
def interseccionConjuntos(listaA,listaB):
    listaNueva=[]
    for i in range (len(listaA)):
        if listaA[i] in listaB:
            listaNueva.append(listaA[i])
    return listaNueva
#Reto14
def multiplicacionListas (listaA,listaB):
    listaNueva=[]
    for i in range (len(listaA)):
        listaNueva.append(listaA[i]*listaB[i])
    return listaNueva
#Elaborado por: Sebastián Bermúdez Acuña y Felipe Obando Arrieta
#Fecha de Creación: 12/04/21 7:43 PM
#Fecha de última Modificación: XX/XX/XX X:XXpm 
#Versión: 3.9.2

#Importación
import re
from datetime import datetime
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
def codificarCenit(texto):
    """
    Función: Codificar el texto en cenit polar.
    Entrada:
    -texto(str): Texto validado, debe ser letras (sin tilde y minúsculas),espacios y comas.
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
#Bitacora
def crearBitacora(): #esta se llama una linea antes de llamar al menú principal, cuando está todo listo
    bitacora=open("Bitacora.txt","w")
def annadirBitacora(nombre,entra,sale): #esta se llama en el E/S de cada función de procesamiento, a lo último con los parámetros
    now=datetime.now()
    now.strftime("%H:%M:%S")
    bitacora=open("Bitacora.txt","a")
    bitacora.write("\n"+str(now.strftime("%H:%M:%S"))+"\t"+nombre+": entra (\""+entra+"\"), sale (\""+sale+"\")\n")
    bitacora.close()