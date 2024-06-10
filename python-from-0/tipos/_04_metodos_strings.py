""" Metodos de strings en python"""
ANIMAL = "chanchito feliz"
ANIMAL2 = "Chanchito Triste"
PRUEBAS = "cHANchito fELIZ"
print(ANIMAL[0].upper() + ANIMAL[1:])
print(ANIMAL.lower())
print(PRUEBAS.capitalize())  # Pone en mayuscula la primera letra de la cadena
print(PRUEBAS.title())  # Pone en mayuscula la primera letra de cada palabra
print(PRUEBAS.strip())  # Elimina espacios en blanco
