"""
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""

from PIL import Image
from requests import get
from io import BytesIO


def calculate_aspect_ratio(image_url: str) -> float:
    response = get(image_url)
    image = Image.open(BytesIO(response.content))

    width, height = image.size
    aspect_ratio = width / height

    response.close()
    image.close()

    return aspect_ratio


image_url = "https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg"
print("The aspect ratio of the image is:", calculate_aspect_ratio(image_url))
