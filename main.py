class RectCorrectError(list):
    pass

def isCorrectRect(list):
    if list[0][0] >= list[1][0] or list[0][1] >= list[1][1]:
        return False
    else:
        return True