from my_io import np, safe_number_input
from sauvola import sauvola_threshold, simple_bin
from typing import Literal


operators = {
    'x': np.array(
        [[17, 61, 17],
         [0, 0, 0],
         [-17, -61, -17]]
    ),

    'y': np.array(
        [[17, 0, -17],
         [61, 0, -61],
         [17, 0, -17]]
    )
}


def get_frame(img: np.array, x: int, y: int) -> np.array:
    above = x - 1
    low = x + 2
    left = y - 1
    right = y + 2

    return img[above: low, left: right]


def apply_operator(frame: np.array, direction: Literal['x', 'y', 'g', 'b']):
    frame = frame.astype(np.int32)

    match direction:
        case 'x':
            return np.sum(operators['x'] * frame)

        case 'y':
            return np.sum(operators['y'] * frame)

        case 'g':
            return abs(np.sum(operators['x'] * frame)) + \
                        abs(np.sum(operators['y'] * frame))

        case 'b':
            return abs(np.sum(operators['x'] * frame)) + \
                        abs(np.sum(operators['y'] * frame))
        case _:
            raise ValueError("Unsupported direction")


def krun_operator(img: np.array, direction: Literal['x', 'y', 'g', 'b']):
    new_img = np.zeros_like(img, dtype=np.float64)
    x, y = 1, 1

    while x < img.shape[0] - 1:
        if x % 2 == 0:
            while y + 1 < img.shape[1] - 1:
                frame = get_frame(img, x, y)
                new_img[x, y] = apply_operator(frame, direction)
                y += 1

        else:
            while y - 1 > 1:
                frame = get_frame(img, x, y)
                new_img[x, y] = apply_operator(frame, direction)
                y -= 1

        x += 1

    new_img = new_img / np.max(new_img) * 255

    if direction == 'b':
        # print("Введите порог t:")
        # t = safe_number_input(0, 255)
        # return simple_bin(new_img, 45).astype(np.uint8)

        return sauvola_threshold(new_img.astype(np.uint8), 45, 0.3).astype(np.uint8)

    elif direction == 'x' or direction == 'y' or direction == 'g':
        return new_img.astype(np.uint8)

    else:
        raise ValueError("Unsupported direction")


if __name__ == '__main__':
    pass
