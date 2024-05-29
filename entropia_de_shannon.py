import math

def entropia_shannon(probabilidades):
   entropia = 0
   for prob in probabilidades:
       if prob != 0:
           entropia -= prob * math.log2(prob)
   return entropia

def calcular_fracciones(texto):
   # Dividir el texto en palabras
   palabras = texto.split()
   total_palabras = len(palabras)

   # Inicializar un diccionario para contar las ocurrencias de cada palabra
   conteo_palabras = {}
   for palabra in palabras:
       conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

   # Calcular la fracción para cada palabra
   fracciones = []
   for palabra in palabras:
       fraccion = conteo_palabras[palabra] / total_palabras
       fracciones.append(fraccion)

   return fracciones

texto = input("Ingrese el texto: ")
fracciones = calcular_fracciones(texto)
entropia = entropia_shannon(fracciones)
print("Entropía de Shannon del texto:", entropia)