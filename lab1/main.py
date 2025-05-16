from resampling import *
from color_models import *

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

def execute(img, f1, f2, number_type=int):
    data_type = np.uint8
    color_model = 'RGB'

    factor = safe_number_input(number_type, 1e-10)
    result = Image.fromarray(one_step_resampling(
        img, factor, f1, f2).astype(data_type), color_model)

    return result

def save_image(image_array, filename):
    img = Image.fromarray(image_array.astype(np.uint8))
    img.save(path.join('pictures_results', filename))

images = {
    'KCD2': 'kcd_2.png',
    'Spiral': 'spiral.png',
    'Test': 'test.png',
    'Football': 'football.png',
    'Spiral2': 'spiral2.png'
}

operation_classes_colors = {
    'Выделение RGB-компонентов': 'rgb',
    'Преобразование в HSI (яркость)': 'hsi',
    'Инверсия яркости': 'invert'
}

operation_classes = {
    'Интерполяция': 'int',
    'Децимация': 'dec',
    'Однопроходная передискретизация': 'one',
    'Двухпроходная передискретизация': 'two'

}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)
    result = None


    print('Выберите категорию операции:')
    category = prompt({'Цветовые модели': 'color', 'Передискретизация': 'resampling'})

    if category == 'resampling':
        print('Выберите операцию:')
        selected_operation = prompt(operation_classes)

        match selected_operation:
            case 'int':
                print('Введите целый коэффициент растяжения')
                result = execute(img, lambda a, b: a * b,
                                 lambda a, b: int(round(a / b)))

            case 'dec':
                print('Введите целый коэффициент сжатия')
                result = execute(img, lambda a, b: int(round(a / b)),
                                 lambda a, b: a * b)

            case 'two':
                print('Введите целый коэффициент растяжения')
                numerator = safe_number_input(int, 1)

                print('Введите целый коэффициент сжатия')
                denominator = safe_number_input(int, 1)

                args = [numerator, denominator]
                result = Image.fromarray(
                    two_step_resampling(img, *args).astype(np.uint8),
                    'RGB')

            case 'one':
                print('Введите дробный коэффициент растяжения/сжатия')
                result = execute(img, lambda a, b: int(round(a * b)),
                                 lambda a, b: int(round(a / b)), float)

            case _:
                exit()

    else:
        print('Выберите операцию с цветовой моделью:')
        selected_operation = prompt(operation_classes_colors)

        match selected_operation:
            case 'rgb':
                extract_rgb_components(selected_image)

            case 'hsi':
                rgb_to_hsi(selected_image)

            case 'invert':
                invert_intensity(selected_image)

            case _:
                exit()

    if category == 'resampling':
        print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
        selected_path = input()
        if selected_path and result is not None:
            result.save(path.join('pictures_results', selected_path))

    print('Операция завершена!')

