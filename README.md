# poo en python
introducción a la programación orientada a objetos (POO) en python

## ¿por qué aprender POO?

- Imagina que quieres crear un video juego. Tienes guerros, magos, fragones... cada uno con sus propios puntos de vida, ataques y habilidades. ¿cómo los organizo en código sin repetir todo una y otra vez?

- La **Programación orientada a objetos (POO)** es la respuesta. En lugar de escribir instrucciones sueltas,modelas el mundo real con *objetos* que tienen caracteristicas y comportamientos. Es la forma en que estan construidos la mayoria de los programas profesionales del mundo.

![POO](img/poo.png)("POO")

## Clase y objetos

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancia.

- La clase es la definición del concepto del mundo real y losobjetos o instancias son el propio "objeto" del mundo real.

- Las clases estan compuestas por dos elementos:
     - **Atributos:** informacion que almacena la clase.
     - **Métodos:** operaciones que pueden realizarse con las clase.

## Definición de una clase en python

``` python
class NombreClase:

    def __init__(self, variable1, variable2):
        self.atributo1 = valor1
        self.atributo2 = valor2

    def nombreMetodo(self):
        BloqueCodigo
```

- `class`: palabra reservada en python para definir una clase.
- NombreClase`: nombre de la clase que se quiere crear.
- `def` : palabra reservada en python que se utiliza para definir tanto el constructor de la clase (método que se ejecuta la primera vez que usas clase) como los diferentes métodos que tiene.
- `__init__`: palabra reservada en python para definir el metodo constructor de la clase. El metodo `__init__` es lo primero que se ejecuta cuando creas un objeto de una clase.
- `(self, variablex)`: parametro del constructor de la clase. El parameto `self` es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.
- `self.Atributox`: forma de utilizacion y acceso a los atributos de la clase.
- `nombreMetodo`: nombre del metodo de la clase.
- `self`: parametro del metodo. El parametro `self`es obligatorio y despues puedes tener  tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.
- `BloqueCodigo`: instrucciones que ejecutara el metodo.

**Al definir una clase en cuenta:**
- Puedes definir tantos atributos como necesites.
- Puedes definir tantos metodos como necesites.
- Puedes definir tantos parametros en el constructor y en los metodos como necesites.

## Ejemplo 1

- Crear una clase que represente una persona.
- Atributos: nombre, apellidos y edad.
- Métodos: mostrar la informacion de las personas.

### Código

```python
class Persona:

    # Método constructor de la clase
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    # Metodo para mostrar la informacion
    def mostrarpersona(self):
        print("nombre: ",self.nombre)
        print("apellidos: "self.apellidos)
        print("edad: "self.edad)

def main():
    print("Vamos a aprender POO...")
    persona_1 = Persona("Lorenzo", "Perez", 18)
    persona_1.mostrarPersona()

    if __name__ == main():
        main()
```

## Representación en RAM del objeto creado

![Objeto RAM](img/objetoRam.jpeg "Objeto RAM")


## composición

- Consiste en la creacion de nuevas  clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva.
- Las clases existentes seran atributos de la nueva clase.

### Ejemplo

- Una coordenada en dos dimensiones esta compuesta por dos valores, el valor en el eje de las X y el valor en el eje de las Y. Esto podria ser una clase
- Un cuadrado esta compueszto por 4 coordenadas que son los cuatro vertices. Esto podria ser una clase que estacompuesta por cuatro clases del objeto coordenada.

### Código python
```python
class Coordenada:
    # Metodo constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    
    def mostrarCoordenada(self):
        print("(",self.X,",",self.Y,")")

class Cuadrado:
    # Método constructor
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices:")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()
```
## Representación en RAM de la composicion

![Objeto RAM](img/cordenadas.png "Objeto RAM")

## Encapsulación

- Uno de los objetivos que tiene la POO es proteger los datos de acceso o usos no controlados, y esto es lo que se conoce como **encapsulacion**.
- Los datos (atributos) que componen una clase pueden ser de dos tipos:
    - **Públicación:** los datos son accesibles sin control, es decir,los datos pueden ser usados sin ningun tipo de mecanismo que protega ante usos no autorizados o indebidos.
    - **Privados:** los datos no pueden ser accedidos sin control y para acceder a ellos se debera inplementar un metodo que acceda a ellos. De esta manera, los datos unicamente seran accedidos directamente por la propia clase.
    - La encapsulacion tambien puede realizarse sobre los metodos.
    - La definicion de atributos privados se realiza incluyendo los caracteres"__" (dos guiones de piso) entre la palabra *self* y el nombre del atributo.

### Ejemplo 

### Codigo python

class coordenada:
    # Metodo constructor
    def__init__(self, x, y):
        self.__x = x
        self.__y = y

    # Metodo de acceso 
    def getX(self):
        return self.__x

    def setX(self,X):
        self.__X = X

    def getY(self):
        return self.__Y

    def setY(self, Y):
        self.__Y = Y

    def mostrarcoordenada(self):
        print("(",self.__x,",",self.__y,")")

class Cuadrado:
    def__init__(self,v1,v2,v3,v4)
    self.v1 = v1
    self.v2 = v2
    self.v3 = v3
    self.v4 = v4

    def mostrarvertices(self):
        print("el cuadrado esta compuesto por los siguientes vertices:")
        self.v1.mostrarcoordenada()
        self.v2.mostrarcoordenada()
        self.v3.mostrarcoordenada()
        self.v4.mostrarcoordenada()


## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ```class NombreClase(ClaseBase):```
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono