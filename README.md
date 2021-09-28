# Notas - Curso intermedio de Python
Profesor Facundo Garcia Martoni de Platzi.

![](https://static.platzi.com/media/avatars/Platzi-f730e65b-e92b-44d3-81c0-5c59c4dc4658.png) ![](https://static.platzi.com/media/learningpath/badges/46.png) ![](https://static.platzi.com/media/achievements/badge-intermedio-de-python-d0d16518-5edd-450a-b2a9-0710bded1494.png)


## Tabla de Contenidos

- [Introducción](#introducción)
  - [¿Por qué Python?](#por-qué-python)
  - [¿Que es un algoritmo?](#que-es-un-algoritmo)

# Introducción

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

## Hight order functions (Funciones de orden superior): filter, map and reduce.

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

