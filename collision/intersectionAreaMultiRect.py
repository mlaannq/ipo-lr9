def isCorrectRect(rectangles): #корректность
    for rect in rectangles:
        if len(rect) != 2 or len(rect[0]) != 2 or len(rect[1]) != 2:
            raise ValueError("Некорректный прямоугольник")
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Некорректные координаты прямоугольника")

def get_intersection(rects): #координаты пересеч
    x1 = max(rect[0][0] for rect in rects)
    y1 = max(rect[0][1] for rect in rects)
    x2 = min(rect[1][0] for rect in rects)
    y2 = min(rect[1][1] for rect in rects)
    if x1 < x2 and y1 < y2:
        return [(x1, y1), (x2, y2)]
    return None

def area(rect): #площадь
    if not rect:
        return 0
    width = rect[1][0] - rect[0][0]
    height = rect[1][1] - rect[0][1]
    return width * height

def intersectionAreaMultiRect(rectangles): #площадь перечес нескольких прямоуг
    try:
        isCorrectRect(rectangles)
    except ValueError as e:
        print(e)
        return 0
    itog_area = 0
    all_intersections = [] #для пересеч

    num_rectangles = len(rectangles) #кол-во прямоуг
    for i in range(num_rectangles):
        for j in range(i + 1, num_rectangles):
            crossing = get_intersection([rectangles[i], rectangles[j]]) #пересеч между прямоуг
            if crossing:
                all_intersections.append(crossing)
    num_intersections = len(all_intersections) #кол-во найденных пересеч
    for k in range(1, num_intersections + 1):
        sign = (-1) ** (k + 1)
        for i in range(num_intersections):
            for j in range(i + 1, num_intersections):
                crossing = get_intersection([all_intersections[i], all_intersections[j]])
                if crossing:
                    itog_area += sign * area(crossing)

    return itog_area