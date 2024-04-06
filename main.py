# Gestor de contraseñas

import random

print('Bienvenido al gestor de contraseñas')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?']

is_on = True
contador = 0

while is_on:
    password_length_input = input('¿Cuántos caracteres quieres que tenga tu contraseña? (el rango es de 4 a 40) o '
                                  'escribe "salir" para terminar el programa: ')

    if password_length_input.lower() == 'salir':
        print('Gracias por usar el gestor de contraseñas.')
        break

    try:
        password_length = int(password_length_input)
        if password_length < 4 or password_length > 40:
            print('Introduce un número entre 4 y 40')
        else:
            password = []
            for i in range(0, password_length):
                random_choice = random.randint(0, 2)
                if random_choice == 0:
                    password.append(random.choice(alphabet))
                elif random_choice == 1:
                    password.append(str(random.choice(numbers)))
                elif random_choice == 2:
                    password.append(random.choice(symbols))
            password = ''.join(password)
            print(f'Tu contraseña es: {password}')
            save_password = input('Deseas guardar esta contraseña? "si/no": ')
            if save_password.lower() == 'si':
                with open('contraseñas.txt', 'a') as file:
                    file.write(f'Tu contraseña numero {contador} generada es: {password}\n')
                    print('Contraseña guardada con éxito.')
                    contador += 1
            else:
                print('Contraseña no guardada.')
    except ValueError:
        print('Por favor, ingresa un número válido o "salir" para terminar el programa.')
