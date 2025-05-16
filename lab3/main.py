from morph_opening import morphological_opening
from difference import difference_image
from my_io import prompt, image_to_np_array, path, Image

images = {
    'Staroslav': 'staroslav_bin.png',
    'KCD2': 'kcd_bin2.png',
    'Cartoon': 'cartoon_bin.png',
    'Fingerprint': 'fingerprint_semitone.png',
    'Gorshok': 'gorshok_bin.png',
    'Map': 'map_bin.png',
    'Photo': 'photo_semitone.png',
    'Test': 'test_bin.png',
    'Text': 'text_bin.png',
    'Xray': 'xray_semitone.png'
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    res_img = morphological_opening(img)  # Применяем морфологическое открытие
    difference = difference_image(img, res_img)

    res_img = Image.fromarray(res_img, 'L')
    difference = Image.fromarray(difference, 'L')

    difference.save(path.join('differential_pictures', selected_image))
    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
    selected_path = input()
    if selected_path:
        res_img.save(path.join('pictures_results', selected_path))
