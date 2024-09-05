#!/usr/bin/awk -f

function es_primo(n) {
    if (n <= 1) return 0
    if (n <= 3) return 1
    if (n % 2 == 0 || n % 3 == 0) return 0
    i = 5
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) return 0
        i += 6
    }
    return 1
}

{
    for (i = 1; i <= NF; i++) {
        num = $i
        if (es_primo(num)) {
            print num
        }
    }
}
