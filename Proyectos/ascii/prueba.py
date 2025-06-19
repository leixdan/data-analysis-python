import time
import sys

def animacion_cargando(ciclos=3, delay=0.5):
    estados = ["Cargando   ", "Cargando.  ", "Cargando.. ", "Cargando..."]
    for _ in range(ciclos):
        for estado in estados:
            # Imprime y sobrescribe la línea anterior
            sys.stdout.write("\r" + estado)
            sys.stdout.flush()
            time.sleep(delay)
    # Limpia la línea y escribe mensaje final
    sys.stdout.write("\r¡Listo!        \n")

# Ejecutar la animación
animacion_cargando()