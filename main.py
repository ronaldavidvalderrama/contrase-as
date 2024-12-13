#Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.
#Instrucciones:
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
#Utilizará una función para generar la contraseña según las preferencias del usuario.
#Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
#Si el usuario decide salir, se despedirá y el programa se cerrará.

#Se debe entregar el/los archivos de Python o el indicado por el Trainer, en el cual contenga el código del programa en cuestión.

import random
import string

def generar_contraseña(longitud, incluir_minusculas, incluir_mayusculas, incluir_alfanumericos, incluir_simbolos):
    # Inicializar la lista de caracteres válidos
    caracteres = ''
    
    # Añadir mayúsculas si se desea
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    
    # Añadir minúsculas si se desea
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    
    # Añadir alfanuméricos (números) si se desea
    if incluir_alfanumericos:
        caracteres += string.digits
    
    # Añadir símbolos si se desea
    if incluir_simbolos:
        caracteres += string.punctuation
    
    # Verificar que al menos se ha seleccionado un tipo de carácter
    if not caracteres:
        print("¡Debes seleccionar al menos un tipo de carácter!")
        return None
    
    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def mostrar_menu():
    print("\n----- GENERADOR DE CONTRASEÑAS -----")
    print("1. Generar una nueva contraseña")
    print("2. Salir")

def main():
    print("hola usuario bienvenido")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            try:
                # Solicitar la longitud de la contraseña
                longitud = int(input("Ingresa la longitud de la contraseña (mínimo 4): "))
                if longitud < 4:
                    print("La longitud mínima es 4 caracteres. Intenta nuevamente.")
                    continue
                
                # Solicitar las preferencias del usuario
                incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
                incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
                incluir_alfanumericos = input("¿Incluir números? (s/n): ").lower() == 's'
                incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'
                
                # Generar la contraseña
                contraseña = generar_contraseña(longitud, incluir_minusculas, incluir_mayusculas, incluir_alfanumericos, incluir_simbolos)
                
                if contraseña:
                    print(f"Contraseña generada: {contraseña}")
            
            except ValueError:
                print("Por favor, ingresa un número válido para la longitud.")
        
        elif opcion == '2':
            print("¡Gracias por usar el generador de contraseñas! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción correcta.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
