from itertools import product

class LenguajeGenerador:
    def __init__(self, n, p):
        self.alfabeto = list(range(n))
        self.potencia = p

    def generar_lenguaje(self):
        for i in range(self.potencia + 1):
            lenguaje = [''.join(map(str, x)) for x in product(self.alfabeto, repeat=i)]
            print(f"L^{i} = {lenguaje}")

def main():
    tamaño_alfabeto = int(input("Tamaño del alfabeto: "))
    potencia_lenguaje = int(input("Potencia del lenguaje: "))

    generador = LenguajeGenerador(tamaño_alfabeto, potencia_lenguaje)
    generador.generar_lenguaje()

if __name__ == "__main__":
    main()
