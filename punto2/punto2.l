%{
#include <stdio.h>

int flag = 0;  // Bandera para indicar si se reconoce la expresión lambda
%}

%%

# Ignorar espacios y tabulaciones
[ \t]+               ;

# Identificadores (nombres de variables o funciones)
[a-zA-Z_][a-zA-Z0-9_]* { /* Coincide con nombres de variables o funciones */ }

# La palabra clave lambda
lambda               { /* Coincide con la palabra lambda */ }

# El operador de asignación
"="                  { /* Coincide con el operador de asignación */ }

# El símbolo de dos puntos que separa los parámetros del cuerpo de la lambda
":"                  { /* Coincide con el símbolo ":" en la expresión lambda */ }

# Operadores matemáticos
"**"                 { /* Coincide con el operador de exponenciación */ }

# Cualquier número entero
[0-9]+               { /* Coincide con un número entero */ }

# Paréntesis para las llamadas a funciones
"(" | ")"            { /* Coincide con paréntesis */ }

# Comas
","                  { /* Coincide con comas */ }

# Coincidir la expresión lambda en su totalidad
[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"="[ \t]*"lambda"[ \t]*"("[a-zA-Z_][a-zA-Z0-9_]*"[ \t]*")"[ \t]*":"[ \t]*[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"**"[ \t]*[0-9]+ {
    flag = 1; // Si se detecta la expresión completa, activar la bandera
}

.                     ;  // Cualquier otro carácter

%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s <archivo de entrada>\n", argv[0]);
        return 1;
    }

    // Abrir el archivo de entrada
    FILE *archivo = fopen(argv[1], "r");
    if (!archivo) {
        printf("Error al abrir el archivo %s\n", argv[1]);
        return 1;
    }

    // Establecer la entrada de lex en el archivo
    yyin = archivo;

    // Ejecutar el analizador léxico
    yylex();

    // Comprobar si se encontró la expresión lambda
    if (flag) {
        printf("ACEPTA\n");
    } else {
        printf("NO ACEPTA\n");
    }

    // Cerrar el archivo
    fclose(archivo);

    return 0;
}
