from collision.isCorrectRect import isCorrectRect
from collision.intersectionAreaRect import intersectionAreaRect
from collision.isCollisionRect import isCollisionRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect

def main():
    while True:
        number = int(input("Выбор: 1 - intersectionAreaRect , 2 - isCorrectRect , 3 - isCollisionRect , 4 - intersectionAreaMultiRect , 5 - Выход\n"))
        if number == 1:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [((x1, y1), (x2, y2)), ((x3, y3), (x4, y4))]
            print("Площадь пересечения: ", intersectionAreaRect(rectangles))

        elif number == 2:
            rectangles = []
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rectangles.append([(x1, y1), (x2, y2)])
            try:
                isCorrectRect(rectangles)
                print("Прямоугольник корректный")
            except ValueError as e:
                print(e)

        elif number == 3: #проверка на пересеч прямоугольников
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [((x1, y1), (x2, y2)), ((x3, y3), (x4, y4))]
            collision_result = isCollisionRect(rectangles)
            print("Пересечение: ", collision_result)

        elif number == 4: #вычисление площади пересеч
            n = int(input("Количество прямоугольников: "))
            rectangles = []
            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                rectangles.append([(x1, y1), (x2, y2)])
            try:
                area = intersectionAreaMultiRect(rectangles)
                print("Общая площадь пересечения:", area)
            except ValueError as e:
                print(e)

        elif number == 5:
            print("Выход из программы")
            break
        else:
            print(f"Вы ввели {number}, чтобы продолжить введите число от 1 до 5")

if __name__ == "__main__":
    main()