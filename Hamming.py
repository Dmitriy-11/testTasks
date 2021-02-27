def getWeightHamming(binaryCode):
    weight = 0
    for bit in binaryCode:
        if bit == '1':
            weight += 1
    return weight


print(getWeightHamming('100010010110111101101'))
