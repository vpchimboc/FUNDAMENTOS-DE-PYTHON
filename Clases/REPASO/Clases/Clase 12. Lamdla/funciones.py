"""En Python, las funciones lambda son funciones anónimas 
que pueden ser definidas en línea y utilizadas para operaciones sencillas. 
La sintaxis básica de una función lambda es la siguiente:
"""
#lambda argumentos: expresión
"""donde "argumentos" son los argumentos de la función separados por comas,
 y "expresión" es una expresión que devuelve el valor de la función.
"""
"""
Las funciones map(), filter() y reduce() 
son funciones incorporadas en Python 
que son comúnmente utilizadas junto con funciones lambda.
"""
"""La función map() toma una función y un iterable como argumentos, 
y devuelve un nuevo iterable con los resultados de aplicar la función 
a cada elemento del iterable. La sintaxis básica de map() es la siguiente:
"""
#map(función, iterable)
"""donde "función" es la función que se aplicará a cada elemento del iterable, 
y "iterable" es el iterable que se procesará.
Por ejemplo, si queremos multiplicar cada elemento de una lista por 2, 
podemos usar map() de la siguiente manera:
"""
lista = [1, 2, 3, 4, 5]
resultado = map(lambda x: x * 2, lista)
print(list(resultado)) # [2, 4, 6, 8, 10]
"""La función filter() 
toma una función y un iterable como argumentos, 
y devuelve un nuevo iterable que contiene los elementos 
del iterable para los cuales la función devuelve True. 
La sintaxis básica de filter() es la siguiente:"""
#filter(función, iterable)
"""donde "función" es la función que se aplicará a cada elemento 
del iterable, y "iterable" es el iterable que se procesará.
Por ejemplo, si queremos filtrar los números impares de una lista, 
podemos usar filter() de la siguiente manera:
"""
lista = [1, 2, 3, 4, 5]
resultado = filter(lambda x: x % 2 == 1, lista)
print(list(resultado)) # [1, 3, 5]
"""La función reduce() toma una función y un iterable como 
argumentos, y devuelve un único valor que resulta de aplicar 
la función a cada par de elementos del iterable. 
La sintaxis básica de reduce() es la siguiente:
"""
#reduce(función, iterable)
"""donde "función" es la función que se aplicará a cada par de elementos 
del iterable, y "iterable" es el iterable que se procesará.
Sin embargo, a partir de Python 3, reduce() se movió a la biblioteca functools, 
por lo que ahora debemos importarla antes de poder usarla. Por ejemplo, 
si queremos calcular la suma de una lista, podemos usar reduce() de la siguiente manera:
"""
from functools import reduce
lista = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, lista)
print(resultado) 
"""En este ejemplo, 
la función lambda recibe dos argumentos (x e y), 
y devuelve su suma. 
reduce() aplica la función a los elementos de la lista 
de manera recursiva, acumulando el resultado en cada iteración. 
En la primera iteración, la función recibe los primeros dos elementos 
de la lista. En la segunda iteración, la función recibe el resultado 
de la primera iteración y el siguiente elemento de la lista, y así sucesivamente.
"""

#############EJEMPLOS##########################
print("Ejemplo de map() con función lambda:")
print("multiplicar cada elemento de una lista por 2")
lista = [1, 2, 3, 4, 5]
resultado = map(lambda x: x * 2, lista)
print(list(resultado)) 

print("Ejemplo de filter() con función lambda:")
print("filtrar los números impares de una lista")
lista = [1, 2, 3, 4, 5]
resultado = filter(lambda x: x % 2 == 1, lista)
print(list(resultado)) 

print("Ejemplo de reduce() con función lambda:")
print("calcular la suma de una lista")
from functools import reduce
lista = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, lista)
print(resultado) 

