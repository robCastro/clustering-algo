from typing import List, Tuple

from bokeh.plotting import figure, show, output_file
from bokeh.models import Range1d
from bokeh.layouts import column

from puntos import MAX_X, MAX_Y, MIN_X, MIN_Y


RADIO_PUNTO = 20


def generar(clusters: List[Tuple[int, int]], grupo: Tuple[int, int], cantidad: int):
    x = []
    y = []
    colors = []
    sizes = []
    for cluster in clusters:
        x.append(cluster[0])
        y.append(cluster[1])
        colors.append('navy')
        sizes.append(RADIO_PUNTO)
    x.append(grupo[0])
    y.append(grupo[1])
    colors.append('red')
    sizes.append(RADIO_PUNTO + ((cantidad - len(clusters)) * 2 ))
    
    chart = figure()
    chart.circle(x, y, size=sizes, color=colors, alpha=0.5)
    chart.x_range = Range1d((MIN_X - RADIO_PUNTO), (MAX_X + RADIO_PUNTO))
    chart.y_range = Range1d((MIN_Y - RADIO_PUNTO), (MAX_Y + RADIO_PUNTO))
    
    return chart


def mostrar(graficos: list) -> None:
    show(column(graficos))