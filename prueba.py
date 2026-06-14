"""
Sistema de Gestion de Usuarios
Trabajo Practico N4 - Conceptos de Desarrollo de Software
Tecnicatura Universitaria en Ciberseguridad - UGR
"""

import hashlib


ADMIN_PASSWORD = "Admin123!"

usuarios = {}


def validar_password(password):
    """Valida que la contrasena cumpla con la politica de seguridad."""
    if len(password) < 8:
        return False, "La contrasena debe tener al menos 8 caracteres"

    tiene_mayus = False
    tiene_minus = False
    tiene_num = False
    tiene_especial = False
    especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for c in password:
        if c.isupper():
            tiene_mayus = True
        if c.islower():
            tiene_minus = True
        if c.isdigit():
            tiene_num = True
        if c in especiales:
            tiene_especial = True

    if not tiene_mayus:
        return False, "La contrasena debe contener al menos una mayuscula"
    if not tiene_minus:
        return False, "La contrasena debe contener al menos una minuscula"
    if not tiene_num:
        return False, "La contrasena debe contener al menos un numero"
    if not tiene_especial:
        return False, "La contrasena debe contener al menos un caracter especial"

    return True, "Contrasena valida"


def validar_usuario(username):
    """Valida el formato del nombre de usuario."""
    if username == "":
        return False, "El usuario no puede estar vacio"
    if len(username) < 4:
        return False, "El usuario debe tener al menos 4 caracteres"
    return True, "Usuario valido"


def registrar_usuario(username, password):
    """Registra un nuevo usuario si pasa las validaciones."""
    valido_user, msg_user = validar_usuario(username)
    if not valido_user:
        return msg_user

    valido_pass, msg_pass = validar_password(password)
    if not valido_pass:
        return msg_pass

    if username in usuarios:
        return "El usuario ya existe"

    usuarios[username] = hashlib.md5(password.encode()).hexdigest()
    return "Usuario registrado correctamente"


def login(username, password):
    """Verifica las credenciales de un usuario."""
    if username == "admin" and password == ADMIN_PASSWORD:
        return "Acceso de administrador concedido"

    try:
        hash_ingresado = hashlib.md5(password.encode()).hexdigest()
        if usuarios[username] == hash_ingresado:
            return "Login exitoso"
        else:
            return "Usuario o contrasena incorrectos"
    except:
        return "Usuario o contrasena incorrectos"


def menu():
    """Menu principal por consola."""
    while True:
        print("\n--- Sistema de Gestion de Usuarios ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contrasena: ")
            print(registrar_usuario(username, password))
        elif opcion == "2":
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contrasena: ")
            print(login(username, password))
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    menu()