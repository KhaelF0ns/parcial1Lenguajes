#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Convierte una cadena a minúsculas
void to_lowercase(char *str) {
    while (*str) {
        *str = tolower((unsigned char)*str);
        ++str;
    }
}

// Cuenta las ocurrencias de 'key' en 'line'
int count_occurrences(const char *line, const char *key) {
    int count = 0;
    const char *pos = line;
    size_t keyword_len = strlen(key);

    while ((pos = strstr(pos, key)) != NULL) {
        ++count;
        pos += keyword_len; 
    }

    return count;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Uso: %s <archivo> <palabra clave>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    char *key;
    char *line = NULL;
    size_t line_size = 0;
    FILE *file;
    int total_count = 0;

    // Aloca memoria para la palabra clave
    key = malloc(strlen(argv[2]) + 1);

    // Copia la palabra clave y conviértela a minúsculas
    strcpy(key, argv[2]);
    to_lowercase(key);

    // Abre el archivo
    file = fopen(filename, "r");
    if (!file) {
        perror("Error al abrir el archivo");
        free(key);
        return 1;
    }

    // Lee y procesa cada línea
    while (getline(&line, &line_size, file) != -1) {
        to_lowercase(line);
        total_count += count_occurrences(line, key);
    }

    free(line);
    free(key);
    fclose(file);

    printf("'%s' se repite %d veces en el texto.\n", argv[2], total_count);

    return 0;
}
