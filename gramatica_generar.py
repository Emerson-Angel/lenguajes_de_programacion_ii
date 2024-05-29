class Símbolo:
    def __init__(self, nombre, producciones):
        self.nombre = nombre
        self.producciones = producciones

    def generar_cadenas(self, gram, max_prof=10):
        if max_prof == 0:
            return []
        cadenas = []
        for prod in self.producciones:
            if any(s in prod for s in gram.símbolos):
                for s, s_obj in gram.símbolos.items():
                    if s in prod:
                        reemplazos = s_obj.generar_cadenas(gram, max_prof-1)
                        for reemplazo in reemplazos:
                            cadenas.append(prod.replace(s, reemplazo, 1))
            else:
                cadenas.append(prod)
        return cadenas

class Gram:
    def __init__(self, alfabeto, terminales, producciones):
        self.alfabeto = alfabeto
        self.terminales = terminales
        self.símbolos = {nombre: Símbolo(nombre, prod) for nombre, prod in producciones.items()}

    def mostrar_idiomas(self):
        for nombre, símbolo in self.símbolos.items():
            print(f'Idioma para {nombre}: {símbolo.generar_cadenas(self)}')

# Ejemplo de uso
gram_ej = Gram(
    alfabeto=['0', '1'],
    terminales=['S', 'A', 'B'],
    producciones={
        'S': ['AB', 'BA'],
        'A': ['00A', '0'],
        'B': ['11B', '1']
    }
)

gram_ej.mostrar_idiomas()
