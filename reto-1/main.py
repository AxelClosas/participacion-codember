import sys
import CalcularFrecuencia as modulo


def run():
    # Capturamos los argumentos enviados desde la consola manejando potenciales errores
    try:
        if 0 < len(sys.argv) <= 2:
            path = f"./{sys.argv[1]}"
            programa = modulo.CalcularFrecuencia(path)
            programa.exportar_resultado_en_archivo()
        else:
            raise Exception("Modo de uso\npython3 main.py <nombre_del_archivo.txt>")
    except Exception as e:
        print(e)


# El objetivo es ejecutar el archivo como script
if __name__ == "__main__":
    run()
