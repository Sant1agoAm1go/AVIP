from my_io import prompt
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from os import path, makedirs
from semitone import to_semitone
from glrlm import glrlm, GLNU, RLNU
from contrast import contrast
from hsl_contrast import hsl_contrast

images = {
    'Bricks': 'kirp.png',
    'Pattern': 'oboi.png',
    'Sun': 'sun.png',
    'KCD2': 'kcd_2.png',
    'Gorshok': 'gorshok.png',
}

DIRECTIONS = ['0', '45', '90', '135']

def estimate_run_length(matrix, percentile=95):
    """Возвращает разумную длину серии для обрезки матрицы."""
    run_lengths = np.nonzero(matrix)[1]  # индексы по оси длины серии
    if len(run_lengths) == 0:
        return 10  # fallback
    max_length = int(np.percentile(run_lengths, percentile))
    return max(5, min(max_length + 1, matrix.shape[1]))


def visualize_glrlm(matrix, title, save_path, max_run_length=20):
    """Отображает и сохраняет GLRLM с логарифмическим масштабированием и ограничением длины серий."""
    cropped = matrix[:, :max_run_length]  # ограничение по длине серии
    log_scaled = np.log1p(cropped)

    norm = log_scaled / np.max(log_scaled) if np.max(log_scaled) != 0 else log_scaled
    norm *= 255

    plt.figure(figsize=(6, 5))
    plt.imshow(norm.astype(np.uint8), cmap='gray', aspect='auto')
    plt.title(title)
    plt.xlabel('Длина серии')
    plt.ylabel('Яркость')
    plt.colorbar(label='log(1 + значение)')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def ensure_dirs():
    for folder in ['results/semitone', 'results/contrasted', 'results/histograms',
                   'results/glrlm', 'results/glrlm_contrasted']:
        makedirs(folder, exist_ok=True)

if __name__ == '__main__':
    ensure_dirs()
    print('Выберите изображение:')
    selected_image = prompt(images)

    # Сохраняем полутоновое изображение
    semitone_img = to_semitone(selected_image)
    semitone_img.save(path.join('results', 'semitone', selected_image))

    semi = np.array(Image.open(path.join('results', 'semitone', selected_image)).convert('L'))

    # Контрастирование
    transformed = contrast(semi)
    transformed_img = Image.fromarray(transformed.astype(np.uint8), "L")
    transformed_img.save(path.join('results', 'contrasted', selected_image))

    # Контрастирование цветного изображения через HSL
    original_rgb = np.array(Image.open(path.join('src', selected_image)).convert('RGB'))
    contrasted_color = hsl_contrast(original_rgb)
    Image.fromarray(contrasted_color).save(path.join('results', 'contrasted', f"color_{selected_image}"))

    # Гистограммы яркости
    figure, axis = plt.subplots(2, 1, figsize=(6, 6))
    axis[0].hist(x=semi.flatten(), bins=np.arange(1, 255))
    axis[0].set_title('Исходное изображение')

    axis[1].hist(x=transformed.flatten(), bins=np.arange(1, 255))
    axis[1].set_title('Преобразованное изображение')
    plt.tight_layout()
    plt.savefig(path.join('results', 'histograms', selected_image))
    plt.close()

    # Обработка всех направлений
    for direction in DIRECTIONS:
        print(f'\n--- Направление {direction}° ---')

        # Исходное
        matrix = glrlm(semi.astype(np.uint8), direction=direction)
        max_run_length = estimate_run_length(matrix)
        visualize_glrlm(
            matrix,
            title=f"GLRLM {direction}° — исходное",
            save_path=path.join('results', 'glrlm', f'{direction}_{selected_image}'),
            max_run_length=max_run_length
        )

        # Контрастированное
        t_matrix = glrlm(transformed.astype(np.uint8), direction=direction)
        t_max_run_length = estimate_run_length(t_matrix)
        visualize_glrlm(
            t_matrix,
            title=f"GLRLM {direction}° — контрастированное",
            save_path=path.join('results', 'glrlm_contrasted', f'{direction}_{selected_image}'),
            max_run_length=t_max_run_length
        )

        # Признаки
        print(f"GLNU: {GLNU(matrix):.2f}")
        print(f"GLNU (contrasted): {GLNU(t_matrix):.2f}")
        print(f"RLNU: {RLNU(matrix):.2f}")
        print(f"RLNU (contrasted): {RLNU(t_matrix):.2f}")
