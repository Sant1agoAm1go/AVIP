import numpy as np


def integral_image(img: np.ndarray) -> np.ndarray:
    int_img = np.zeros_like(img, dtype=np.float64)

    int_img[0, 0] = img[0, 0]

    for x in range(1, img.shape[1]):
        int_img[0, x] = int_img[0, x - 1] + img[0, x]

    for y in range(1, img.shape[0]):
        int_img[y, 0] = int_img[y - 1, 0] + img[y, 0]

    for y in range(1, img.shape[0]):
        for x in range(1, img.shape[1]):
            int_img[y, x] = img[y, x] + int_img[y - 1, x] + int_img[y, x - 1] - int_img[y - 1, x - 1]

    return int_img

