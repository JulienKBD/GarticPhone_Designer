# === Includes ===
from pynput.mouse import Controller, Button
import time
import requests
from PIL import Image
from io import BytesIO

# === Colors ===
colors = [
    {"color": "BLACK",        "rgb": (0, 0, 0),         "pos": (510, 450)},
    {"color": "GREY",         "rgb": (102, 102, 102),   "pos": (560, 450)},
    {"color": "BLUE",         "rgb": (5, 83, 205),      "pos": (600, 450)},
    {"color": "WHITE",        "rgb": (255, 255, 255),   "pos": (510, 500)},
    {"color": "GREY_LIGHT",   "rgb": (170, 170, 170),   "pos": (560, 500)},
    {"color": "CYAN",         "rgb": (51, 200, 252),    "pos": (600, 500)},
    {"color": "GREEN",        "rgb": (54, 116, 33),     "pos": (510, 550)},
    {"color": "RED_DARK",     "rgb": (154, 40, 18),     "pos": (560, 550)},
    {"color": "BROWN",        "rgb": (150, 65, 20),     "pos": (600, 550)},
    {"color": "GREEN_LIGHT",  "rgb": (85, 177, 61),     "pos": (510, 600)},
    {"color": "RED",          "rgb": (242, 68, 35),     "pos": (560, 600)},
    {"color": "ORANGE",       "rgb": (245, 118, 41),    "pos": (600, 600)},
    {"color": "ORANGE_BROWN", "rgb": (176, 112, 30),    "pos": (510, 650)},
    {"color": "PURPLE",       "rgb": (155, 50, 78),     "pos": (560, 650)},
    {"color": "BEIGE_DARK",   "rgb": (203, 90, 87),     "pos": (600, 650)},
    {"color": "YELLOW",       "rgb": (228, 167, 47),    "pos": (510, 700)},
    {"color": "PINK",         "rgb": (240, 86, 143),    "pos": (560, 700)},
    {"color": "BEIGE",        "rgb": (247, 174, 168),   "pos": (600, 700)},
]

# === Global variables ===
mouse = Controller()

# === Functions ===
def extract_rgb_pixels_from_url(url: str, size: int = 400) -> list[tuple[int, int, int]]:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((size, size))
    image = image.convert("RGB")
    pixels = [
        image.getpixel((x, y))
        for y in range(image.height)
        for x in range(image.width)
    ]
    return pixels

def round_rgb_values(pixels_list):
    reference_colors = [c["rgb"] for c in colors]

    def closest_color(pixel):
        return min(reference_colors, key=lambda ref: (
            (pixel[0] - ref[0]) ** 2 +
            (pixel[1] - ref[1]) ** 2 +
            (pixel[2] - ref[2]) ** 2
        ))
    return [closest_color(p) for p in pixels_list]


def main():
    url = "https://cdn.futura-sciences.com/sources/images/actu/esperance-vie-chiens-chiot-golden-retriever.jpg"
    REDIMENSION_SIZE = 400

    pixels_list = extract_rgb_pixels_from_url(url, REDIMENSION_SIZE)
    round_pixels_list = round_rgb_values(pixels_list)

    # z = 750
    # time.sleep(2)
    # for color in colors:
    #     mouse.position = color["pos"]
    #     mouse.click(Button.left, 1)
    #     mouse.position = (z, 550)
    #     mouse.click(Button.left, 1)
    #     time.sleep(0.75)
    #     z += 25
    return

# === Entry point ===
if __name__ == "__main__":
    main()
