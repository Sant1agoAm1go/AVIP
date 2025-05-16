from sauvola import sauvola_threshold
from semitone import to_semitone, image_to_np_array, path
from semitone import semitone, Image, np


def prompt(variants: dict):
    for number, variant in enumerate(variants.keys(), 1):
        print(f'{number} - {variant}')
    input_correct = False
    user_input = 0
    while not input_correct:
        try:
            user_input = int(input('> '))
            if user_input <= 0 or user_input > len(variants):
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return dict(enumerate(variants.values(), 1))[user_input]


def safe_number_input(number_type: type, lower_bound=None, upper_bound=None):
    input_correct = False
    user_input = 0

    while not input_correct:
        try:
            user_input = number_type(input('> '))
            if lower_bound is not None and user_input < lower_bound:
                raise ValueError
            if upper_bound is not None and user_input > upper_bound:
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return user_input


def run_sauvola(img_name):
    # print("Введите коэффициент k (0.2 - 0.5, рекомендовано 0.3):")
    # k = safe_number_input(float, lower_bound=0.2, upper_bound=0.5)

    # Загружаем изображение и переводим в градации серого
    img = image_to_np_array(img_name)
    img_gray = semitone(img)

    return Image.fromarray(sauvola_threshold(img_gray, 75, 0.3).astype(np.uint8), "L")


images = {
    "KCD 2": 'kcd_2.png',
    "Test": 'test.png',
    "Xray": 'xray2.png',
    "Fingerprint": 'fingerprint.png',
    "Cartoon": 'cartoon.png',
    "Map": 'map.png',
    "Text": 'text.png',
    "Photo": 'photo.png',
    "Gorshok": 'gorshok.png',
    "Staroslav": 'staroslav.png'
}

operations = {
        'Полутон': 'semitone',
        'Бинаризация': 'thresholding'
}


if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    print("Выберите обработку изображения:")
    selected_handle = prompt(operations)

    match selected_handle:
        case 'semitone':
            result = to_semitone(selected_image)
        case 'thresholding':
            result = run_sauvola(selected_image)
        case _:
            exit()

    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path.join('pictures_results', selected_path))
