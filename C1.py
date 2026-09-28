
# Distribución del cuarto
#   A --<-- B
#   |       |
#   |       |
#   C -->-- D
# La aspiradora comienza en A

conexiones = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


def agente_reflejo_simple(sucias):

    posicion = "A"
    limpias = set()

    acciones = 0
    movimientos_repetidos = 0

    # Máximo de 20 acciones
    while acciones < 20:

        # Si la celda está sucia, la limpia
        if posicion in sucias and posicion not in limpias:

            limpias.add(posicion)
            acciones += 1

        else:

            # El agente solamente se mueve entre A y B
            # cuando encuentra una celda limpia.

            if posicion == "A":
                siguiente = "B"

            elif posicion == "B":
                siguiente = "A"

            else:
                # Si llegara a C o D, vuelve hacia arriba
                if posicion == "C":
                    siguiente = "A"
                else:
                    siguiente = "B"

            posicion = siguiente
            acciones += 1

            # Contamos si vuelve a una celda que ya limpió
            if posicion in limpias:
                movimientos_repetidos += 1

        # Si ya limpió todas las celdas sucias, termina
        if limpias == sucias:
            return True, acciones, movimientos_repetidos

    return False, acciones, movimientos_repetidos

def agente_basado_en_modelos(sucias):

    posicion = "A"

    # Guarda las celdas que ya limpió
    limpias = set()

    acciones = 0
    movimientos_repetidos = 0

    # Orden de exploración del cuarto
    recorrido = ["A", "B", "D", "C"]

    while acciones < 20:

        # Si la celda está sucia, la limpia
        if posicion in sucias and posicion not in limpias:

            limpias.add(posicion)
            acciones += 1

        else:

            # Busca una celda que todavía necesite limpiar
            siguiente_objetivo = None

            for celda in recorrido:

                if celda in sucias and celda not in limpias:
                    siguiente_objetivo = celda
                    break

            # Si ya no hay celdas por limpiar, termina
            if siguiente_objetivo is None:
                return True, acciones, movimientos_repetidos

            # Decide hacia dónde moverse para acercarse
            # al objetivo

            if posicion == "A":

                if siguiente_objetivo == "B":
                    posicion = "B"

                elif siguiente_objetivo == "C":
                    posicion = "C"

                elif siguiente_objetivo == "D":
                    posicion = "B"

            elif posicion == "B":

                if siguiente_objetivo == "A":
                    posicion = "A"

                elif siguiente_objetivo == "D":
                    posicion = "D"

                elif siguiente_objetivo == "C":
                    posicion = "D"

            elif posicion == "C":

                if siguiente_objetivo == "A":
                    posicion = "A"

                elif siguiente_objetivo == "D":
                    posicion = "D"

                elif siguiente_objetivo == "B":
                    posicion = "D"

            elif posicion == "D":

                if siguiente_objetivo == "B":
                    posicion = "B"

                elif siguiente_objetivo == "C":
                    posicion = "C"

                elif siguiente_objetivo == "A":
                    posicion = "B"

            acciones += 1

            # Revisamos si volvió a una celda ya limpia
            if posicion in limpias:
                movimientos_repetidos += 1

        # Si ya limpió todo lo que estaba sucio, termina
        if limpias == sucias:
            return True, acciones, movimientos_repetidos

    return False, acciones, movimientos_repetidos


casos = [
    {"A"},
    {"B"},
    {"C"},
    {"D"},
    {"A", "B"},
    {"A", "C"},
    {"A", "D"},
    {"B", "C"},
    {"B", "D"},
    {"A", "B", "C", "D"}
]

print(" COMPARACIÓN DE AGENTES")

resultados_reflejo = 0
resultados_modelo = 0


for numero, sucias in enumerate(casos, start=1):

    reflejo = agente_reflejo_simple(sucias)
    modelo = agente_basado_en_modelos(sucias)

    if reflejo[0]:
        resultados_reflejo += 1

    if modelo[0]:
        resultados_modelo += 1

    print(f"\nCaso {numero}")
    print("Celdas sucias:", ", ".join(sorted(sucias)))

    print("Reflejo simple:")

    if reflejo[0]:
        print("  ✓ Terminó")
    else:
        print("  ✗ No terminó")

    print("  Acciones:", reflejo[1])
    print("  Movimientos repetidos:", reflejo[2])


    print("Basado en modelos:")

    if modelo[0]:
        print("  ✓ Terminó")
    else:
        print("  ✗ No terminó")

    print("  Acciones:", modelo[1])
    print("  Movimientos repetidos:", modelo[2])

print(" RESULTADOS GENERALES")

print(
    "Reflejo simple:",
    resultados_reflejo,
    "de 10 casos terminados"
)

print(
    "Basado en modelos:",
    resultados_modelo,
    "de 10 casos terminados"
)