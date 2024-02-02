def numero_a_palabras(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales_diez_a_veinte = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if 0 <= numero <= 99:
        if numero < 10:
            return unidades[numero]
        elif 10 <= numero <= 19:
            return especiales_diez_a_veinte[numero - 10]
        else:
            decena = numero // 10
            unidad = numero % 10
            return f"{decenas[decena]} {'y' if unidad != 0 else ''} {unidades[unidad]}"
    else:
        return "Número fuera de rango. Debe ser entre 0 y 99."

def obtener_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero entre 0 y 99: "))
            return numero
        except ValueError:
            print("Error: Ingresa un numero valido.")

def main():
    try:
        numero = obtener_numero()
        palabras = numero_a_palabras(numero)
        print(f"El número {numero} se escribe como: {palabras}")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
