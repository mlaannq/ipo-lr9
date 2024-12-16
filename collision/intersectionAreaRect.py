def isCorrectRect(rectangles): #корректность
    for rect in rectangles:
        if len(rect) != 2 or len(rect[0]) != 2 or len(rect[1]) != 2:
            raise ValueError("Некорректный прямоугольник")
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Некорректные координаты прямоугольника")

def intersectionAreaRect(rectangles): #площадь пересеч
    area = 0
    try:
        isCorrectRect(rectangles)
    except ValueError as e:
        print(e)
        return 0

    n = len(rectangles)  #кол-во прямоуг
    is_intersection = False  #флаг на наличие пересечения

    for i in range(n):
        for j in range(i + 1, n):
            (x1, y1), (x2, y2) = rectangles[i]
            (x3, y3), (x4, y4) = rectangles[j]

            left = max(x1, x3) #границы
            top = min(y2, y4)
            right = min(x2, x4)
            bottom = max(y1, y3)

            width = right - left #ширина и высота
            height = top - bottom

            if width > 0 and height > 0: #площадь пересеч
                area += width * height
                is_intersection = True

    return area if is_intersection else 0  #возвращаем 0 если нет пересеч