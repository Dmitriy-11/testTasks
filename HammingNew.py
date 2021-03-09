def getWeightHamming(decNumbers):
    weight = 0
    for dec_number in decNumbers:
        while dec_number != 0:
            weight += (dec_number % 2)
            dec_number //= 2
    return weight


def getDecNumber(str):
    if str.isdigit():
        return [str]
    else:
        lst_code_symb = []
        for s in str:
            lst_code_symb.append(ord(s))
        return lst_code_symb


inp = input("Enter string or number: ")
decNumbers = getDecNumber(inp)
print(decNumbers)
print("Weight Hamming = ", getWeightHamming(decNumbers))
