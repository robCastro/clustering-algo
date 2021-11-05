import random
from typing import List, Tuple


MAXIMA_CANTIDAD_PUNTOS = 15

MIN_X = 0
MAX_X = 40

MIN_Y = 0
MAX_Y = 40

# c**2 = a**2 + b**2
MAXIMA_DISTANCIA_CUADRADO = ((MIN_X - MAX_X)**2 + (MIN_Y - MAX_Y)**2)


def generar_puntos(cantidad: int) -> List[Tuple[int, int]]:
    return [(random.randrange(MIN_X, MAX_X), random.randrange(MIN_Y, MAX_Y)) for _ in range (cantidad + 1)]


def obtener_punto_cercano(punto: Tuple[int, int], clusters: List[Tuple[int, int]]) -> int:
    # Inicializando la menor distancia a un valor muy alto
    menor_distancia = MAXIMA_DISTANCIA_CUADRADO
    indice_punto = -1
    for index, cluster in enumerate(clusters):
        # c = (a**2 + b**2)**0.5
        distancia = ((punto[0] - cluster[0])**2 + (punto[1] - cluster[1])**2)**0.5
        if distancia <= menor_distancia:
            menor_distancia = distancia
            indice_punto = index
    return indice_punto


def unir_puntos(punto: Tuple[int, int], otro_punto: Tuple[int, int]) -> Tuple[int, int]:
    x = (punto[0] + otro_punto[0]) / 2
    y = (punto[1] + otro_punto[1]) / 2
    return (x, y)
