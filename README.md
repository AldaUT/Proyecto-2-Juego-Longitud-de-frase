# Proyecto-2-Juego-Longitud-de-frase
A este proyecto le complementé un ejercicio de los que realicé en este módulo, con la idea de crear un juego de palabras donde, a medida que el jugador hace intentos, se le generan pistas que ayudan a adivinar la clave.

La idea principal es que el jugador introduzca tres palabras. Se valida que cada palabra tenga entre 4 y 8 caracteres. Si la palabra tiene menos de 4 letras, se le muestra un mensaje indicando cuántas letras faltan. Si tiene más de 8 letras, se le avisa que tiene caracteres sobrantes. 
Si cumple con las condiciones, se acepta la palabra.

### Descripción del juego:

1. El jugador debe introducir tres palabras con un mínimo de 4 caracteres y un máximo de 8 caracteres.
2. Al ingresar cada palabra, se valida la longitud y se da retroalimentación sobre la cantidad de caracteres faltantes o sobrantes.
3. Después de que el jugador ingrese las tres palabras, el sistema genera una "clave" secreta a partir de las palabras. La clave se forma combinando:
   - Las dos primeras letras de la primera palabra.
   - Las dos últimas letras de la segunda palabra.
   - Las primeras cuatro letras de la tercera palabra.
4. El jugador debe adivinar esta clave secreta. Se le proporcionan pistas a medida que hace intentos. En cada intento fallido, se revela una letra de la clave.
5. El jugador tiene un límite de 3 intentos. Si no adivina la clave en esos intentos, el juego termina y muestra la clave correcta.

### Funcionalidades del código:

- Validación de longitud de las palabras ingresadas.
- Generación de clave secreta a partir de las palabras ingresadas.
- Progreso dinámico de la clave con pistas sobre letras descubiertas.
- Límite de intentos para adivinar la clave.
