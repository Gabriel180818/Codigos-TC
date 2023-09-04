#include <stdio.h>

int collatz(int n) {
    if (n % 2 == 0) {//par
        return n / 2;
    } else {//impar
        return 3 * n + 1;
    }
}

int main() {
    int num;
    printf("Ingresa un numero: ");
    scanf("%d", &num);

    printf("Serie de Collatz para %d:\n", num);
    while (num != 1) {
        printf("%d -> ", num);
        num = collatz(num);
    }
    printf("1\n");

    return 0;
}