"""
También puedes combinar varias funciones lambda y funciones 
de orden superior para realizar operaciones más complejas. 
Aquí te proporciono un ejemplo de cómo utilizar map() y reduce() 
juntos con funciones lambda para calcular el promedio de una lista:
"""
"""
En este ejemplo, utilizamos reduce() para calcular la suma 
de los elementos de la lista, y luego dividimos
 el resultado por la longitud de la lista para obtener el promedio.
"""
print("Ejemplos complejos")
print("Calcular el promedio")
from functools import reduce
lista = [1, 2, 3, 4, 5]
promedio = reduce(lambda x, y: x + y, lista) / len(lista)
print(promedio) 
 
 #Ejercicio 1: Dado un listado de números, obtener un nuevo listado con los números pares multiplicados por 2.
"""
En este ejemplo, primero utilizamos filter() para obtener una lista con los números pares, y luego utilizamos map() para multiplicar cada elemento por 2.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))
print(resultado) 

#Ejercicio 2: Dado un listado de palabras, obtener un nuevo listado con las palabras que tienen más de 5 caracteres.
palabras = ["hola", "mundo", "python", "programacion", "lambda"]
resultado = list(filter(lambda x: len(x) > 5, palabras))
print(resultado) 
"""
En este ejemplo, utilizamos filter() para obtener una lista con las palabras que tienen más de 5 caracteres.
"""
#Ejercicio 3: Dado un listado de números, obtener el resultado de multiplicar todos los números entre sí.
from functools import reduce
numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x * y, numeros)
print(resultado)
"""
En este ejemplo, utilizamos reduce() para multiplicar todos los números de la lista entre sí.
"""
#Ejercicio 4: Dado un listado de cadenas de caracteres, obtener un nuevo listado con las cadenas en mayúsculas.
palabras = ["hola", "mundo", "python", "programacion", "lambda"]
resultado = list(map(lambda x: x.upper(), palabras))
print(resultado)
"""
En este ejemplo, utilizamos map() para convertir cada cadena en mayúsculas.
""" 
#Ejercicio 5: Dado un listado de palabras, obtener un nuevo listado con las palabras que empiezan por la letra 'a'.

palabras = ["hola", "adios", "amigo", "azul", "abril"]
resultado = list(filter(lambda x: x.startswith('a'), palabras))
print(resultado)
"""En este ejemplo, utilizamos filter() para obtener una lista con las palabras que empiezan por la letra 'a'."""
#Ejercicio 6: Dado un listado de números, obtener un nuevo listado con los números impares elevados al cuadrado.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, numeros)))
print(resultado) 
"""En este ejemplo, utilizamos filter() para obtener una lista con los números impares, y luego utilizamos map() para elevar cada elemento al cuadrado."""

####EJERCICIOS DE DEBER#####
#Ejercicio 1: Dado un listado de cadenas, obtener un nuevo listado con la longitud de cada cadena.
palabras = ["hola", "adios", "amigo", "azul", "abril"]
resultado = list(map(lambda x: len(x), palabras))
print(resultado) 
#En este ejemplo, utilizamos map() y una función lambda para obtener la longitud de cada cadena de la lista.
#Ejercicio 2: Dado un listado de números, obtener un nuevo listado con los números que son divisibles entre 3.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(filter(lambda x: x % 3 == 0, numeros))
print(resultado) # [3, 6, 9]
#En este ejemplo, utilizamos filter() y una función lambda para obtener una lista con los números que son divisibles entre 3.
#Ejercicio 3: Dado un listado de números, obtener la multiplicación de todos los números.
from functools import reduce
numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x * y, numeros)
print(resultado) # 120
#En este ejemplo, utilizamos reduce() y una función lambda para calcular la multiplicación de todos los números de la lista.
#Ejercicio 4: Dado un listado de palabras, obtener un nuevo listado con las palabras que tienen más de 5 letras.
palabras = ["hola", "adios", "amigo", "azul", "abril"]
resultado = list(filter(lambda x: len(x) > 5, palabras))
print(resultado) # ['abril']
#En este ejemplo, utilizamos filter() y una función lambda para obtener una lista con las palabras que tienen más de 5 letras.
#Ejercicio 5: Dado un listado de números, obtener un nuevo listado con los números elevados a la tercera potencia.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(lambda x: x ** 3, numeros))
print(resultado) # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#En este ejemplo, utilizamos map() y una función lambda para obtener una lista con los números elevados a la tercera potencia.