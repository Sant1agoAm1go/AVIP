from my_io import *
from contour import krun_operator
from my_io import Image

operations = {
    'Градиентная матрица G_x': 'x',
    'Градиентная матрица G_y': 'y',
    'Градиентная матрица G': 'g',
    'Бинаризованная градиентная матрица G_b': 'b',
}

images = {
    'Cartoon': 'cartoon_semitone.png',
    'Gorshok': 'gorshok_semitone.png',
    'KCD2': 'kcd2_semitone.png',
    'Staroslav': 'staroslav_semitone.png',
    'Text': 'text_semitone.png',
    'Xray': 'xray_semitone.png',
    'Photo': 'photo_semitone.png',
    'Map': 'map_semitone.png'
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    print('Выберите вид обработки:')
    op = prompt(operations)

    result = Image.fromarray(krun_operator(img, op), 'L')
    print('Введите название сохраненного изображения (оставьте пустым, чтобы \
не сохранять)')

    selected_path = input()
    if selected_path:
        result.save(path.join('pictures_results', selected_path))
