#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 1024

void to_lowercase(char *str) {
    while (*str) {
        *str = tolower((unsigned char) *str);
        str++;
    }
}

int count_occurrences(const char *line, const char *keyword) {
    int count = 0;
    const char *p = line;

    while ((p = strstr(p, keyword)) != NULL) {
        count++;
        p += strlen(keyword); 
    }

    return count;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Uso: %s <archivo> <palabra clave>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    char keyword[256];
    char line[MAX_LINE_LENGTH];
    FILE *file = fopen(filename, "r");
    int total_count = 0;

    strncpy(keyword, argv[2], sizeof(keyword) - 1);
    keyword[sizeof(keyword) - 1] = '\0'; 
    to_lowercase(keyword);

    if (!file) {
        perror("Error al abrir el archivo");
        return 1;
    }

    while (fgets(line, sizeof(line), file)) {
        to_lowercase(line);
        total_count += count_occurrences(line, keyword);
    }

    fclose(file);

    printf("%s se repite %d veces en el texto.\n", argv[2], total_count);

    return 0;
}