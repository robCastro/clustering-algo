import puntos, random, grafico


def main():
    cantidad = int(input('Cantidad a generar: '))
    if cantidad > puntos.MAXIMA_CANTIDAD_PUNTOS:
        raise ValueError(f"La maxima cantidad permitida es {puntos.MAXIMA_CANTIDAD_PUNTOS}")

    graficos = []
    # Por definicion, cada punto es un cluster
    clusters = puntos.generar_puntos(cantidad)
    # Partir de un punto random en los puntos
    punto = clusters.pop(random.randrange(len(clusters)))
    while len(clusters) > 0:
        idx_punto_cercano = puntos.obtener_punto_cercano(punto, clusters)
        otro_punto = clusters.pop(idx_punto_cercano)
        # Hace la union de ambos
        punto = puntos.unir_puntos(punto, otro_punto)
        # Muestra en pantalla
        graficos.append(grafico.generar(clusters, punto, cantidad))

    grafico.mostrar(graficos)

if __name__ == "__main__":
    main()