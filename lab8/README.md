# Лабораторная работа №8. Текстурный анализ и контрастирование.
- Матрица длин серий (GLRLM)
- Расчет признаков GLNU и RLNU 
- Линейное контрастирование
- Матрицы длин серий(логарифмической нормировки) для полутоновых и контрастированных полутоновых изображений

##  Изображение кирпичной стены 
### Исходное:

![](src/kirp.png)

### Полутоновое:

![](results/semitone/kirp.png)

### Матрица длин серий

![](results/glrlm/0_kirp.png)

### Признаки
GLNU: 3028.87

RLNU: 188174.10

### Гистограммы
![](results/histograms/kirp.png)

### Констрастированное полутоновое изображение
![](results/contrasted/kirp.png)

### Матрица длин серий для контрастированного изображения
![](results/glrlm_contrasted/0_kirp.png)

### Контрастированные признаки
GLNU (contrasted): 3133.83

RLNU (contrasted): 179682.02


##  Изображение узора с обоев
### Исходное:

![](src/oboi.png)

### Полутоновое:

![](results/semitone/oboi.png)

### Матрица длин серий

![](results/glrlm/0_oboi.png)

### Признаки
GLNU: 16804.51

RLNU: 684303.37

### Гистограммы
![](results/histograms/oboi.png)

### Констрастированное полутоновое изображение 
![](results/contrasted/oboi.png)

### Матрица длин серий для контрастированного изображения
![](results/glrlm_contrasted/0_oboi.png)

### Контрастированные признаки
GLNU (contrasted): 18294.07

RLNU (contrasted): 677160.98
##  Изображение поверхности Солнца
### Исходное:

![](src/sun.png)

### Полутоновое:

![](results/semitone/sun.png)

### Матрица длин серий

![](results/glrlm/0_sun.png)

### Признаки
GLNU: 18285.26

RLNU: 2966180.02

### Гистограммы
![](results/histograms/sun.png)

### Констрастированное полутоновое изображение 
![](results/contrasted/sun.png)

### Матрица длин серий для контрастированного изображения
![](results/glrlm_contrasted/0_sun.png)

### Контрастированные признаки
GLNU (contrasted): 18808.20

RLNU (contrasted): 2859456.97

## Выводы
Линейное контрастирование обычно уменьшает яркость изображения в целом, а так же иногда может помочь выделить текстуры объектов, несильно отличающихся по яркости. Матрица длин серий при этом меняется; параметр GLNU (Неоднородность яркости, Gray-level
nonuniformity), как правило, увеличивается, а параметр RLNU (Неоднородность длин серий, Run length
nonuniformity) уменьшается.
