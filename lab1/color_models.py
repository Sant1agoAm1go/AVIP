from PIL import Image
import numpy as np
from os import path


def image_to_np_array(image_name: str) -> np.array:
    img_src = Image.open(path.join('pictures_src', image_name)).convert('RGB')
    return np.array(img_src)


def save_image(image_array, filename):
    img = Image.fromarray(image_array.astype(np.uint8))
    img.save(path.join('pictures_results', filename))


def extract_rgb_components(image_name):
    img = image_to_np_array(image_name)

    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    save_image(np.stack([R, np.zeros_like(R), np.zeros_like(R)], axis=2), f'R_{image_name}')
    save_image(np.stack([np.zeros_like(G), G, np.zeros_like(G)], axis=2), f'G_{image_name}')
    save_image(np.stack([np.zeros_like(B), np.zeros_like(B), B], axis=2), f'B_{image_name}')


def rgb_to_hsi(image_name):
    img = image_to_np_array(image_name).astype(np.float32) / 255.0
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    I = (R + G + B) / 3

    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (min_rgb / (I + 1e-10))


    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-10
    theta = np.arccos(num / den)  # В радианах

    H = np.where(B > G, 2 * np.pi - theta, theta)  # Коррекция угла
    H = H / (2 * np.pi)  # Нормализация в диапазон [0,1]


    save_image((H * 255).astype(np.uint8), f'H_{image_name}')
    save_image((S * 255).astype(np.uint8), f'S_{image_name}')
    save_image((I * 255).astype(np.uint8), f'I_{image_name}')

    H = np.clip(H, 0, 1)
    S = np.clip(S, 0, 1)
    I = np.clip(I, 0, 1)

    hsi_image = np.stack([H, S, I], axis=2) * 255
    save_image(hsi_image.astype(np.uint8), f'HSI_{image_name}')
    return H, S, I

def invert_intensity(image_name):
    img = image_to_np_array(image_name).astype(np.float32) / 255.0
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    I = (R + G + B) / 3
    inverted_I = 1 - I

    factor = inverted_I / (I + 1e-10)  # Избегаем деления на 0
    R_new, G_new, B_new = R * factor, G * factor, B * factor

    R_new = np.clip(R_new, 0, 1)
    G_new = np.clip(G_new, 0, 1)
    B_new = np.clip(B_new, 0, 1)

    inverted_img = np.stack([R_new, G_new, B_new], axis=2) * 255

    save_image(inverted_img.astype(np.uint8), f'Inverted_{image_name}')


def invert_intensity_hsi(image_name):
    H, S, I = rgb_to_hsi(image_name)

    I_inverted = 1 - I

    hsi_inverted_image = np.stack([H, S, I_inverted], axis=2) * 255

    H, S, I = hsi_inverted_image[:, :, 0] / 255, hsi_inverted_image[:, :, 1] / 255, hsi_inverted_image[:, :, 2] / 255

    R = I * (1 + S * np.cos(H * 2 * np.pi) / (np.cos(np.pi / 3 - H * 2 * np.pi)))
    G = I * (1 + S * np.cos((H * 2 * np.pi) - 2 * np.pi / 3) / (np.cos(np.pi / 3 - H * 2 * np.pi)))
    B = I * (1 + S * np.cos((H * 2 * np.pi) + 2 * np.pi / 3) / (np.cos(np.pi / 3 - H * 2 * np.pi)))

    R = np.clip(R, 0, 1)
    G = np.clip(G, 0, 1)
    B = np.clip(B, 0, 1)

    rgb_inverted = np.stack([R, G, B], axis=2) * 255

    save_image(rgb_inverted.astype(np.uint8), f'Inverted_HSI_{image_name}')


if __name__ == '__main__':
    pass
