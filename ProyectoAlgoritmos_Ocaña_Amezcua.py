import os
import random
import collections
import numpy as np

infoINSERTIONSORT = """
TIPO DE ENTRADA: ARREGLO QUE SUS ELEMENTOS ESTÁN DESORDENADOS.

TIPO DE SALIDA: El mismo arrelgo poero con sus elementos ordenados.
    
DESCRIPCIÓN DEL ALGORITMO: CADA ELEMENTO DEBE SER INSERTADO EN SU POSICIÓN CORRECTA. LA BÚSQUEDA SE SECUENCIALMENTE PARA IR ACOMODANDO LOS LEMENTOS UNO POR UNO EN LA SUBLISTA QUE YA ESTÁ ORDENADA. CUANDO SE TIENE UN ELEMENTO i, SE HACE LA COMPARACIÓN CON LOS ELEMENTOS QUE ESTÁN POR DELANTE DE ÉL Y SI SE ENCUENTRA UN ELEMENTO MENOR QUE i, ENTONCE SE HACE EL INTERCAMBIO DE POSICIÓN ENTRE LOS DOS ELEMENTOS.
    
TIEMPO DE EJECICIÓN: O(n^2)
REFERENCIA: htps://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm 

--------------------------------------"""

infoBUSQUEDABINARIA = """
TIPO DE ENTRADA: UN ARREGLO ORDENADO Y UN ELEMENTO QUE SE VA A BUSCAR EN ÉL.

TIPO DE SALIDA: REGRESA UN TEXTO DÓNDE DICE SI SÍ SE ENCONTRÓ O NO EL VALOR BUCADO EN EL ARREGLO.

DESCRIPCIÓN DEL ALGORITMO: LA BÚSQUEDA BINARIA ES UN ALGORITMO EFICIENTE PARA ENCONTRAR UN ELEMENTO EN UNA LISTA ORDENADA DE ELEMENTOS. FUNCIONA AL DIVIDIR REPETIDAMENTE A LA MITAD LA PORCIÓN DE LA LISTA QUE PODRÍA CONTENER AL ELEMENTO, HASTA REDUCIR LAS UBICACIONES POSIBLES A SOLO UNA.

TIEMPO DE EJECICIÓN: O(nlgn)

REFERENCIA: https://es.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

------------------------------------"""

infoFIBONACCIRECURSIVO = """
TIPO DE ENTRADA: UN NÚMERO n QUE SE REFIERE AL ELMENTO n DE LA SERIE DE FIBONACCI.

TIPO DE SALIDA: LA SUCESIÓN DE FIBONACCI HASTA EL ELEMENTO n.

DESCRIPCIÓN DEL ALGORITMO: LA SUCESIÓN COMIENZA CON LOS NÚMEROS 0 Y 1​ A PARTIR DE ESTOS, CADA TÉRMINO ES LA SUMA DE LOS DOS ANTERIORES», ES LA RELACIÓN DE RECURRENCIA QUE LA DEFINE.

TIEMPO DE EJECICIÓN: O(2^n), NO SE RECOMIENDA SU USO.

REFERENCIA:https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci


-----------------------------------"""


infoFIBONACCIITERATIVO = """
TIPO DE ENTRADA: UN NÚMERO n QUE SE REFIERE AL ELMENTO n DE LA SERIE DE FIBONACCI.

TIPO DE SALIDA: LA SUCESIÓN DE FIBONACCI HASTA EL ELEMENTO n.

DESCRIPCIÓN DEL ALGORITMO: LA SUCESIÓN COMIENZA CON LOS NÚMEROS 0 Y 1​ A PARTIR DE ESTOS, CADA TÉRMINO ES LA SUMA DE LOS DOS ANTERIORES», ES LA RELACIÓN DE RECURRENCIA QUE LA DEFINE.

TIEMPO DE EJECICIÓN: o(n)

REFERENCIA: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci"


-----------------------------------"""


infoFACTORIALITERATIVO = """
TIPO DE ENTRADA: UN NÚMERO PARA CALCULAR SU FACTORIAL.

TIPO DE SALIDA: EL FACTORIAL DEL NÚMERO QUE INGRESÉ.

DESCRIPCIÓN DEL ALGORITMO: CALCULA EL FACTORIAL DEL NÚMERO QUE SEA INGRESADO

TIEMPO DE EJECICIÓN: 0(n)


-----------------------------------"""


infoMERGE = """
TIPO DE ENTRADA: UN ARREGLO CON SUS ELEMENTOS DESORDENADOS.

TIPO DE SALIDA: EL MISMO ARREGLO CON SUS ELEMENTOS ORDENADOS.

DESCRIPCIÓN DEL ALGORITMO: DIVIDE EL PROBLEMA EN DOS SUCECIONES DE TAMAÑO n/2, PARA ORDENAR RECURSIVAMENTE CADA UNAY DESPUÉS MEZCLAS LAS DOS SUCESIONES PARA OBTENER LA SUCECIÓN TOTAL ORDENADA.

TIEMPO DE EJECICIÓN: O(n)

-----------------------------------"""


