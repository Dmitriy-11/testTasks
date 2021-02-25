# Функция для получения N-ой строки треугольника Паскаля
# (без использования биномиального коэффициента)


def getPasTrianLine(N):

    if N > 1:
        lineTemp = [1, 1]
        line = []
        while len(line) != N + 1:
            line = [1, 1]
            for i in range(len(lineTemp) - 1):
                line.insert(line.__len__() - 1, lineTemp[i] + lineTemp[i + 1])
            lineTemp = line
        return line
    elif N == 1:
        return [1, 1]
    elif N == 0:
        return [1]


line = getPasTrianLine(2)
print(' '.join(str(x) for x in line))
