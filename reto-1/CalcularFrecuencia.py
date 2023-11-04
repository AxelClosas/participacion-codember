# Creo una clase que contendra toda la lógica de la aplicación
class CalcularFrecuencia:
    # Recibimos como parametro el path del archivo a decodificar
    def __init__(self, path):
        self.path = path

    # Aquí se encuentra la lógica necesaria para obtener la frecuencia de cada palabra. Retorna un diccionario
    def obtener_frecuencia(self) -> dict:
        f = {}
        with open(self.path, "r") as archivo:
            lista = archivo.readline().split()
            for palabra in lista:
                if palabra in f.keys():
                    f[palabra] += 1
                else:
                    f[palabra] = 1
        return f

    # Aquí se encuentra la lógica para generar un archivo txt con el resultado
    def exportar_resultado_en_archivo(self, nombre="resultado.txt"):
        f = self.obtener_frecuencia()
        keys, values = f.keys(), f.values()
        concatenar = lambda x, y: str(x) + str(y)

        with open(nombre, "w") as nuevo_archivo:
            nuevo_archivo.write("".join(list(map(concatenar, keys, values))))

        # my_list = my_list[0].split()
        # for word in my_list:
        #     if word in f.keys():
        #         f[word] += 1
        #     else:
        #         f[word] = 1
        # keys = list(f.keys())
        # values = list(f.values())
        # result = "".join(list(map(lambda x, y: str(x) + str(y), keys, values)))

    # return result
