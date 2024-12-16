def isCorrectRect(cor):
    if cor[0][0] >= cor[1][0] or cor[0][1] >= cor[1][1]:
        return False
    else:
        return True