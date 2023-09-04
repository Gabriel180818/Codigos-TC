#include <stdio.h>
#include<windows.h>


int multiplicacionRusa(int a, int b) {
    int res = 0;
    printf("\nDivision  Duplicacion\n");
    while (a > 0) {
        if (a % 2 == 1) {//comprueba si son impares
           SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),3);
            res += b;
            printf("%d\t\t",a);
        	printf("%d\n",b);
        }else{
        	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
        	printf("%d\t\t",a);
            printf("%d\n",b);
	  }
        a /= 2;//divide
        b *= 2;//duplica
        
    }
    return res;
}

int main() {
    int num1, num2;
    printf("Ingrese dos numeros para multiplicar:\n ");
    printf("Numero 1: ");
    scanf("%d",&num1);
    printf("Numero 2: ");
    scanf("%d",&num2);

    int res = multiplicacionRusa(num1, num2);
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),15);
    printf("\n\n	Resultado: %d x %d = %d\n", num1, num2, res);

    return 0;
}
