import math
import hashlib

# Función para cifrar un texto usando el cifrado César
def cifra_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha() or caracter.isspace():  # Incluye espacios en el cifrado
            mayuscula = caracter.isupper()  
            caracter = caracter.upper()  
            if caracter.isalpha():  # Solo aplica el cifrado a letras
                codigo = ord(caracter) + desplazamiento
                if codigo > ord('Z'):
                    codigo -= 26
                caracter_cifrado = chr(codigo)
            else:  # Si no es una letra, conserva el carácter
                caracter_cifrado = caracter
            if mayuscula:
                texto_cifrado += caracter_cifrado
            else:
                texto_cifrado += caracter_cifrado.lower()  
        else:
            texto_cifrado += caracter  
    return texto_cifrado

# Función para calcular la entropía de Shannon dada una lista de probabilidades
def entropia_shannon(probabilidades):
    entropia = 0
    for prob in probabilidades:
        if prob != 0:
            entropia -= prob * math.log2(prob)
    return entropia

# Función para calcular las fracciones de aparición de cada carácter en un texto
def calcular_fracciones(texto):
    total_caracteres = len(texto)
    
    conteo_caracteres = {}
    for caracter in texto:
        conteo_caracteres[caracter] = conteo_caracteres.get(caracter, 0) + 1
    
    fracciones = []
    for caracter in texto:
        fraccion = conteo_caracteres[caracter] / total_caracteres
        fracciones.append(fraccion)
    
    return fracciones

# Solicita al usuario ingresar un párrafo de texto
texto_original = input("Ingrese un párrafo de texto: ")

# Cifrado César
desplazamiento_cesar = 3  # Ejemplo de desplazamiento
texto_cifrado_cesar = cifra_cesar(texto_original, desplazamiento_cesar)

# MD5
md5_hash = hashlib.md5(texto_original.encode()).hexdigest()

# SHA-256
sha256_hash = hashlib.sha256(texto_original.encode()).hexdigest()

# Calcular entropía de Shannon para cada texto cifrado
fracciones_cesar = calcular_fracciones(texto_cifrado_cesar)
entropia_cesar = entropia_shannon(fracciones_cesar)

fracciones_md5 = calcular_fracciones(md5_hash)
entropia_md5 = entropia_shannon(fracciones_md5)

fracciones_sha256 = calcular_fracciones(sha256_hash)
entropia_sha256 = entropia_shannon(fracciones_sha256)

# Imprimir los resultados de la entropía de Shannon para cada caso
print("\nEntropía de Shannon del texto cifrado con César:", entropia_cesar)
print("Entropía de Shannon del hash MD5:", entropia_md5)
print("Entropía de Shannon del hash SHA-256:", entropia_sha256)