infoHEAPSORT = """
TIPO DE ENTRADA: UN ARREGLO CON SUS ELEMENTOS DESORDENADOS. 

TIPO DE SALIDA: EL MISMO ARREGLO CON SUS ELEMENTOS ORDENADOS.

DESCRIPCIÓN DEL ALGORITMO: EL MÉTODO DE ORDENACIÓN SE PUEDE DESCRIBIR CON LOS SIGUIENTES PASOS:

1. CONSTRUIR UN MONTÍCULO INICIAL CON TODOS LOS ELEMENTOS DEL VECTOR A [1], A [2], …., A [N]
2. INTERCAMBIAR LOS VALORES DE A [1] Y A [N] (SIEMPRE QUEDA EL MÁXIMO EN EL EXTREMO)
3. RECONSTRUIR EL MONTÍCULO CON LOS ELEMENTOS A [1], A [2],……, A [N-1]
4. INTERCAMBIAR LOS VALORES DE A [1] Y A [N-1]
5. RECONSTRUIR EL MONTÍCULO CON LOS ELEMENTOS A [1], A [2],……, A [N-2]

TIEMPO DE EJECICIÓN: O(nlgn)

REFERENCIA: http://www.udb.edu.sv/udb_files/recursos_guias/informatica-ingenieria/programacion-iv/2019/ii/guia-5.pdf


-----------------------------------"""


infoQUICKSORT = """
TIPO DE ENTRADA: UN ARREGLO CON SUS ELEMENTOS DESORDENADOS.

TIPO DE SALIDA: EL MISMO ARREGLO CON SUS ELEMENTOS ORDENADOS.

DESCRIPCIÓN DEL ALGORITMO: ELEGIR EL ÚLTIMO ELEMENTO DEL CONJUNTO DE ELEMENTOS A ORDENAR, AL QUE LLAMAREMOS PIVOTE.

RESITUAR LOS DEMÁS ELEMENTOS DE LA LISTA A CADA LADO DEL PIVOTE, DE MANERA QUE A UN LADO QUEDEN TODOS LOS MENORES QUE ÉL, Y AL OTRO LOS MAYORES. LOS ELEMENTOS IGUALES AL PIVOTE PUEDEN SER COLOCADOS TANTO A SU DERECHA COMO A SU IZQUIERDA, DEPENDIENDO DE LA IMPLEMENTACIÓN DESEADA. EN ESTE MOMENTO, EL PIVOTE OCUPA EXACTAMENTE EL LUGAR QUE LE CORRESPONDERÁ EN LA LISTA ORDENADA.

LA LISTA QUEDA SEPARADA EN DOS SUBLISTAS, UNA FORMADA POR LOS ELEMENTOS A LA IZQUIERDA DEL PIVOTE, Y OTRA POR LOS ELEMENTOS A SU DERECHA.

REPETIR ESTE PROCESO DE FORMA RECURSIVA PARA CADA SUBLISTA MIENTRAS ÉSTAS CONTENGAN MÁS DE UN ELEMENTO. UNA VEZ TERMINADO ESTE PROCESO TODOS LOS ELEMENTOS ESTARÁN ORDENADOS.SU TIEMPO DE EJECUCIÓN PUEDE SER LINEAL.

TIEMPO DE EJECICIÓN: O(nlgn)

REFERENCIA: https://es.wikipedia.org/wiki/Quicksort#:~:text=El%20ordenamiento%20r%C3%A1pido%20(quicksort%20en,Hoare.

-----------------------------------"""


infoRANDOMZIEDQUICKSORT = """
TIPO DE ENTRADA: UN ARREGLO CON SUS ELEMENTOS DESORDENADOS.

TIPO DE SALIDA: EL MISMO ARREGLO CON SUS ELEMENTOS ORDENADOS.

DESCRIPCIÓN DEL ALGORITMO: ES LO MISMO QUE QUICK SORT, PERO EN CAMBIO EL PIVOTE SE TOMA ALEATORIAMENTE EN VEZ DE TOMAR EL ÚLTIMO ELEMENTO DEL ARRAY.

TIEMPO DE EJECICIÓN: O(nlgn)


-----------------------------------"""

infoCOUNTINGSORT = """
TIPO DE ENTRADA: UN ARREGLO CON SUS ELEMENTOS DESORDENADOS.

TIPO DE SALIDA: EL MISMO ARREGLO CON SUS ELEMENTOS ORDENADOS.

DESCRIPCIÓN DEL ALGORITMO: ES UN ALGORITMO DE ORDENAMIENTO EN EL QUE SE CUENTA EL NÚMERO DE ELEMENTOS DE CADA CLASE PARA LUEGO ORDENARLOS. SOLO PUEDE SER UTILIZADO POR TANTO PARA ORDENAR ELEMENTOS QUE SEAN CONTABLES.
EN ESTE ALGORITMO ES IMPORTANTE CONOCER EL ELEMENTO MÍNIMO Y MÁXIMO  DEL ARRAY.
SOLO ORDENA NÚMEROS ENTEROS, NO VALE PARA ORDENAR CADENAS Y ES DESACONSEJABLE PARA ORDENAR NÚMEROS DECIMALES.
EL NÚMERO MÁS GRANDE TAMBIÉN ES UNA LIMITACIÓN PARA EL ALGORITMO.

TIEMPO DE EJECICIÓN: O(n + k)

REFERENCIA: https://es.wikipedia.org/wiki/Ordenamiento_por_cuentas

-----------------------------------"""

infoRADIXSORT = """
TIPO DE ENTRADA: UN ARREGLO CON SUS ELEMENTOS DESORDENADOS.

TIPO DE SALIDA: EL MISMO ARREGLO CON SUS ELEMENTOS ORDENADOS.

DESCRIPCIÓN DEL ALGORITMO: ESTA FORMA DE ORDENAR NÚMEROS CONSISTE EN ORDENAR LAS UNIDADES, DESPUÉS DE LAS DECENAS Y POR ÚLTIMO LAS CENTENAS, ASÍ YA CON TODO ORDENADO ESTARÁN LOS NÚMEROS ORDENADOS.

TIEMPO DE EJECICIÓN: EN ESTE ALGORTMO EL TIEMPO DE EJEUCIÓB VARIA DEPENDIENDO QUE ALGORITMO DE ORDENAMIENTO OCUPEMOS.

-----------------------------------"""

