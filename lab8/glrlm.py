import numpy as np

def glrlm(img: np.array, direction: str = '0'):
    max_gray = 256
    max_run_length = max(img.shape)
    matrix = np.zeros((max_gray, max_run_length), dtype=int)

    if direction == '0':
        # Горизонтально
        for row in img:
            run_val = row[0]
            run_len = 1
            for val in row[1:]:
                if val == run_val:
                    run_len += 1
                else:
                    matrix[run_val, run_len - 1] += 1
                    run_val = val
                    run_len = 1
            matrix[run_val, run_len - 1] += 1

    elif direction == '90':
        # Вертикально
        for col in img.T:
            run_val = col[0]
            run_len = 1
            for val in col[1:]:
                if val == run_val:
                    run_len += 1
                else:
                    matrix[run_val, run_len - 1] += 1
                    run_val = val
                    run_len = 1
            matrix[run_val, run_len - 1] += 1

    elif direction == '45':
        # Диагональ ↗ (снизу вверх, слева направо)
        h, w = img.shape
        for offset in range(-h + 1, w):
            diag = np.diagonal(np.fliplr(img), offset=offset)
            if diag.size == 0:
                continue
            run_val = diag[0]
            run_len = 1
            for val in diag[1:]:
                if val == run_val:
                    run_len += 1
                else:
                    matrix[run_val, run_len - 1] += 1
                    run_val = val
                    run_len = 1
            matrix[run_val, run_len - 1] += 1

    elif direction == '135':
        # Диагональ ↙ (сверху вниз, слева направо)
        h, w = img.shape
        for offset in range(-h + 1, w):
            diag = np.diagonal(img, offset=offset)
            if diag.size == 0:
                continue
            run_val = diag[0]
            run_len = 1
            for val in diag[1:]:
                if val == run_val:
                    run_len += 1
                else:
                    matrix[run_val, run_len - 1] += 1
                    run_val = val
                    run_len = 1
            matrix[run_val, run_len - 1] += 1

    return matrix

def GLNU(matrix: np.array):
    return np.sum(np.square(np.sum(matrix, axis=1))) / np.sum(matrix)

def RLNU(matrix: np.array):
    return np.sum(np.square(np.sum(matrix, axis=0))) / np.sum(matrix)


