import numpy as np
from PIL import Image
from integral import integral_image
from semitone import image_to_np_array
from semitone import semitone


def sauvola_threshold(img: np.ndarray, window_size: int = 3, k: float = 0.3) -> np.ndarray:
    if window_size % 2 == 0:
        raise ValueError("Размер окна должен быть нечетным!")

    half_win = window_size // 2
    img = img.astype(np.float64)

    int_img = integral_image(img)
    int_img_sq = integral_image(img ** 2)

    rows, cols = img.shape
    binarized = np.zeros_like(img, dtype=np.uint8)

    for y in range(rows):
        for x in range(cols):
            y1, y2 = max(0, y - half_win), min(rows - 1, y + half_win)
            x1, x2 = max(0, x - half_win), min(cols - 1, x + half_win)

            area = (y2 - y1 + 1) * (x2 - x1 + 1)

            sum_pixels = int_img[y2, x2]
            sum_sq_pixels = int_img_sq[y2, x2]

            if x1 > 0:
                sum_pixels -= int_img[y2, x1 - 1]
                sum_sq_pixels -= int_img_sq[y2, x1 - 1]

            if y1 > 0:
                sum_pixels -= int_img[y1 - 1, x2]
                sum_sq_pixels -= int_img_sq[y1 - 1, x2]

            if x1 > 0 and y1 > 0:
                sum_pixels += int_img[y1 - 1, x1 - 1]
                sum_sq_pixels += int_img_sq[y1 - 1, x1 - 1]

            mean = sum_pixels / area
            std_dev = np.sqrt((sum_sq_pixels / area) - (mean ** 2))

            threshold = mean * (1 + k * ((std_dev / 128) - 1))

            binarized[y, x] = 255 if img[y, x] > threshold else 0

    return binarized


if __name__ == '__main__':
    img = image_to_np_array("test.png")
    img_gray = semitone(img)

    bin_img = sauvola_threshold(img_gray, 3, 0.3)

    result = Image.fromarray(bin_img, "L")
    result.show()
    result.save('pictures_results/test_binarized.png')



