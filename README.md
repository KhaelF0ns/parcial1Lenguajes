# parcial1Lenguajes

En este repositorio se lleva a cabo el parcial de corte 1 para la materia de Lenguajes de Programación presentado por __Mateo Fonseca__. Para ver la ejecución, debe ingresar con el comando `cd` a la carpeta del punto de su interés:

## Punto 1:

El programa debe recibir como parámetro una expresión regular y debe devolver su token.

Expresiones que acepta el programa:

- \+
- \++
- [0-9]+
- ([0-9]+)”.”([0-9])+

Ejemplo: si se ejecuta el programa:

```sh
python3 punto1AFD.py +
```

Desde la consola debe imprimir `SUMA`

## Punto 2:

El programa debe recibir un archivo de texto como parámetro de entrada y debe devolver (imprimir) si se acepta o no la expresión. Si el archivo.txt contine:

```
square = lambda x: x ** 2
print(square(3))
```

La salida debe ser:

```
ACEPTA
NO ACEPTA
```

Para ejecutar el programa:

### Paso 1: Ejecute la siguiente línea para procesar el archivo de definición de análisis léxico:

```sh
flex punto2.l
```

### Paso 2: Compile el archivo de C resultante:

```sh
gcc lex.yy.c -lfl
```

### Paso 3: Ejecute el programa resultante `a.out`:

```sh
./a.out archivo.txt
```

## Punto 3:

El programa debe recibir un archivo de texto y una palabra clave de búsqueda en el texto. Retorna la cantidad de coincidencias que tiene el texto con la palabra clave.

Ejemplo:

```sh
cuentaPalabras.c ejemplo.txt key
```

Si `key = arroz` retorna: 

```
arroz se repite 10 veces en el texto.
```

## Punto 4:

El programa analiza un archivo de texto con 1000 números enteros aleatorios de 1 a 1000 y diga cuales números son primos. Para generar los números de forma aleatoria ejecute:

```sh
python3 aleatorios.py
```

Esto creará un archivo llamado `números.txt` con 1000 números entre 1 y 1000. Luego de permisos de ejecución al archivo `awk`:

```sh
chmod +x punto4.awk
```

Y por último, ejecute el archivo con `numeors.txt` como parámetro:

```sh
./punto4.awk numeros.txt
```

## Punto 5: 

Para instalar `pip`:

```sh
sudo apt install python-pip
```

Activar el entorno virtual:

```sh
source .venv/bin/activate
```

**Nota**: Si no tiene entorno virtual:

```sh
pip install virtualenv
```

### Paso 1: Instale las dependencias del programa:

```sh
pip install -r requirements.txt
```

### Paso 2: Compile la gramatica in `Python`:

```sh
antlr4 -visitor -Dlanguage=Python3 punto5TrigCalc.g4
```

### Paso 3: Ejecute el archivo de prueba:

```sh
python3 main.py expr.in
```

### Paso 4: Ejecute la calculadora con sus propias expresiones trigonométricas:

```sh
python3 calc.py
```

Y luego escriba la expresión.
