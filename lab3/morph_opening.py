import numpy as np
import cv2


def morphological_opening(img, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # Создаем квадратный структурирующий элемент
    eroded = cv2.erode(img, kernel, iterations=1)  # Эрозия
    opened = cv2.dilate(eroded, kernel, iterations=1)  # Дилатация
    return opened


if __name__ == '__main__':
    pass
