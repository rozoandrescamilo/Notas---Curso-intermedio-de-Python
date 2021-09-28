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
