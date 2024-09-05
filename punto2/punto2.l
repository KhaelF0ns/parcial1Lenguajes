%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int line_number = 0;
%}

/* Definición de macros para los patrones */
ID                      [a-zA-Z_][a-zA-Z0-9_]*
ENTERO                  [0-9]+
OPS                     \*\*|\+|\-|\*|\/
ASIGNACION              =
DOS_PUNTOS              :
PARENTESIS_IZQUIERDO    \(
PARENTESIS_DERECHO      \)
ESPACIOS                [ \t]*
COMA                    ,
LAMBDA                  lambda{ESPACIOS}{ID}({ESPACIOS}{COMA}{ESPACIOS}{ID})*{ESPACIOS}{DOS_PUNTOS}{ESPACIOS}[^;]*

%%

{LAMBDA}                                        { printf("ACEPTA\n"); }
{ID}{ESPACIOS}{ASIGNACION}{ESPACIOS}{LAMBDA}    { printf("ACEPTA\n"); }
[ \t]*\n                                        { }
.+                                              { printf("NO ACEPTA\n"); }

%%

int yywrap() {
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s <archivo.txt>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("No se pudo abrir el archivo");
        return 1;
    }

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, file)) != -1) {
        if (line[read - 1] == '\n') {
            line[read - 1] = '\0';
        }

        yy_scan_string(line);
        yylex();
    }

    free(line);
    fclose(file);
    return 0;
}
