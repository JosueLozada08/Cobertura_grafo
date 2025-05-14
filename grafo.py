def flujo_control(a, b, c):
    resultado = ""

  
    if a > 0:
        if b > 0:
            resultado += "R1-"
        else:
            resultado += "R2-"
    else:
        if c > 0:
            resultado += "R3-"
        else:
            resultado += "R4-"

    if a + b + c > 5:
        resultado += "R5-"
    else:
        resultado += "R6-"


    if a == b:
        resultado += "R7"
    else:
        resultado += "R8"

    return resultado



def pruebas():
    print("Caso 1: a=1, b=1, c=0")      # R1–R5–R8
    print("Salida:", flujo_control(1, 1, 0))
    print()

    print("Caso 2: a=1, b=-1, c=2")    # R2–R6–R8
    print("Salida:", flujo_control(1, -1, 2))
    print()

    print("Caso 3: a=-1, b=0, c=2")    # R3–R6–R8
    print("Salida:", flujo_control(-1, 0, 2))
    print()

    print("Caso 4: a=-1, b=0, c=-1")   # R4–R6–R8
    print("Salida:", flujo_control(-1, 0, -1))
    print()

    print("Caso 5: a=2, b=2, c=2")     # R1–R5–R7
    print("Salida:", flujo_control(2, 2, 2))
    print()


if __name__ == "__main__":
    pruebas()

