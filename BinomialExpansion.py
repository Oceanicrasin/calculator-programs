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

def parseFraction(value):
    if "i" in value:
        numerator, denominator = map(int, value.split("i"))
        return numerator / denominator, (numerator, denominator)
    return float(value), (int(value), 1)

def simplifyFraction(numerator, denominator):
    a, b = numerator, denominator
    while b:
        a, b = b, a % b
    return numerator // a, denominator // a

def formatFraction(value, fractionTuple):
    numerator, denominator = simplifyFraction(fractionTuple[0], fractionTuple[1])
    if denominator == 1:
        return str(numerator)
    return str(numerator) + "/" + str(denominator)

def binomialExpansion(fPower, xCoeffStr, yCoeffStr):
    expansion = []

    xCoeff, xFraction = parseFraction(xCoeffStr)
    yCoeff, yFraction = parseFraction(yCoeffStr)

    for secondPower in range(fPower + 1):
        coefficientMultiplier = combination(fPower, secondPower)

        coefficient = coefficientMultiplier * ((xCoeff**(fPower - secondPower))*(yCoeff**secondPower))

        numerator = coefficientMultiplier * (xFraction[0] ** (fPower - secondPower)) * (yFraction[0] ** secondPower)
        denominator = (xFraction[1] ** (fPower - secondPower)) * (yFraction[1] ** secondPower)
        coefficientStr = formatFraction(coefficient, (numerator, denominator))

        if fPower-secondPower == 0:
            term = coefficientStr + "y^" + str(secondPower)
        elif secondPower == 0:
            term = coefficientStr + "x^" + str(fPower)
        elif fPower-secondPower == 1:
            term = coefficientStr + "xy^" + str(secondPower)
        elif secondPower == 1:
            term = coefficientStr + "x^" + str(fPower - secondPower) + "*y"
        else:
            term = coefficientStr + "x^" + str(fPower - secondPower) + "*y^" + str(secondPower)
        expansion.append(term)

    return " + ".join(expansion)


firstPower = int(input("Enter the power you need to expand by: "))
xNum = input("Enter the first number: ")
yNum = input("Enter the second number: ")

print(binomialExpansion(firstPower, xNum, yNum))
