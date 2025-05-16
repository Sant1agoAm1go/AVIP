import pandas as pd

df = pd.read_excel('results/Лист Microsoft Excel.xlsx', sheet_name='features')

template = """# Лабораторная работа №5. Выделение признаков символов.
Лабораторная работа проделывалась на грузинском алфавите. Тип букв -- обычные прописные,
шрифт NotoSansGeorgian-Regular, размер 52. В качестве демонстрации были выбраны 
6 символов, представляющих собой наибольший интерес. Квадраты для расчета веса черного расположены
следующим образом:

![](table.jpg)

{letters}
"""

letter_template = """
## Символ {letter} ({name})
Прямое и инвертированное сгенерированные изображения:

![](alphabet/direct/letter_{index:02d}.png)
![](alphabet/inverse/letter_{index:02d}.png)

Профили буквы:

![](results/profiles/x/letter_{index:02d}.png "Профиль по Х")
![](results/profiles/y/letter_{index:02d}.png "Профиль по Y")

Признаки:
1. Вес первого квадрата: {weight_I}
2. Нормированный(на четверть площади) вес черного: {relative_weight_I}
3. Вес второго квадрата: {weight_II}
4. Нормированный(на четверть площади) вес черного: {relative_weight_II}
5. Вес третьего квадрата: {weight_III}
6. Нормированный(на четверть площади) вес черного: {relative_weight_III}
7. Вес четвертого квадрата: {weight_IV}
8. Нормированный(на четверть площади) вес черного: {relative_weight_IV}
9. Центр масс: ({center_x}, {center_y})
10. Нормированный центр масс: ({relative_center_x}, {relative_center_y})
11. Моменты инерции: ({inertia_x}, {inertia_y})
12. Нормированные моменты инерции: ({relative_inertia_x}, {relative_inertia_y})
"""

letter_names = {
    "ბ": "ба́ни",
    "ზ": "зéни",
    "პ": "па́ри",
    "ს": "са́ни",
    "ქ": "ка́ни",
    "ჭ": "ча́ри"
}

letters_content = []

for idx, (_, row) in enumerate(df.iterrows(), start=1):
    if row["letter"] in letter_names:
        letter_data = {
            "letter": row["letter"],
            "name": letter_names[row["letter"]],  # Используем правильное имя для каждой буквы
            "index": idx,  # Используем порядковый номер строки
            "weight_I": row["weight_I"],
            "relative_weight_I": row["relative_weight_I"],
            "weight_II": row["weight_II"],
            "relative_weight_II": row["relative_weight_II"],
            "weight_III": row["weight_III"],
            "relative_weight_III": row["relative_weight_III"],
            "weight_IV": row["weight_IV"],
            "relative_weight_IV": row["relative_weight_IV"],
            "center_x": row["center_x"],
            "center_y": row["center_y"],
            "relative_center_x": row["relative_center_x"],
            "relative_center_y": row["relative_center_y"],
            "inertia_x": row["inertia_x"],
            "inertia_y": row["inertia_y"],
            "relative_inertia_x": row["relative_inertia_x"],
            "relative_inertia_y": row["relative_inertia_y"],
        }

        letters_content.append(letter_template.format(**letter_data))


letters_content = "\n".join(letters_content)

new_content = template.format(letters=letters_content)

with open("README_updated.md", "w", encoding="utf-8") as file:
    file.write(new_content)

print("Новый файл README_updated.md успешно создан!")