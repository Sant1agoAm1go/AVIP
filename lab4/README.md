# Лабораторная работа №4. Выделение контуров на изображении.
Использовались оператор Круна и градиентная матрица $`G = |G_x| + |G_y|`$
## Кадр из мультфильма
Исходное изображение:

<img src="pictures_src/cartoon_semitone.png" width="512">

Градиент по Х:

<img src="pictures_results/cartoon_G_x.png" width="512">

Градиент по Y:

<img src="pictures_results/cartoon_G_y.png" width="512">

Градиентная матрица G:

<img src="pictures_results/cartoon_G.png" width="512">

Бинаризованная градиентная матрица G (Глобальная бинаризация, порог 15):

<img src="pictures_results/cartoon_G_b.png" width="512">

Бинаризованная градиентная матрица G (Саувола):

<img src="pictures_results/cartoon_G_b_sauvola15.png" width="1024">



## Кадр из игры
Исходное изображение:

![](pictures_src/kcd2_semitone.png)

Градиент по Х:

![](pictures_results/kcd2_G_x.png)

Градиент по Y:

![](pictures_results/kcd2_G_y.png)

Градиентная матрица G:

![](pictures_results/kcd2_G.png)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 30):

![](pictures_results/kcd2_G_b30.png)

Бинаризованная градиентная матрица G(Саувола):

![](pictures_results/kcd2_G_b_sauvola.png)


## Фото человеческого лица
Исходное изображение:

![](pictures_src/gorshok_semitone.png)

Градиент по Х:

![](pictures_results/gorshok_G_x.png)

Градиент по Y:

![](pictures_results/gorshok_G_y.png)

Градиентная матрица G:

![](pictures_results/gorshok_G.png)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 15):

![](pictures_results/gorshok_G_b.png)

Бинаризованная градиентная матрица G(Саувола):

![](pictures_results/gorshok_G_b_sauvola.png)


## Фото текста
Исходное изображение:

![](pictures_src/staroslav_semitone.png)

Градиент по Х:

![](pictures_results/staroslav_G_x.png)

Градиент по Y:

![](pictures_results/staroslav_G_y.png)

Градиентная матрица G:

![](pictures_results/staroslav_G.png)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 45):

![](pictures_results/staroslav_G_b45.png)

Бинаризованная градиентная матрица G(Саувола):

![](pictures_results/staroslav_G_b_sauvola.png)


## Выводы
Алгоритм выделения контуров оператором Круна хорошо себя показывает для векторных и мультяшных изображений, но не очень 
хорошо работает для фотографий с изображениями людей и рукописным текстом. Ещё его не стоит использовать в случае если 
бинаризованное изображение получено методом Сауволы (для всех изображений видно, что выделение контуров намного лучше 
работает при глобальной пороговой бинаризации, потому что нет лишних шумов, как на изображении текста или лица человека).
