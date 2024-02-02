def es_multiplo_de_dos_y_tres(numero):
    if numero <= 0:
        raise ValueError("El número debe ser un entero positivo mayor que cero.")
    else:
        es_multiplo_de_dos = numero % 2 == 0
        es_multiplo_de_tres = numero % 3 == 0

        if es_multiplo_de_dos and es_multiplo_de_tres:
            return f"El número {numero} es múltiplo de 2 y 3."
        else:
            return f"El número {numero} no es múltiplo de 2 y 3."

def obtener_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Error: Ingresa un número entero válido.")

def main():
    try:
        numero = obtener_numero()
        resultado = es_multiplo_de_dos_y_tres(numero)
        print(resultado)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
