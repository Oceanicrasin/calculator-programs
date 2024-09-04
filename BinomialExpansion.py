def combination(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n
        denominator *= i
        n -= 1
    return numerator // denominator

def binomialExpansion(firstPower, xNum, yNum):

    expansion = []
    fPowerIncrement = firstPower

    for secondPower in range(firstPower + 1):
        coefficientMultiplier = combination(firstPower, secondPower)
        coefficient = coefficientMultiplier * ((xNum**fPowerIncrement)*(yNum**secondPower))
        fPowerIncrement -= 1

        term = str(coefficient) + "x^" + str(firstPower - secondPower) + "*y^" + str(secondPower)

        if firstPower-secondPower == 0:
            term = str(coefficient) + "y^" + str(secondPower)
        elif secondPower == 0:
            term = str(coefficient) + "x^" + str(firstPower)
        elif firstPower-secondPower == 1:
            term = str(coefficient) + "xy^" + str(secondPower)
        elif secondPower == 1:
            term = str(coefficient) + "x^" + str(firstPower - secondPower) + "*y"
        expansion.append(term)

    return " + ".join(expansion)


firstPower = int(input("Enter the power you need to expand by: "))
xNum = int(input("Enter the first number: "))
yNum = int(input("Enter the second number: "))

print(binomialExpansion(firstPower, xNum, yNum))
