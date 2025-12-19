def printNumbers1ToN(n):
    if n == 0:
        return n
    printNumbers1ToN(n-1)
    print(n)

def printNumbersNto1(n):
    if n == 0:
        return n
    print(n)
    printNumbersNto1(n-1)
    




printNumbers1ToN(5)
print("###########")
printNumbersNto1(5)