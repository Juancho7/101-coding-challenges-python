"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""


def polygon_area(polygon: dict) -> None:
    if polygon["type"] == "triangle":
        print((polygon["base"] * polygon["height"]) / 2)

    if polygon["type"] == "square":
        print(polygon["base"] * polygon["base"])

    if polygon["type"] == "rectangle":
        print(polygon["base"] * polygon["height"])


polygon = {"type": "triangle", "base": 10, "height": 10}
polygon_area(polygon)

polygon = {"type": "square", "base": 10, "height": 10}
polygon_area(polygon)

polygon = {"type": "rectangle", "base": 10, "height": 5}
polygon_area(polygon)
