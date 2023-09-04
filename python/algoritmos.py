def collatz_conjectura(n):
    sequencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia


def kaprekar_constante(n):
    def kaprekar_iteracion(num):
        num_str = str(num).zfill(4)
        ascender = int(''.join(sorted(num_str)))
        descender = int(''.join(sorted(num_str, reverse=True)))
        return descender - ascender

    sequencia = [n]
    while n != 6174:
        n = kaprekar_iteracion(n)
        sequencia.append(n)
    return sequencia


def multiplicacionegipcia(a, b):
    productos = []
    while a > 0:
        if a % 2 == 1:
            productos.append(b)
        a //= 2
        b *= 2
    return sum(productos)


def multiplicacionrusa(a, b):
    resultado = 0
    while a > 0:
        if a % 2 == 1:
            resultado += b
        a //= 2
        b *= 2
    return resultado


def main():
    while True:
        print("\nSeleccione una función:")
        print("1. Conjetura de Collatz")
        print("2. Constante de Kaprekar")
        print("3. Multiplicación Egipcia")
        print("4. Multiplicación Rusa")
        print("5. Salir")

        choice = int(input("Ingrese el número de la función que desea ejecutar: "))

        if choice == 1:
            n = int(input("Ingrese un número para la conjetura de Collatz: "))
            result = collatz_conjectura(n)
            print("Secuencia de Collatz:", result)
        elif choice == 2:
            n = int(input("Ingrese un número para la constante de Kaprekar: "))
            result = kaprekar_constante(n)
            print("Secuencia de Kaprekar:", result)
        elif choice == 3:
            a = int(input("Ingrese el primer número para la multiplicación egipcia: "))
            b = int(input("Ingrese el segundo número para la multiplicación egipcia: "))
            result = ultiplicacionegipcia(a, b)
            print("Resultado de la multiplicación egipcia:", result)
        elif choice == 4:
            a = int(input("Ingrese el primer número para la multiplicación rusa: "))
            b = int(input("Ingrese el segundo número para la multiplicación rusa: "))
            result = multiplicacionrusa(a, b)
            print("Resultado de la multiplicación rusa:", result)
        elif choice == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
