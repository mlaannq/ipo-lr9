def isCollisionRect(rectangles):
    n = len(rectangles)

    for rect in rectangles:
        if len(rect) != 2 or len(rect[0]) != 2 or len(rect[1]) != 2:
            raise ValueError("Некорректный прямоугольник")
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Некорректные координаты прямоугольника")

    for i in range(n):
        for j in range(i + 1, n):
            (x1_min, y1_min), (x1_max, y1_max) = rectangles[i] #1
            (x2_min, y2_min), (x2_max, y2_max) = rectangles[j] #2

            left = max(x1_min, x2_min) #границы пересеч
            right = min(x1_max, x2_max)
            bottom = max(y1_min, y2_min)
            top = min(y1_max, y2_max)

            width = right - left #ширина и высота пересеч
            height = top - bottom

            if width > 0 and height > 0: #проверяем пересечение
                return True
    return False
