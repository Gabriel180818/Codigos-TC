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
    pasos = []
    producto = 0 

    while a > 0:
        if a % 2 == 1:
            pasos.append(f"{a} x {b} = {b}")
            producto += b
        pasos.append(f"{a} / 2 = {a // 2}")
        a = a // 2
        b = b * 2

    return producto, pasos
def mostrarmultegipcia(a,b):
  resultado, pasos = multiplicacionegipcia(a, b)
  print(f"Resultado de {a} x {b} usando multiplicación egipcia: {resultado}")
  print("Pasos intermedios:")
  for paso in pasos:
    print(paso)
def multiplicacionrusa(a, b):
    pasos = []  # Lista para almacenar los pasos intermedios
    producto = 0  # Inicializa el producto en cero

    while a > 0:
        if a % 2 == 1:
            pasos.append(f"{a} x {b} = {b}")
            producto += b
        pasos.append(f"{a} // 2 = {a // 2}")
        pasos.append(f"{b} * 2 = {b * 2}")
        a = a // 2
        b = b * 2

    return producto, pasos
def mostrarrusa(a, b):
    resultado, pasos = multiplicacionrusa(a, b)
    print(f"Resultado de {a} x {b} usando multiplicación rusa: {resultado}")
    print("Pasos intermedios:")
    for paso in pasos:
        print(paso)
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
            multiplicacionegipcia(a, b)
            mostrarmultegipcia(a, b)
           
        elif choice == 4:
            a = int(input("Ingrese el primer número para la multiplicación rusa: "))
            b = int(input("Ingrese el segundo número para la multiplicación rusa: "))
            multiplicacionrusa(a, b)
            mostrarrusa(a, b)
        elif choice == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()