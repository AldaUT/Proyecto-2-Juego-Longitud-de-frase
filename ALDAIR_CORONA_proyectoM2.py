# Solicitar tres palabras con un mínimo de 4 caracteres y un maximo de 8 caracteres
# Se indican la cantidad de caracteres faltantes en caso de -4 o caracteres sobrantes en caso de +8
print("¡Juguemos a adivinar la palabra!")
while True:
    palabra1 = input("Introduce la primera palabra (mínimo 4 caracteres): ").upper()
    if len(palabra1) >= 4 and len(palabra1) <= 8:  # Validación si está en el rango de 4 a 8 letras
        print(f"¡Palabra correcta! La palabra tiene {len(palabra1)} letras.")
        break
    elif len(palabra1) < 4:
        print(f"Hacen falta letras. Solo tiene {len(palabra1)} letras.")
    else:
        print(f"Sobran letras. Tiene {len(palabra1)} letras.")

while True:
    palabra2 = input("Introduce la segunda palabra (mínimo 4 caracteres): ").upper()
    if len(palabra2) >= 4 and len(palabra2) <= 8:
        print(f"¡Palabra correcta! La palabra tiene {len(palabra2)} letras.")
        break
    elif len(palabra2) < 4:
        print(f"Hacen falta letras. Solo tiene {len(palabra2)} letras.")
    else:
        print(f"Sobran letras. Tiene {len(palabra2)} letras.")

while True:
    palabra3 = input("Introduce la tercera palabra (mínimo 4 caracteres): ").upper()
    if len(palabra3) >= 4 and len(palabra3) <= 8:
        print(f"¡Palabra correcta! La palabra tiene {len(palabra3)} letras.")
        break
    elif len(palabra3) < 4:
        print(f"Hacen falta letras. Solo tiene {len(palabra3)} letras.")
    else:
        print(f"Sobran letras. Tiene {len(palabra3)} letras.")


# Se genera el nombre clave combinando las palabras ingresadas
# - se toman las dos primeras letras de la primera palabra
# - se toman las dos últimas letras de la segunda palabra
# - se toman las primeras cuatro letras de la tercera palabra
nombre_clave = palabra1[:2] + palabra2[-2:] + palabra3[:4]

# muestra el conteno inicial de ltras
progreso = nombre_clave[:2] + '*' * 4 + nombre_clave[-2:]
letras_descubiertas = 4  # Inicialmente se muestran 4 letras
total_letras = len(nombre_clave)  # Total de letras de la clave

# Contador de errores
errores = 0
limite_errores = 3

# Mostrar una pista inicial al usuario sobre cómo comienza y termina la clave
print(f"La clave tiene {total_letras} caracteres y comienza con '{nombre_clave[:2]}' y termina con '{nombre_clave[-2:]}'.")
print("¡Intenta adivinar el nombre clave!")

# Bucle para que el usuario intente adivinar el nombre clave
while True:
    print(f"\nProgreso actual de la clave: {progreso}")
    print(f"Letras descubiertas: {letras_descubiertas}/{total_letras} (Faltan {total_letras - letras_descubiertas})")
    clave_usuario = input("Adivina el nombre clave generado: ")

    # Comprueba si la clave adivinada es correcta, admitiendo mayusculas y minusculas
    # El juego sale del bucle en cuanto el usuario adivina la palabras antes de los 3 intentos
    if clave_usuario.upper() == nombre_clave:
        letras_descubiertas = total_letras
        print("\n¡Correcto! Has adivinado el nombre clave.")
        print(f"Letras descubiertas: {letras_descubiertas}/{total_letras}")
        break
    else:
        errores += 1  # Incrementar contador de errores
        print("La clave no coincide. Inténtalo de nuevo.")

        if errores < limite_errores:
            # Por cada error, se revela una letra adicional
            posicion_a_revelar = 2 + errores  # Calcula la posición de la nueva letra a revelar
            progreso = (
                nombre_clave[:posicion_a_revelar] +  # Muestra hasta la nueva letra revelada
                '*' * (total_letras - posicion_a_revelar - 2) +
                nombre_clave[-2:]  # Mantiene las últimas letras visibles
            )
            letras_descubiertas = posicion_a_revelar + 2  # Sumar letras iniciales visibles
            print("Pista adicional: Se ha revelado otra letra.")
        else:
            # Si el usuario alcanza el límite de errores, termina el juego
            print(f"\nHas alcanzado el límite de intentos. La clave era: {nombre_clave}.")
            print(f"Letras descubiertas: {letras_descubiertas}/{total_letras}")
            break




