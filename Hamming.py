def getWeightHamming(binaryCode):
    weight = 0
    for bit in binaryCode:
        if bit == '1':
            weight += 1
    return weight


def getBinaryCode(str):
    if str.isdigit():
        return bin(int(str))[2:]
    else:
        return ' '.join(map(bin, bytearray(str, 'utf8'))).replace('0b', '')


inp = input("Enter string or number: ")
binaryCode = getBinaryCode(inp)
print(binaryCode)
print("Weight Hamming = ", getWeightHamming(binaryCode))
