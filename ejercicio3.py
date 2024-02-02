import math

PI = 3.1416

def calcular_area_circulo(radio):
    if radio <= 0:
        raise ValueError("El radio debe ser un número positivo mayor que cero.")
    else:
        area = PI * (radio ** 2)
        return area

def obtener_radio():
    while True:
        try:
            radio = float(input("Ingrese el valor del radio del círculo: "))
            return radio
        except ValueError:
            print("Error: Ingresa un número válido para el radio.")

def main():
    try:
        radio = obtener_radio()
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {area}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
