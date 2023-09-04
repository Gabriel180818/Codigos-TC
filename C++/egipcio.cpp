#include<stdio.h>

int main() {
    int num1, num2;
    printf("Ingrese el primer numero: ");
    scanf("%d", &num1);
    printf("Ingrese el segundo numero: ");
    scanf("%d", &num2);

    int col1 = num1;
    int col2 = 1;
    printf("COLUMNA1\tCOLUMNA2\n");
    while (col2 <= num2 ) {
        col1 *= 2;
        col2 *= 2;
        
        printf("%d\t\t",col1);
        printf("%d\n",col2);
    }
    printf("\n\nNumeros a sumar\n\n");
    int sum = 0;
    while (col2 > 0) {
        if (col2 <= num2) {
        	printf("%d\t\t",col1);
        	printf("%d\n",col2);
            sum += col1;
            num2 -= col2;
        }
        col1 /= 2;
        col2 /= 2;
    }

    printf("El resultado de la multiplicacion es: %d\n", sum);

    return 0;
}