infoMULTIPLICACIONMATRICES = """
TIPO DE ENTRADA: LA DIMENSIÓN DE CADA MATRIZ Y LOS ELEEMNTOS DE CADA MATRIZ

TIPO DE SALIDA: UNA MATRIZ QUE ES EL RESULTADO DE LA MULTIPLICACIÓN DE LAS DOS MATRICIES QUE SE INTRODUCIERON.

DESCRIPCIÓN DEL ALGORITMO: VERIFICAR SI SE CUMPLE LA CONDICIÓN PARA MULTIPLICAR MATRICES Y EN CASO QUE SÍ REALIZAR LA MULTIPLICACIÓN. 
EN CASO QUE NO ENTONCES NO SE REALIZARÁ LA MULTIPLICACIÓN.

TIEMPO DE EJECICIÓN: O(n^3)


-----------------------------------"""


infoLCS = """
TIPO DE ENTRADA: DOS CADENAS DE TEXTO.

TIPO DE SALIDA: EL TAMAÑO DE LA CADENA EN COMÚN Y LA CADENA EN COMÚN.

DESCRIPCIÓN DEL ALGORITMO: SE TRATA DE ENCONTRAR UNA SUBSECUENCIA MÁS LARGA QUE ES COMÚN EN UN CONJUNTO DE SECUENCIAS.

TIEMPO DE EJECICIÓN: O(nm)

REFERENCIA: https://es.wikipedia.org/wiki/Problema_de_subsecuencia_com%C3%BAn_m%C3%A1s_larga


-----------------------------------"""


infoBFS = """
TIPO DE ENTRADA: UNA GRÁFICA

TIPO DE SALIDA: LISTA DE CÓMO SE FUERON ABRIENDO LOS NODOS.

DESCRIPCIÓN DEL ALGORITMO: SU FUNCIONAMIENTO CONSISTE EN IR EXPANDIENDO TODOS Y CADA UNO DE LOS NODOS QUE VA LOCALIZANDO, DE FORMA RECURRENTE, EN UN CAMINO CONCRETO. CUANDO YA NO QUEDAN MÁS NODOS QUE VISITAR EN DICHO CAMINO, REGRESA DE MODO QUE REPITE EL MISMO PROCESO CON CADA UNO DE LOS HERMANOS DEL NODO YA PROCESADO.

TIEMPO DE EJECICIÓN: O(V + E)

REFERENCIA: https://es.wikipedia.org/wiki/B%C3%BAsqueda_en_profundidad

-----------------------------------"""

#FUNCIONALIDADES---------------------------------
def informaciónAlgoritmo( x ):
  if x == 1:
    print("\n|  INSERTION SORT  |")    
    print(infoINSERTIONSORT)

  if x == 2:
    print("| BÚSQUEDA BINARIA |")
    print(infoBUSQUEDABINARIA)


  if x == 3:
    print("| FIBONACCI RECURSIVO |")
    print(infoFIBONACCIRECURSIVO)

  if x == 4:
    print("| FIBONACCI ITERATIVO |")
    print(infoFIBONACCIITERATIVO)

  if x == 5:
    print("| FACTORIAL ITERATIVO |")
    print(infoFACTORIALITERATIVO)

  if x == 6:
    print("| MERGE |")
    print(infoMERGE)
  
  if x == 7:
    print("| HEAP SORT|")
    print(infoHEAPSORT)

  if x == 8:
    print("| QUICK SORT |")
    print(infoQUICKSORT)

  if x == 9:
    print("| RANDOMZIED QUICK SORT |")
    print(infoRANDOMZIEDQUICKSORT)

  if x == 10:
    print("| COUNTING SORT |")
    print(infoCOUNTINGSORT)

  if x == 11:
    print("| RADIX SORT |")
    print("\n\nESTE MÉTODO NO ES TAN RECOMENDABLE. EN ESTE PROGRAMA SIRVE BIEN PARA NÚMEROS DE TRES DÍGITOS, CON DOS DIGÍTOS O MÁS DE TRES TENDRÁ PROBLEMAS.\n\n", infoRADIXSORT)

  if x == 12:
    print("|RECURSIVE N-QUEENS  |")
    print("\n\n")

def llenarArreglo( numAlgoritmo ):
  intA = []
  intTamañoArreglo = int(input("\n¿De qué tamaño es tu arreglo?\nTamaño: "))
  while intTamañoArreglo <= 0:
    os.system("clear")
    informaciónAlgoritmo( numAlgoritmo )

    intTamañoArreglo = int(input("\n¿De qué tamaño es tu arreglo?\nTamaño: "))

  i = 0
  while i < intTamañoArreglo:
    if i == 0:
      intElemento  = int(input("\nIngresa el primer elemnto de tu arreglo: "))
    else:
      intElemento  = int(input("\nIngresa el siguiente elemnto de tu arreglo: "))

    intA.append(intElemento)
    i += 1

  return intA

def terminarAlgoritmo():
  print("\n\nPresiona 0 para reresar al menú principal.")
  opcion = int(input(""))
  while opcion != 0:
    os.system("clear")
    print("\n\nPresiona 0 para reresar al menú principal.")
    opcion = int(input(""))

  os.system("clear")
  MenuPrincipal()



