import random
import string

def generator_password(longitud):
    caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890!@#$%^&*()_-+="
    password = ''.join(random.choice(caracteres) for i in range(longitud))
    return password

def cumple_condiciones(password):
    # Verifica si la contraseña cumple con las condiciones
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_minuscula = any(c.islower() for c in password)
    tiene_numero = any(c.isdigit() for c in password)
    tiene_caracter_especial = any(c in "!@#$%^&*()_-+=" for c in password)
    
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial

try:
    longitud = int(input("¿Cuál es la longitud de la contraseña deseada?: "))
    if longitud < 5:
        raise ValueError("La contraseña debe ser mayor a 5")
    
    while True:
        new_password = generator_password(longitud)
        if cumple_condiciones(new_password):
            print(f"Tu contraseña es: {new_password}")
            break  # Sale del bucle si la contraseña cumple las condiciones

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"Error: {e}")