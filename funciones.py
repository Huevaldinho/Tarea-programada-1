#Elaborado por: Felipe Obando Arrieta y Sebastián Bermúdez
#Fecha de creación: 24/03/2021 1:15 PM
#Última modificación: 27/03/2021 5:15 PM
#Versión: 3.9.2 Windows 10.


#importación de librerías
import sys
sys.setrecursionlimit(5000)

#Definición de funciones
def calcularTarifa(pactual,pporc):
        """
        Funcionamiento:Calcular el aumento de la tarifa de buses
        Entradas:
        - montoActual(int): costo actual
        - porcentaje(int):valor de aumento
        Salidas: 
        -monto aumentado (float): monto con el incremento. 
        """
        aumento=(pactual*pporc)/100
        nuevo=pactual+aumento
        #return pactual+((pactual*pporc)/100)
        return nuevo
    
def calcularTarifaAux(pactual,pporc):
    """
    Funcionamiento:Validar las entradas para el calculo de aumento
    Entradas:
    -montoActual(int): monto actual
    -porcentaje(int):porcentaje
    Salidas: 
    -monto aumentado (float): Monto aumentado
    """
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
    Entrada:
    -a(int):Recibe el año a analizar
    Salida: 
    -True/False si corresponde a un año bisiesto o no
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
    -número1(int): número 1
    -número2(int): número 2
    -número3(int): número 3
    -número4(int): número 4
    Restricciones : Los cuatros números pueden ser negativos, cero, positivos
    Salida: 
    -Devuelve una hilera o texto con el número más cercano. 
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
            print(digito)
        pnumero//=10
    return ""
#Reto 3. Encontrar al menos un cero en un número  
"""
Funcionamiento: Recibe una cifra numérica y devuelve si posee un cero o no.
Entradas: Número Entero
Salidas: Indica si el número posee un cero o no
"""
def encontrarAlmenosUnCero(pnumero):
    mensaje="No posee ningun cero"
    while pnumero!=0:
        digito=pnumero%10
        if digito==0:
            mensaje="Hay almenos un cero"
            break
        pnumero=pnumero//10
    print(mensaje)
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
#Versión: 3.9.2 Windows 10

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