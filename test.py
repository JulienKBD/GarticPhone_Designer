import pygame
import requests
from PIL import Image
from io import BytesIO

# === Couleurs de référence ===
colors = [
    {"color": "BLACK",        "rgb": (0, 0, 0)},
    {"color": "GREY",         "rgb": (102, 102, 102)},
    {"color": "BLUE",         "rgb": (5, 83, 205)},
    {"color": "WHITE",        "rgb": (255, 255, 255)},
    {"color": "GREY_LIGHT",   "rgb": (170, 170, 170)},
    {"color": "CYAN",         "rgb": (51, 200, 252)},
    {"color": "GREEN",        "rgb": (54, 116, 33)},
    {"color": "RED_DARK",     "rgb": (154, 40, 18)},
    {"color": "BROWN",        "rgb": (150, 65, 20)},
    {"color": "GREEN_LIGHT",  "rgb": (85, 177, 61)},
    {"color": "RED",          "rgb": (242, 68, 35)},
    {"color": "ORANGE",       "rgb": (245, 118, 41)},
    {"color": "ORANGE_BROWN", "rgb": (176, 112, 30)},
    {"color": "PURPLE",       "rgb": (155, 50, 78)},
    {"color": "BEIGE_DARK",   "rgb": (203, 90, 87)},
    {"color": "YELLOW",       "rgb": (228, 167, 47)},
    {"color": "PINK",         "rgb": (240, 86, 143)},
    {"color": "BEIGE",        "rgb": (247, 174, 168)},
]

# === Fonctions ===
def extract_pixels_from_url(url, size=400):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((size, size))
    image = image.convert("RGB")
    return list(image.getdata()), size, size

def round_rgb_values(pixels_list):
    reference_colors = [c["rgb"] for c in colors]

    def closest_color(pixel):
        return min(reference_colors, key=lambda ref: (
            (pixel[0] - ref[0]) ** 2 +
            (pixel[1] - ref[1]) ** 2 +
            (pixel[2] - ref[2]) ** 2
        ))

    return [closest_color(p) for p in pixels_list]

# === Programme principal ===
def main():
    url = "https://cdn.futura-sciences.com/sources/images/actu/esperance-vie-chiens-chiot-golden-retriever.jpg"
    url = "https://www.cuisineetsentiments.com/images/canard_1.jpg"
    pixel_size = 5  # Taille d’un "pixel affiché"
    img_pixels, width, height = extract_pixels_from_url(url, size=250)
    rounded_pixels = round_rgb_values(img_pixels)

    pygame.init()
    screen = pygame.display.set_mode((width * pixel_size, height * pixel_size))
    pygame.display.set_caption("Image en pixels simplifiés")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Affichage des pixels
        for y in range(height):
            for x in range(width):
                color = rounded_pixels[y * width + x]
                rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
                pygame.draw.rect(screen, color, rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