#ALGORITMOS ---------------------------
def INSERTION_SORT():

  Arreglo = []

  #Se presenta la información del algoritmo
  informaciónAlgoritmo(1)

  #Primero se llena el array
  Arreglo = llenarArreglo(1)
  intTamañoArreglo = len(Arreglo)

  os.system("clear")

  #Se presenta la información del algoritmo
  informaciónAlgoritmo(1)
  print("\nArreglo inicial: ",Arreglo)

  j = 1
  while j < intTamañoArreglo:
    key = Arreglo[ j ]

    i = j - 1
    while i >= 0 and Arreglo[i] > key:
      Arreglo[i + 1] = Arreglo[i]
      i = i - 1

    Arreglo[i + 1] = key

    j += 1

  
  print("\nArreglo ordenado: ",Arreglo)
  terminarAlgoritmo()


def BUSQUEDA_BINARIA():
  Arreglo = []

  #Se presenta la información del algoritmo
  informaciónAlgoritmo(2)

  Arreglo = llenarArreglo(2)
  intTamañoArreglo = len(Arreglo)

  j = intTamañoArreglo 

  x = int(input("\n¿Cuál es el elemento que deseas buscar?\nElemento:   "))
  os.system("clear")
  print("\nBúsqueda binaria")
  print("\nEs un método para encontra un valor dentro de un arreglo ya ordenado.")
  BUSQUEDA_BINARIA_R(Arreglo, x, 0, j)

def BUSQUEDA_BINARIA_R(Arreglo, x, i , j):

  m = (j + i) // 2
  if m != len(Arreglo) - 1:
  
    #print("m: ",m,"i: ", i, "j", j)

    if m <= j:
      if x == Arreglo[m]:
        os.system("clear")
        #Se presenta la información del algoritmo
        informaciónAlgoritmo(2)
        print("\n\nEl valor sí se encuentra en el arreglo")
        print("\nArreglo inicial: ",Arreglo,"\nElemento buscado: ", x)
      else:
        if x < Arreglo[m] and i < m:
          BUSQUEDA_BINARIA_R(Arreglo, x, i, m )
        else:
          if x > Arreglo[m] and j > m:
            BUSQUEDA_BINARIA_R(Arreglo, x, m , j )

          else: 
            os.system("clear")
            #Se presenta la información del algoritmo
            informaciónAlgoritmo(2)
            print("\n\nEl valor no se encuentra en el arreglo")
            print("\nArreglo inicial: ",Arreglo,"\nElemento buscado: ", x)
  else:
    if Arreglo[m] == x:
      os.system("clear")
      #Se presenta la información del algoritmo
      informaciónAlgoritmo(2)
      print("\n\nEl valor sí se encuentra en el arreglo")
      print("\nArreglo inicial: ",Arreglo,"\nElemento buscado: ", x)
    else:
      os.system("clear")
      #Se presenta la información del algoritmo
      informaciónAlgoritmo(2)
      print("\n\nEl valor no se encuentra en el arreglo")
      print("\nArreglo inicial: ",Arreglo,"\nElemento buscado: ", x)

  terminarAlgoritmo()


def FIBONACCI( tipoFibonacci ):
  serieF = []
  informaciónAlgoritmo( tipoFibonacci )

  print("\n\nIngresa el número de elementos que deseas imprimir")
  n = int(input("Número de elementos: "))
  while n < 1:
    os.system("cls")
    print("\n\nIngresa el número de elementos que deseas imprimir")
    n = int(input("Número de elementos: "))

  #Fibonacci Recursivo
  if tipoFibonacci == 3:
    i = 0
    while i < n:
      serieF.append(FIBONACCI_R(i)) 
      i += 1

    print("\n\nLa serie de Fibonacci con ",n," elementos es: ",serieF)

   #Fibonacci Iterativo
  if tipoFibonacci == 4:
    i = 0
    while i < n:
      serieF.append(FIBONACCI_I(i)) 
      i += 1

    print("\n\nLa serie de Fibonacci con ",n," elementos es: ",serieF)
  
  terminarAlgoritmo()
  
def FIBONACCI_R( n  ):
  if n == 0:
    return 0
  else:
    if n == 1:
      return 1
    else:
      x = FIBONACCI_R( n - 1 )
      y = FIBONACCI_R( n- 2 )
      return (x + y)
  
def FIBONACCI_I( n  ):
  if n == 0:
    return 0
  else:
    x = 0
    y = 1

    i = 1
    while i < n:
      z = x + y
      x = y
      y = z

      i += 1
  return y


def FACTORIAL_I():
  informaciónAlgoritmo(5)

  print("\n\n¿De qué número deseas calcular su factorial?")
  x = int(input("Número: "))

  factorial = 1
  i = 1
  while i <= x:
    factorial = factorial * i
    i += 1

  print("\n\nEl factorial de ",x," es: ",factorial)
  terminarAlgoritmo()


def MERGE( tipoMerge ):

  informaciónAlgoritmo( tipoMerge )
  Array = llenarArreglo( tipoMerge )

  os.system("clear")
  informaciónAlgoritmo( tipoMerge )
  print("\n\nArrgleo a ordenar: ",Array)

  MERGE_SORT( Array )
  print("\nArreglo ordenado: ",Array)

  terminarAlgoritmo()

def MERGE_SORT( Array ):

  L = []
  R = []

  if len(Array) > 1:
    q = len(Array)//2

    L = Array[:q]
    R = Array[q:]

    MERGE_SORT( L )
    MERGE_SORT( R )

    i = 0
    j = 0
    k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        Array[k] = L[i]
        i += 1
      else:
        Array[k] = R[j]
        j += 1

      k += 1

    while i < len(L):
      Array[k] = L[i]
      i += 1
      k += 1
 
    while j < len(R):
      Array[k] = R[j]
      j += 1
      k += 1


