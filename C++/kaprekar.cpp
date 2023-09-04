#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
//metodo de burbuja para ordenamiento
void burbuja(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void kaprekar(int num) {

    while (num != 6174) {
        int digitos[4];
      //obtiene los digitos del numero entero para covertirlo en arreglo
        digitos[0] = num % 10;
        digitos[1] = (num / 10) % 10;
        digitos[2] = (num / 100) % 10;
        digitos[3] = (num / 1000) % 10;
	 // se ordena los numeros
        burbuja(digitos,4);
	//aqui se forman los numeros ya ordenados de manera ascendente y descendente multiplicando cada digito por una potencia de 10
        int asc = digitos[0] * 1000 + digitos[1] * 100 + digitos[2] * 10 + digitos[3];
        int desc = digitos[3] * 1000 + digitos[2] * 100 + digitos[1] * 10 + digitos[0];

        num = desc - asc;
       
        printf("%d - %d = %d\n\n",desc,asc,num);

    }

}

int main() {
    int num;
    printf("Ingrese un numero de 4 digitos: ");
    scanf("%d", &num);

    if (num < 1000 || num >= 10000) {
        printf("El numero debe tener 4 digitos\n");
    }else kaprekar(num);

    
    

    return 0;
}


