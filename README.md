# Notas - Curso intermedio de Python
Profesor Facundo Garcia Martoni de Platzi.

![](https://static.platzi.com/media/avatars/Platzi-f730e65b-e92b-44d3-81c0-5c59c4dc4658.png) ![](https://static.platzi.com/media/learningpath/badges/46.png) ![](https://static.platzi.com/media/achievements/badge-intermedio-de-python-d0d16518-5edd-450a-b2a9-0710bded1494.png)

## Tabla de Contenidos

- [Introducción](#introducción)
  - [Zen de Python](#zen-de-python)
  - [Documentación](#documentación)
- [Entorno virtual](#entorno-virtual)
  - [Creando un ambiente virtual con VENV](#creando-un-ambiente-virtual-con-venv)
  - [Instalación de dependencias con pip](#instalación-de-dependencias-con-pip)
  - [Anaconda: alternativa gráfica](#anaconda-alternativa-gráfica)
- [Alternativa a los ciclos: comprehensions](#alternativa-a-los-ciclos-comprehensions)
  - [Listas y diccionarios anidados](#listas-y-diccionarios-anidados)
  - [List comprehensions](#list-comprehensions)
  - [Dictionary comprehensions](#dictionary-comprehensions)
- [Conceptos avanzados de funciones](#conceptos-avanzados-de-funciones)
  - [Funciones anónimas: lambda](#funciones-anónimas-lambda)
  - [Hight order functions (Funciones de orden superior): filter, map and reduce](#hight-order-functions-funciones-de-orden-superior-filter-map-and-reduce)
  - [Proyecto: filtrando datos](#proyecto-filtrando-datos)
- [Manejo de errores ](#manejo-de-errores )
  - [Los errores en el código](#los-errores-en-el-código)
  - [Debugging ó Depuración](#debugging-ó-depuración)
  - [Manejo de excepciones](#manejo-de-excepciones)
  - [Poniendo a prueba el manejo de excepciones](#poniendo-a-prueba-el-manejo-de-excepciones)
  - [Assert statements](#assert-statements)
- [Manejo de archivos](#manejo-de-archivos)
  - [¿Cómo trabajar con archivos?](#cómo-trabajar-con-archivos)
  - [Trabajando con archivos de texto en Python](#trabajando-con-archivos-de-texto-en-python)
  - [Reto final: Juego del Ahorcado o Hangman Game](#reto-final-juego-del-ahorcado-o-hangman-game)

# Introducción

## Zen de Python

[![1](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/1.png?raw=true "1")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/1.png?raw=true "1")

Traducción: 

El Zen de Python, por [Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer) "Tim Peters")

- Lo bello es mejor que lo feo.
- Explícito es mejor que implícito.
- Lo simple es mejor que lo complejo.
- Complejo es mejor que complicado.
- Plano es mejor que anidado.
- Es mejor escaso que denso.
- La legibilidad cuenta.
- Los casos especiales no son lo suficientemente especiales como para romper las reglas.
- Aunque la practicidad vence a la pureza.
- Los errores nunca deben pasar en silencio.
- A menos que esté explícitamente silenciado.
- Ante la ambigüedad, rechace la tentación de adivinar.
- Debe haber una, y preferiblemente solo una, forma obvia de hacerlo.
- Aunque esa forma puede no ser obvia al principio a menos que seas holandés.
- Ahora es mejor que nunca.
- Aunque a menudo nunca es mejor que * ahora mismo *.
- Si la implementación es difícil de explicar, es una mala idea.
- Si la implementación es fácil de explicar, puede ser una buena idea.
- Los espacios de nombres son una gran idea, ¡hagamos más de eso!

## Documentación
- Página oficial de Documentación en Python: 
 [https://docs.python.org/3/](https://docs.python.org/3/ "https://docs.python.org/3/")

- Guía de estilos para Python:
 [https://www.python.org/dev/peps/pep-0008](https://www.python.org/dev/peps/pep-0008 "https://www.python.org/dev/peps/pep-0008")

**Leer Guía y Archivo de Introducción antes de continuar.**

# Entorno virtual

Un entorno virtual es un directorio que contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.

Ejemplo:
La aplicación A puede tener su propio entorno virtual con la versión 1.0 instalada mientras que la aplicación B tiene otro entorno virtual con la versión 2.0. Si la aplicación B requiere que actualizar la librería a la versión 3.0, ésto no afectará el entorno virtual de la aplicación A.

[https://docs.python.org/es/3/tutorial/venv.html](https://docs.python.org/es/3/tutorial/venv.html "https://docs.python.org/es/3/tutorial/venv.html")

## Creando un ambiente virtual con VENV

Creación de ambiente Virtual:
`python3 -m venv nombre_venv`

Usualmente el nombre del ambiente virtual es **venv.**

[![2](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/2.png?raw=true "2")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/2.png?raw=true "2")

Activación del ambiente virtual:
- Windows:
` .\venv\Scripts\activate`
- Unix o MacOS:
`source venv/bin/activate`

Desactivar el ambiente virtual:
`deactivate`

[![3](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/3.png?raw=true "3")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/3.png?raw=true "3")

Crear un alias en linux/mac:
`alias nombre-alias="comando"`

`alias avenv=“source venv/bin/activate”`

Crear alias en Linux Ubuntu:
Para hacerlo en este sistema operativo, necesitamos que cada que la terminal cargue, el alias sea leído, para ello, la terminal tiene un archivo llamado .bashrc que contiene la configuración inicial, y usualmente se encuentra en nuestro home, por lo que hacemos lo siguiente:

- Ejecutar `sudo nano ~/.bashrc`
- Ir al final del archivo
- Agregar el comando: `alias avenv='source venv/bin/activate'`
- Guardar presionando ctrl + o y luego salir con ctrl + x
- Reejecutar la configuración de la terminal: `source ~/.bashrc`
- Activar el entorno vitual `avenv`

De esa forma persistirá siempre, ya que el alias se guarda dentro del archivo de configuración de la terminal 😄

[![4](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/4.png?raw=true "4")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/4.png?raw=true "4")

## Instalación de dependencias con pip

**Pip (package installer for python)** nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, además se puede definir una versión especifica del paquete.

Módulos populares:
- Request
- BeatifulSoup4
- Pandas
- Numpy
- Pytest

`pip install <paquete>` instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique.
`pip freeze` muestra todos los paquetes instalados en tu ambiente virtual.

[![5](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/5.png?raw=true "5")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/5.png?raw=true "5")

Si quisiéramos que alguien más pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:
`pip freeze > requirements.txt`

El resultado de pip freeze se escribe en requirements.txt (puedes usar otro nombre pero el mostrado es una buena practica).

Para instalar paquetes desde un archivo como requirements.txt ejecutamos:
`pip install -r requirements.txt`

[![6](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/6.png?raw=true "6")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/6.png?raw=true "6") [![7](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/7.png?raw=true "7")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/7.png?raw=true "7")

## Anaconda: alternativa gráfica

[![8](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/8.png?raw=true "8")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/8.png?raw=true "8")
Link para descarga: https://www.anaconda.com/products/individual

Software especializado para hacer entornos virtuales e instalar dependencias de manera gráfica que está enfocado en la ciencia de datos.

Anaconda es un programa de Python que contiene los paquetes más utilizados en temas de ingeniería, matemáticas o ciencia, como pueden ser Matplotlib, SciPy y NumPy. Cuenta con versiones para los tres sistemas operativos más importantes: Mac, Windows y Linux.
Y es un ambiente de trabajo para la ciencia de datos que permite hacer funcionar aplicaciones y administrar fácilmente distintos paquetes. Así, Anaconda Navigator puede buscar paquetes en Anaconda Cloud o en otros repositorios, y está disponible para ambientes Windows, macOS y Linux.

[![9](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/9.png?raw=true "9")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/9.png?raw=true "9")

# Alternativa a los ciclos: comprehensions

## Listas y diccionarios anidados

Iniciando con la creación de carpeta en la cual vamos a trabajar código:

[![10](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/10.png?raw=true "10")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/10.png?raw=true "10")

Se inicializa en Git, se crea entorno virtual:

[![11](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/11.png?raw=true "11")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/11.png?raw=true "11")

Para entrar a **VS Code** desde la consola:

[![12](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/12.png?raw=true "12")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/12.png?raw=true "12")

Buena práctica: Ignorar dentro de repositorio.

[![13](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/13.png?raw=true "13")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/13.png?raw=true "13")

Como ejemplo realizamos el siguiente ejercicio de .py con el fin de imprimir una lista y un diccionario anidados:

```python
def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Andrés", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Andrés", "lastname": "Rozo"},
        {"firstname": "Camilo", "lastname": "Vanegas"},
        {"firstname": "Amaparo", "lastname": "Rozo"},
        {"firstname": "Gloria", "lastname": "Vanegas"},
        {"firstname": "Facundo", "lastname": "Garcia"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4, 5.5]
    }

    print("super_list:")
    for i in super_list:
        for key, values in i.items():
            print(key,": ", values);
    
    print("super_dicts:")
    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()
```

Al ejecutarlo en la terminal se obtiene lo siguiente:

[![14](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/14.png?raw=true "14")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/14.png?raw=true "14")

## List comprehensions

Es una construcción sintáctica disponible en Python con la que se pueden crear lista a partir de otros elementos iterables. Siendo una de las contracciones más elegantes del lenguaje.

Para entender el concepto vamos a escribir los cuadrados de los números del 1 al 100 que no sean divisibles por el número 3:

```python
def run():
     squares = []
     for i in range(1, 101):
         if i % 3 != 0:
             squares.append(i**2)

     print(squares)

if __name__ == "__main__":
    run()
```

[![15](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/15.png?raw=true "15")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/15.png?raw=true "15")

Esto se puede realizar en tan solo una línea con la siguiente estructura:

```python
def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

     squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)

if __name__ == "__main__":
    run()
```

### Estructura de list comprehensions

[![16](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/16.png?raw=true "16")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/16.png?raw=true "16") [![17](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/17.png?raw=true "17")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/17.png?raw=true "17")

> - En mi nueva lista voy a guardar para cada elemento en el iterable ese elemento solo si se cumple la condición.
> - En mi lista voy a guardar cada i en el rango de 1 a 101 cada i^2 solo si se cumple la condición de que no sea divisible por 3.

### Reto

Crear, con un list comprehension, una lista de todos los múltiplos de 4 que a su vez son múltiplos del 6 y del 9 hasta 5 digitos.

```python
def run():

    challenge = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(challenge)

if __name__ == "__main__":
    run()
```

[![18](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/18.png?raw=true "18")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/18.png?raw=true "18")

## Dictionary comprehensions

Son una forma de almacenar elementos tal como lo haría en una lista de Python. Pero, en lugar de acceder a los elementos usando su índice, le asigna una clave fija y accede al elemento usando la clave. Lo que ahora trata es un par "clave-valor", que a veces es una estructura de datos más apropiada para muchos problemas en lugar de una simple lista.

Para entender el concepto vamos a escribir diccionario con llaves de los números del 1 al 100, que como valores tengas los mismos números, pero elevados al cubo y con la condición de que no sean divisibles por el número 3:

```python
def run():
     my_dict = {}

     for i in range(1, 101):
         if i % 3 != 0:
             my_dict[i] = i**3

if __name__ == "__main__":
    run()
```

[![19](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/19.png?raw=true "19")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/19.png?raw=true "19")

Esto se puede realizar en tan solo una línea con la siguiente estructura:

```python
def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

     my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

     print(my_dict)

if __name__ == "__main__":
    run()
```

### Estructura de dict comprehensions

[![20](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/20.png?raw=true "20")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/20.png?raw=true "20") [![21](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/21.png?raw=true "21")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/21.png?raw=true "21")

> - En mi nuevo diccionario guardaré para cada elemento en el iterable voy a colocar una llave y un valor solo si se cumple la condición.
> - En mi diccionario para cada i en el rango de 1 a 101 voy a guardar ese número como llave y el nùmero^2 solo si se cumple la condición de que no sea divisible por 3.

### Reto

Crear, con un dictionary comprehension, un diccionario cuyas llaves sean los 1000 primeros números naturales con sus raices cuadradas como valor.

```python
def run():
    
    challenge = { i: i**0.5 for i in range(1, 1001) }

    print(challenge)


if __name__ == "__main__":
    run()
```

[![22](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/22.png?raw=true "22")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/22.png?raw=true "22")

# Conceptos avanzados de funciones

## Funciones anónimas: lambda

- Son funciones que no tienen un identificador (nombre), retornan un objeto de tipo función que guardaremos en una variable.
- No necesitan la palabra clave return

[![23](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/23.png?raw=true "23")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/23.png?raw=true "23")

[![24](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/24.png?raw=true "24")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/24.png?raw=true "24")

## Hight order functions (Funciones de orden superior): filter, map and reduce

- `filter` Recorre toda la lista para devolver uno o varios elementos de esta. Devuelve True or False según el valor esté dentro de los criterios buscados o no.

 Pasar array a solo numeros impares.
 
[![25](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/25.png?raw=true "25")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/25.png?raw=true "25")

Usando función filter:

[![26](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/26.png?raw=true "26")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/26.png?raw=true "26")

- `map` Recorre toda la lista, la modifica y devuelve la misma lista, pero modificada. Sirve parar realizar una operación a todos los elementos de la lista uno a uno y devolver la lista con sus valores modificados.

 Elevar al cuadrado los elementos del array.
 
[![27](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/27.png?raw=true "27")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/27.png?raw=true "27")

Usando función map:

[![28](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/28.png?raw=true "28")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/28.png?raw=true "28")

- `reduce` No devuelve una lista, devuelve un valor haciendo una operación con todos los elementos. Sirve para hacer acumulaciones de los elementos de una lista.

 Multiplicar 2 x 2 x 2… hasta obtener 32.
 
[![29](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/29.png?raw=true "29")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/29.png?raw=true "29")

Usando la función reduce, la cual requiere que la importemos del módulo functools:

[![30](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/30.png?raw=true "30")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/30.png?raw=true "30")

reduce toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

## Proyecto: filtrando datos

Teniendo como base un diccionario con los datos de nombre, edad, organización, cargo y lenguaje de algunas personas procederemos a la siguiente función:

```python
DATA = [ #al estar en mayusculas no es variable sino constante
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
.
.
.
```

Se utiliza list comprehension para extraer nombre de desarrolladores de Python en DATA:

```python
def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    for worker in all_python_devs:
        print(worker)  

if __name__ == "__main__":
    run()
```
[![31](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/31.png?raw=true "31")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/31.png?raw=true "31")

Ahora lo utilizamos para extraer el nombre de las personas que trabajan en Platzi:
```python
def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    for worker in all_Platzi_workers:
        print(worker)  

if __name__ == "__main__":
    run()
```
[![32](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/32.png?raw=true "32")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/32.png?raw=true "32")

Se practica combinaciones de filter y map para extraer el nombre de los que son adultos de DATA:
```python
def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    for worker in adults:
        print(worker)

if __name__ == "__main__":
    run()
```
[![33](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/33.png?raw=true "33")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/33.png?raw=true "33")

Como último paso se utilizan la suma de diccionario nuevo con el símbolo **|** para diccionarios y **+**, donde para cada uno de los trabajadores dentro de DATA para cada diccionario voy a guardar ese mismo diccionario, pero sumado a otro que contiene la llave **"old"** con la función de evaluar la expresión **"age"** > 70. Si es correcto guarda True de lo contrario False.

```python
def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)  

if __name__ == "__main__":
    run()
```
[![34](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/34.png?raw=true "34")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/34.png?raw=true "34")

### Reto 

- Crear las listas *all_python_devs*  y *all_Platzi_workers* usando una combinación de **filter** y** map**.
- Crear una lista *old_people* y *adults* con **list comprehensions**.

```python
def main():
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)


if __name__ == "__main__":
    main()
```

# Manejo de errores

## Los errores en el código

Cuando Python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como **traceback**, puede ser debido a:

- **Errores de Sintaxis (SyntaxError)** → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
- **Excepciones (Exeption)** → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, también pueden generarse dentro del código o fuera del (elevar una excepción).

[![35](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/35.png?raw=true "35")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/35.png?raw=true "35")

- **Keyboard Interrupt:** Ocurre cuando pulsamos Ctrl + C en la consola interactiva de Python y esto detiene el flujo de ejecución del programa.
- **KeyError:** Cuando intentamos acceder a una llave (key) que no existe en un diccionario.
- **IndexError:** Causada cuando estamos trabajando con listas e intentamos acceder a un index (índice) de esa lista que no existe.
- **FileNotFoundError:** Se origina al intentar abrir un archivo que no existe.
- **ZeroDivisionError:** Se genera este error cuando intentamos dividir un número entre cero.
- **ImportError:** cuando queremos importar un módulo y hay algún error en ese módulo.
 Obtenemos información del error a través del traceback. Lo correcto es leer desde el final hasta el principio.

Ejemplo del tipo de información que arroja el traceback.

- **Lectura de un Traceback:** La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
En el caso de excepciones la última línea nos indicará el tipo de excepción que se generó (generalmente son auto explicativas, pero si no entiendes que paso puedes buscar este error)
La penúltima línea nos indicará donde se encuentra el error (archivo y línea)
La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se generó un error)

- **Elevar una excepción:** Cuando tenemos una excepción en Python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback.

Estos son los errores y excepciones de la documentación oficial de Python:
[https://docs.python.org/es/3/tutorial/errors.html](https://docs.python.org/es/3/tutorial/errors.html "https://docs.python.org/es/3/tutorial/errors.html")

## Debugging ó Depuración

Es una herramienta que traen varios editores de código con el objetivo de solucionar nuestros errores de lógica, revisemos la herramienta debugging de VS Code. Para esto se crea el siguiente código con el fin de imprimir los divisores del número que se le pide al usuario:

```python
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("Terminó mi programa")


if __name__ == "__main__":
    run()
```

Como se observa al ejecutar imprime números errados que no sirven:

[![36](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/36.png?raw=true "36")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/36.png?raw=true "36")

Para realizar el debugging en el editor seleccionamos opción **Run and Debug** y selecciona en la lista desplegable **Python File**:

[![37](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/37.png?raw=true "37")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/37.png?raw=true "37")

[![38](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/38.png?raw=true "38")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/38.png?raw=true "38")

En este entorno podemos acceder a funcionalidades como:

- **pause** → permite pausar la ejecución del programa
- **step over** → permite avanzar un solo paso en el programa
- **step in** → ingresamos a un bloque secundario del programa (funciones)
- **step out** → salimos del bloque secundario
- **restart** → reinicia el programa
- **stop** → detiene el programa

Se abre terminal donde permite ejecutar nuestro código, pero antes de escribir el número se pausa la secuencia, esto permitirá revisar paso por paso cada línea al ejecutarse dando **step over**:

[![39](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/39.png?raw=true "39")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/39.png?raw=true "39")

A medida que avanzamos en cada línea aparece la información de las variables involucradas y sus valores actuales:

[![40](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/40.png?raw=true "40")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/40.png?raw=true "40")

Estos pasos nos facilita la tarea de buscar el error que no nos informa Python, en este caso es que en la condición if, el residuo debe ser igual a cero para poder encontrar los números divisores.

Además, podemos generar **breakpoints** que son los puntos rojos en los que el programa se detendrá para ayudarnos a depurar el código, están ubicados a la izquierda de la numeración de cada línea de código:

[![41](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/41.png?raw=true "41")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/41.png?raw=true "41")

[![42](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/42.png?raw=true "42")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/42.png?raw=true "42")

## Manejo de excepciones

- **try except** → Anidamos nuestro programa en dos bloques de código, el primero es el programa per se (el que se ejecuta normalmente, sin errores) y el segundo representa las instrucciones a seguir en caso de error.

[![43](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/43.png?raw=true "43")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/43.png?raw=true "43")

- **raise** → Esta instrucción nos permite generar errores, es decir crear nuestros propios errores cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos.

[![44](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/44.png?raw=true "44")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/44.png?raw=true "44")

- **finally **→ Es un bloque de código que se ejecuta exista un error o no (un tercer bloque después de try except), no es muy usual, pero puede darse para cerrar archivos, conexiones a BBDD o liberar recursos.

[![45](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/45.png?raw=true "45")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/45.png?raw=true "45") [![46](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/46.png?raw=true "46")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/46.png?raw=true "46")

## Poniendo a prueba el manejo de excepciones

Vamos a probar las excepciones con nuestro archivo **debugging.py**, probando si acepta un string pero nos muestra el siguiente **Traceback**:

[![47](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/47.png?raw=true "47")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/47.png?raw=true "47")

Se agregan los comandos **try** y **except** como se muestra en la imagen, para cuando se introduzcan strings se va devolver mensaje **"Debes ingresar un número":**

```python
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")

if __name__ == "__main__":
    run()
```

[![48](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/48.png?raw=true "48")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/48.png?raw=true "48")

### Reto

Utiliza las palabras clave **try, except** y **raise** para elevar un error si el usuario ingresa un npumero negativo en nuestro programa de divisores.

```python
def run(num):
    divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0]

    while True:
        try:
            num = int(input("Ingresa un número: "))
            if num < 0:
                raise Exception("Debes ingresar un número positivo")
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un número")
        except Exception:
            print("Debes ingresar un número positivo")

if __name__ == "__main__":
    run()
```

[![49](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/49.png?raw=true "49")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/49.png?raw=true "49")

## Assert statements

Es otra alternativa para el manejo de las excepciones en nuestro código.

> Afirmo que esta condición es cierta, de lo contrario, manda este mensaje de error.

[![50](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/50.png?raw=true "50")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/50.png?raw=true "50")

[![51](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/51.png?raw=true "51")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/51.png?raw=true "51")

Este es el orden en que se utilizaría el comando assert.

[![52](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/52.png?raw=true "52")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/52.png?raw=true "52")

[![53](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/53.png?raw=true "53")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/53.png?raw=true "53")

Como ejemplo se utiliza el código anterior, pero con el nuevo comando:	

```python
def run():
    divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0]

    num = input("Ingresa un número: ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un número positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")

if __name__ == "__main__":
    run()
```

Nos devuelve un mensaje **AssertionError** junto con todo un Traceback con los errores presentes:

[![54](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/54.png?raw=true "54")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/54.png?raw=true "54")

# Manejo de archivos

## ¿Cómo trabajar con archivos?

En los diferentes lenguajes de programación podremos trabajar con los archivos de texto (De color gris), pero es más complicado trabajar con los archivos binarios ya que trabajan con imágenes, videos, … (Color verde).

[![55](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/55.png?raw=true "55")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/55.png?raw=true "55")

Existen varias extensiones de archivos con los que podemos interactuar con python (js,csv,py,css,json,xml).

Para abrir un archivo seguimos la siguiente estructura:

`with open(<ruta>, <modo_apertura>) as <nombre>`

[![56](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/56.png?raw=true "56")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/56.png?raw=true "56")

- **with** Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)
- **open(ruta, modo_apertura)** Es una función que necesita de dos parámetros
- **ruta** Es donde se encuentra nuestro archivo en nuestro equipo
- **modo_de_apertura** Como vamos a abrir el archivo, los modificadores son:
 **r** → modo de lectura
 **w** → modo de escritura (sobreescribe el archivo)
 **a** → modo append (añade información al final del archivo)
- **as (nombre)** Nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer

## Trabajando con archivos de texto en Python

Creamos archivo .py con el siguiente código que cuenta dos funciones: una para leer y otra para escribir. Para ejecutar la función de leer utilizamos la línea aprendida para manejar archivos teniendo en cuenta que primero se creó archivo **numbers.txt** con números los cuales vamos a leer e imprimir:

`encoding = "utf-8"` Sirve para que Python pueda soportar caracteres del idioma español, como la **ñ** y letras con tilde.

```python
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Fausto", "Miguel", "Pepe", "Chirstian", "Rocio"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n") #Salto de línea en Python

def run():
    read-()

if __name__ == "__main__":
    run()
```

[![57](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/57.png?raw=true "57")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/57.png?raw=true "57")

[![58](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/58.png?raw=true "58")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/58.png?raw=true "58")

Para la función de escribir se hace lista con diferentes nombres y queremos que se cree un nuevo archivo **names.txt** con los nombres escritos con saltos de línea, para esto establecemos el **modo de apertura “w"** para escribir o sobre escribir:

```python
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Facundo", "Miguel", "Pepe", "Chirstian", "Rocio"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n") #Salto de línea en Python

def run():
    write()

if __name__ == "__main__":
    run()
```

[![59](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/59.png?raw=true "59")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/59.png?raw=true "59")

Si queremos añadir información al final del archivo utilizamos el **modo append “a":**

```python
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Andrés", "José", "Luis", "Sofia", "Catalina"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n") #Salto de línea en Python

def run():
    write()

if __name__ == "__main__":
    run()
```

[![60](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/60.png?raw=true "60")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/60.png?raw=true "60")

## Reto final: Juego del Ahorcado o Hangman Game

**Ayudas y pistas**

- Investiga la función **enumerate.**
- El método **get** de los diccionarios puede servirte.
- La sentencia

   `os.system("cls")` -> Windows
   
   `os.system("clear")`  -> Unix
   
  te servirá para limpiar la pantalla.

**Mejora el juego**

- Añade un sistema de puntos.
- Dibuja al "ahoracado" en cada jugada con **código ASCII.**
- Mejora la interfaz.

Debido al tamaño del código no se escribe acá, pero se puede encontrar el código del reto Hangman Game en mi repositorio Git Hub:

[https://github.com/hackmilo/HangmanGame-JuegoAhorcado.git](https://github.com/hackmilo/HangmanGame-JuegoAhorcado.git "https://github.com/hackmilo/HangmanGame-JuegoAhorcado.git")

Como muestra del resultado podemos ver algunas de las pantallas en diferentes situaciones del juego:

Menú de inicio:

[![61](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/61.png?raw=true "61")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/61.png?raw=true "61")

Hangman Game:

[![62](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/62.png?raw=true "62")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/62.png?raw=true "62")

Ganador interfaz:

[![63](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/63.png?raw=true "63")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/63.png?raw=true "63")

Perdedor interfaz:

[![64](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/64.png?raw=true "64")](https://github.com/hackmilo/Notas---Curso-intermedio-de-Python/blob/main/img/64.png?raw=true "64")