def HEAP( tipoHeap ):
  informaciónAlgoritmo(tipoHeap)

  Array = llenarArreglo(tipoHeap)
  os.system("clear")
  informaciónAlgoritmo(tipoHeap)
  print("\n\nArreglo a ordenar: ", Array)
  HEAP_SORT(Array)
  print("\n\nArreglo ordenado: ", Array)

def LEFT(i):
  return 2 * i

def RIGTH(i):
  return 2 * i + 1

def MAX_HEAPIFY( Array, lenArray, i ):

  l = LEFT(i)
  r = RIGTH(i)
  

  if l < lenArray and Array[l] > Array[i]:
    largest = l
  else:
    largest = i

  if r < lenArray  and Array[r] > Array[largest]:
    largest = r

  if largest != i:
    aux = Array[i]
    Array[i] = Array[largest]
    Array[largest] = aux

    MAX_HEAPIFY(Array , lenArray, largest)

def HEAP_SORT( Array ):
  
  lenArray = len(Array)

  for i in range( lenArray//2 - 1, -1, -1):
    MAX_HEAPIFY( Array, lenArray, i )

  for i in range(lenArray - 1, 0, -1):
    aux = Array[i]
    Array[i] = Array[0] 
    Array[0] = aux
    
    MAX_HEAPIFY(Array, i, 0)
  

def QUICK_SORT():
  informaciónAlgoritmo(8)

  Array = llenarArreglo(8)
  os.system("clear")
  informaciónAlgoritmo(8)
  print("\n\nArreglo a ordenar: ", Array )
  
  QUICK_SORT_ALGORITMO( Array, 0, len(Array) - 1 )

  print("\n\nArreglo a ordenado: ", Array)

def PARTITION( Array, p, r ):
  x = Array[r]
  i = p - 1

  j = p
  while j < r:
    if Array[j] <= x:
      i += 1

      aux = Array[i]
      Array[i] = Array[j]
      Array[j] = aux

    j += 1

  aux = Array[ i + 1 ]
  Array[ i + 1 ] = Array[r]
  Array[r] = aux 

  return i + 1

def QUICK_SORT_ALGORITMO( Array, p, r ):
  if p < r:
    q = PARTITION( Array, p, r )
    QUICK_SORT_ALGORITMO( Array, p, q - 1 )
    QUICK_SORT_ALGORITMO( Array, p + 1, r )


def RANDOM_QUICKSORT():
  informaciónAlgoritmo(9)

  Array = llenarArreglo(9)
  os.system("clear")
  informaciónAlgoritmo(9)
  print("\n\nArreglo a ordenar: ", Array )

  RANDOMIZED_QUICKSORT( Array, 0, len(Array) - 1 )
  print("\n\nArreglo a ordenado: ", Array)

def RANDOMIZED_PARTITION(Array, p, r ):
  i = random.randint(p,r)

  aux = Array[r]
  Array[r] = Array[i]
  Array[i] = aux

  return PARTITION( Array, p, r )

def RANDOMIZED_QUICKSORT(Array, p, r ):
  if p < r:
    q = RANDOMIZED_PARTITION( Array, p, r )
    RANDOMIZED_QUICKSORT( Array, p, q - 1 )
    RANDOMIZED_QUICKSORT( Array, p + 1, r )


def COUNTING_SORT( tipoAlgoritmo ):
  B = []
  informaciónAlgoritmo(tipoAlgoritmo)

  Array = llenarArreglo(tipoAlgoritmo)
  os.system("clear")
  informaciónAlgoritmo(tipoAlgoritmo)
  print("\n\nArreglo a ordenar: ", Array )

  i = 0
  while i < len(Array):
    B.append(0)
    i += 1

  i = 1
  aux = Array[0]
  while i < len(Array):
    if Array[i] > aux:
      aux = Array[i]
    
    i += 1

  COUNTING_SORT_ALGORITMO( Array, B, aux )
  print("\n\nArreglo a ordenado: ", B )

def COUNTING_SORT_ALGORITMO( Array, B, k ):
  C = []

  i = 0
  while i <= k:
    C.append(0)
    i += 1

  j = 0 #bien
  while j < len(Array):
    C[ Array[j] ] = C[ Array[j] ] + 1
    #print("\nj: ",j)
    
    j += 1

  i = 1
  while i <= k:
    C[i] = C[i] + C[ i - 1 ]
    i += 1

  j = len(Array) - 1
  while j >= 0:
    B[ C[ Array[j] ]  - 1] = Array[j]
    C[ Array[j] ] = C[ Array[j] ] - 1
  
    j -= 1


def UNIDADES( x ):
  centenas =  int(x/100)
  decenas = int( (x - (centenas*100) )/10 )
  unidades = int(x - (centenas*100 + decenas * 10))

  return unidades

def DECENAS( x ):
  centenas =  int(x/100)
  decenas = int( (x - (centenas*100) )/10 )

  return decenas

def CENTENAS( x ):
  centenas =  int(x/100)

  return centenas

def RADIX_SORT():
  arrayUnidades = []
  arrayDecenas = []
  arrayCentenas = []
  arraySalida = []
  arrayAux = []

  informaciónAlgoritmo(11)

  Array = llenarArreglo(11)
  os.system("clear")
  informaciónAlgoritmo(11)

  #Array = [ 742, 963, 451, 841 ]
 
  
  print("\n\nArreglo a ordenar: ",Array)
  arraySalida = [0] * len(Array)
  
  
  j = 0
  while j < len(Array):
    #Obtenemos las UNIDADES y las ordenamos
    unidades = UNIDADES(Array[j])
    arrayUnidades.append(unidades) 

    #Obtenemos las UNIDADES y las ordenamos
    decenas = DECENAS(Array[j])
    arrayDecenas.append(decenas) 

    #Obtenemos las CENTENAS y las ordenamos
    centenas =  CENTENAS(Array[j])
    arrayCentenas.append(centenas)   

    #llenamos el array auxiliar
    arrayAux.append(Array[j])
    j += 1

  QUICK_SORT_ALGORITMO( arrayUnidades, 0, len(arrayUnidades) - 1 )
  QUICK_SORT_ALGORITMO( arrayDecenas, 0, len(arrayDecenas) - 1 )
  QUICK_SORT_ALGORITMO( arrayCentenas, 0, len(arrayCentenas) - 1 )
  
  i = 0
  while i < len(Array):
    
    unidadRepetida = 0
    j = 0
    while j < len(Array):
      auxUnidades = UNIDADES(arrayAux[j])
      if arrayUnidades[i] == auxUnidades and unidadRepetida == 0 :
        arraySalida[i] = Array[j]
        unidadRepetida += 1
        arrayAux[j] = -1
      j += 1

    i += 1

  print("\n\nPrimer ordenación: ",arraySalida)


  arrayAux.clear()
  j = 0
  while j < len(Array):
    arrayAux.append(Array[j])
    j += 1


  i = 0
  while i < len(Array):
    decenaRepetida = 0
    j = 0
    while j < len(Array):
      auxDecenas = DECENAS(arrayAux[j])
      if arrayDecenas[i] == auxDecenas and decenaRepetida == 0:
        arraySalida[i] = Array[j]
        decenaRepetida += 1
        arrayAux[j] = -1

      j += 1

    i += 1   

  print("\n\nSegunda ordenación: ",arraySalida)

  arrayAux.clear()
  j = 0
  while j < len(Array):
    arrayAux.append(Array[j])
    j += 1

  i = 0
  while i < len(Array):
    centenaRepetida = 0
    j = 0
    while j < len(Array):
      auxCentena = CENTENAS(arrayAux[j])
      if arrayCentenas[i] == auxCentena and centenaRepetida == 0:
        arraySalida[i] = Array[j]
        centenaRepetida += 1
        arrayAux[j] = -1

      j += 1

    i += 1

  print("\n\nSALIDA FINAL: ",arraySalida)

  terminarAlgoritmo()  


def N_QUEENS():
  Array = []
  informaciónAlgoritmo(12)

  print("\n\n¿Cuántas reínas deseas ordenar?")
  numReinas =  int(input("\nNúmero de Reínas: "))

  while numReinas <= 0:
    os.system("clear")
    print("\nINGRESA UN NÚMERO VÁLIDO POR FAVOR.")
    informaciónAlgoritmo(12)
    print("\n\n¿Cuántas reínas deseas ordenar?")
    numReinas =  int(input("\nNúmero de Reínas: "))
  
  
  i = 1
  while i <= numReinas:
    Array.append(0)
    i += 1

  print("\n\nReínas a ordenar: ",numReinas," en un tablero de: ",numReinas,"x",numReinas)

  RECURSIVE_N_QUEENS(Array, len(Array),  0 )

  print("\n\n",Array)

def RECURSIVE_N_QUEENS(Array, n,  r ):
  if r == n:
    print("\nRRRRRR: ",r)
    return 0
  else:

    j = 0
    while j < n:
      legal = True

      i = 0
      while i < r:
        if (Array[i] == j) or (Array[i] == j + r - i) or (Array[i] == j - r + i): 
          legal = False

        i += 1

      if legal:
        print("\nr: ",r,"  j: ",j)
        Array[r] = j
        RECURSIVE_N_QUEENS(Array, n, r + 1)   

      j += 1


def MATRIX_MULTIPLY_ALGORITMO(A, B , C, filasA, columnasA, columnasB): 

  i = 0
  while i < filasA:

    j = 0
    while j < columnasA:

      k = 0
      while k < columnasA:
        C[i][j] += A[i][k] * B[k][j]

        k += 1

      j += 1

    i += 1

  
  print("\nMATRIZ RESULATDO\n")
  print("",C)

  terminarAlgoritmo()

def MATRIX_MULTIPLY():
  print("| MULTIPLICACIÓN DE MATRICES |")

  print(infoMULTIPLICACIONMATRICES)

  print("\n\nPRIMERA MATRIZ")
  filasA = int(input("\n¿Cuantas filas tiene la matriz?\nFilas: "))
  columnasA = int(input("\n¿Cuantas columnas tiene la matriz?\nColumnas: "))

  while filasA <= 0 or columnasA <= 0:
    os.system("clear")
    print("| MULTIPLICACIÓN DE MATRICES |")

    print(infoMULTIPLICACIONMATRICES)

    print("\n\n**Ni las filas ni las columnas pueden ser menor o igual a 0.**")

    print("\n\nPRIMERA MATRIZ")
    filasA = int(input("\n¿Cuantas filas tiene la matriz?\nFilas: "))
    columnasA = int(input("\n¿Cuantas columnas tiene la matriz?\nColumnas: "))
    

  os.system("clear")
  print("| MULTIPLICACIÓN DE MATRICES |")
  print("\n\nPRIMERA MATRIZ")

  A = np.zeros((filasA, columnasA))

  i = 0
  while i < filasA:
    j = 0
    while j < columnasA:
      print("\nIgresa el elemento en la posición ",i,",",j)
      A[i][j] = int(input("\nElemento: "))
      j += 1

    i += 1

  os.system("clear")
  print("| MULTIPLICACIÓN DE MATRICES |")
  print("\n\nSEGUNDA MATRIZ")
  filasB = int(input("\n¿Cuantas filas tiene la matriz??\nFilas: "))
  columnasB = int(input("\n¿Cuantas columnas tiene la matriz?\nColumnas: "))


  while filasB <= 0 or columnasB <= 0:
    os.system("clear")
    print("| MULTIPLICACIÓN DE MATRICES |")

    print(infoMULTIPLICACIONMATRICES)

    print("\n\n**Ni las filas ni las columnas pueden ser menor o igual a 0.**")

    print("\n\nSEGUNDA MATRIZ")
    filasB = int(input("\n¿Cuantas filas tiene la matriz?\nFilas: "))
    columnasB = int(input("\n¿Cuantas columnas tiene la matriz?\nColumnas: "))

  os.system("clear")
  print("| MULTIPLICACIÓN DE MATRICES |")
  print("\n\nSEGUNDA MATRIZ")

  B = np.zeros((filasB, columnasB))

  i = 0
  while i < filasB:
    j = 0
    while j < columnasB:
      print("\nIgresa el elemento en la posición ",i,",",j)
      B[i][j] = int(input("\nElemento: "))
      j += 1

    i += 1

  os.system("clear")
  print("| MULTIPLICACIÓN DE MATRICES |")
  print("\nMATRIZ A \n",A)
  print("\n\nMATRIZ B \n",B)


  if columnasA != filasB:
    print("\nNo se puede multiplicar debido que las columnas de la primer matriz no son iguales al número de filas de la segunda matriz.")
    return 0
  else:
    a = 0
    C = np.zeros((filasA, columnasB))
    MATRIX_MULTIPLY_ALGORITMO(A, B , C, filasA, columnasA, columnasB)


def PRINT_LCS(x, y, m, n, L):
  aux = ""
  cadena = set()

  if n == 0 or m == 0:
    cadena.add("")
    return cadena

  if x[ m - 1 ] == y[ n - 1 ]:
    aux = PRINT_LCS(x, y, m - 1, n - 1, L)

    for i in aux:   
      cadena.add(i + x[ m - 1 ])

    

  else:
    if L[ m - 1 ][n] >= L[m][ n - 1 ]:
      cadena = PRINT_LCS(x, y, m - 1, n, L)
  
    if L[m][ n - 1 ] >= L[ m - 1 ][n]:
      aux = PRINT_LCS(x, y, m, n - 1, L)

      for i in aux:
        cadena.add(i) 
  
  return cadena

def LCS_LENGTH(x, y, L):
  m = len(x)
  n = len(y)


  i = 0
  while i < ( m + 1 ):
    
    j = 0
    while j < ( n + 1 ):
      
      if i == 0 or j == 0:
        L[i][j] = 0
      
      elif x[ i - 1 ] == y[ j - 1 ]:
        L[i][j] = L[ i - 1 ][ j - 1 ] + 1

      else:
        L[i][j] = max(L[ i - 1 ][j],L[i][ j - 1 ])

      j += 1

    i += 1

  return int(L[m][n])

def LCS():

  print("| LCS |")

  print(infoLCS)

  L = np.zeros(( 100, 100 )) 

  print("\n\nIngresa la primer cadena")
  x = input("Primer cadena: ").upper()

  print("\n\nIngresa la segunda cadena")
  y = input("Segunda cadena: ").upper()


  print("\n\nEl tamaño de las cadenas es: ",LCS_LENGTH(x, y, L))

  m = len(x)
  n = len(y)

  cadena  = PRINT_LCS(x, y, m, n, L)
  print("\nLas cadenas que se encontraron fueron las siguientes: ")
  i = 1
  for j in cadena:
    print(i,".- ",j)
    i += 1

  terminarAlgoritmo()


def BFS_ALGORITMO(grafica, nodoRaiz):
  nodosVisitados = set()
  queue = collections.deque([nodoRaiz])
  nodosVisitados.add(nodoRaiz)

  while queue:
    vertices = queue.popleft()
    print(str(vertices) + " ", end="")

    for i in grafica[vertices]:
      if i not in nodosVisitados:
        nodosVisitados.add(i)
        queue.append(i)

def BFS():
  grafica = {0: [1, 2, 3], 1: [0,4], 2: [0,4], 3: [0, 5, 6], 4: [1,2],5: [3], 6: [3]}

  print("| BFS |")

  print(infoBFS)

  print("\n\nLa gráfica se ingresa desde el código.")

  print("\n\nLa forma en que se abren los nodos es: ")

  BFS_ALGORITMO(grafica, 0)

  terminarAlgoritmo()




#MENÚs PRINCIPALES --------------------------
def MenuMetodosDeOrdenamiento():
  print("\n| MÉTODOS DE ORDENAMIENTO |")
  print("\n\nIntroduce el número del algoritmo que de seas usar:")
  print("\n1.- Insertion Sort")
  print("\n2.- Merge Sort")
  print("\n3.- Heap Sort")
  print("\n4.- Quick Sort")
  print("\n5.- Randomized Quick Sort")
  print("\n6.- Counting Sort")
  print("\n7.- Radix Sort")
  print("\n8.- Regresar Menú Principal")
  print("\n9.- Salir")

  #Entrada del algoritmo a usar y su validación.
  opcion = int(input("\n\nOpción: "))  
  while opcion <= 0 or opcion > 9:
    os.system("clear")
    print("\n| MÉTODOS DE ORDENAMIENTO |")
    print("\n\nIntroduce el número del algoritmo que de seas usar:")
    print("\n1.- Insertion Sort")
    print("\n2.- Merge Sort")
    print("\n3.- Heap Sort")
    print("\n4.- Quick Sort")
    print("\n5.- Randomized Quick Sort")
    print("\n6.- Counting Sort")
    print("\n7.- Radix Sort")
    print("\n8.- Regresar Menú Principal")
    print("\n9.- Salir")
    print("\nPor favor, ingresa un número válido.")
    opcion = int(input("\n\nOpción: "))

  if opcion == 1:
    os.system("clear")
    INSERTION_SORT()

  if opcion == 2:
    os.system("clear")
    MERGE(6)
  
  if opcion == 3:
    os.system("clear")
    HEAP(7)

  if opcion == 4:
    os.system("clear")
    QUICK_SORT()

  if opcion == 5:
    os.system("clear")
    RANDOM_QUICKSORT( )

  if opcion == 6:
    os.system("clear")
    COUNTING_SORT( 10 )

  if opcion == 7:
    os.system("clear")
    RADIX_SORT()
  
  if opcion == 8:
    os.system("clear")
    MenuPrincipal()

  if opcion == 9:
    os.system("clear")
    print("Hasta luego")
    return 0


def MenuFibonacci():

  print("\n| FIBONACCI |")
  print("\n\nIntroduce el número del algoritmo que de seas usar:")
  print("\n1.- Fibonacci recursivo")
  print("\n2.- Fibonacci iterativo")
  print("\n3.- Regresar Menú Principal")
  print("\n4.- Salir")

  #Entrada del algoritmo a usar y su validación.
  opcion = int(input("\n\nOpción: "))
  while opcion <= 0 or opcion > 4:
    os.system("clear")
    print("\n| FIBONACCI |")
    print("\n\nIntroduce el número del algoritmo que de seas usar:")
    print("\n1.- Fibonacci recursivo")
    print("\n2.- Fibonacci iterativo")
    print("\n3.- Regresar Menú Principal")
    print("\n4.- Salir")
    opcion = int(input("\n\nOpción: "))

  if opcion == 1:
    os.system("clear")
    FIBONACCI( 3 )

  if opcion == 2:
    os.system("clear")
    FIBONACCI( 4 )

  if opcion == 3:
    os.system("clear")
    MenuPrincipal()

  if opcion == 4:
    os.system("clear")
    print("Hasta luego")
    return 0


def MenuGraficas():
  print("\nAlgoritmos enfocados a gráficas")
  print("\n\nIntroduce el número del algoritmo que de seas usar:")
  print("\n1.- BFS")
  print("\n2.- Regresar Menú Principal")
  print("\n3.- Salir")

  #Entrada del algoritmo a usar y su validación.
  opcion = int(input("\n\nOpción: "))
  while opcion <= 0 or opcion > 4:
    os.system("clear")
    print("\n| Algoritmos enfocados a gráficas |")
    print("\n\nIntroduce el número del algoritmo que de seas usar:")
    print("\n1.- BFS")
    print("\n2.- Regresar Menú Principal")
    print("\n3.- Salir")
    opcion = int(input("\n\nOpción: "))

  if opcion == 1:
    os.system("clear")
    BFS()

  if opcion == 2:
    os.system("clear")
    MenuPrincipal()

  if opcion == 3:
    os.system("clear")
    print("Hasta luego")
    return 0


def MenuPrincipal():
  print("\nAnálisis de Algoritmos")
  print("\n\nIntroduce el número del algoritmo que de seas usar:")
  print("\n1.- Métodos de ordenación")
  print("\n2.- Búsqueda binaria")
  print("\n3.- Fibonacci")
  print("\n4.- Factorial iterativo")
  print("\n5.- N-Reínas recursivo")
  print("\n6.- Multiplicar matrices")
  print("\n7.- LCS")
  print("\n8.- Algoritmos de gráficas")
  print("\n9.- Salir")

  #Entrada del algoritmo a usar y su validación.
  opcion = int(input("\n\nOpción: "))
  while opcion <= 0 or opcion > 9:
    os.system("clear")
    print("\nAnálisis de Algoritmos")
    print("\n\nIntroduce el número del algoritmo que de seas usar:")
    print("\n1.- Insertion Sort")
    print("\n2.- Búsqueda binaria")
    print("\n3.- Fibonacci")
    print("\n4.- Factorial iterativo")
    print("\n5.- N-Reínas recursivo")
    print("\n6.- Multiplicar matrices")
    print("\n7.- LCS")
    print("\n8.- Algoritmos de gráficas")
    print("\n9.- Salir")
    

    opcion = int(input("\n\nOpción: "))

  if opcion == 1:
    os.system("clear")
    MenuMetodosDeOrdenamiento()

  if opcion == 2:
    os.system("clear")
    BUSQUEDA_BINARIA()
  
  if opcion == 3:
    os.system("clear")
    MenuFibonacci()

  if opcion == 4:
    os.system("clear")
    FACTORIAL_I()

  if opcion == 5:
    os.system("clear")
    N_QUEENS()

  if opcion == 6:
    os.system("clear")
    MATRIX_MULTIPLY()
  
  if opcion == 7:
    os.system("clear")
    LCS()
  
  if opcion == 8:
    os.system("clear")
    MenuGraficas()




  if opcion == 9:
    os.system("clear")
    print("Hasta luego")
    return 0
  


MenuPrincipal()