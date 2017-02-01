''' This program approximates the root of a nth-degree polynomial using
    Newton's Method. Copyright 2017 Matthew Sedam. '''
    
    
''' Takes a coefficientList, a list of the coefficients of the n-th
        degree polynomial including the constant term starting with the highest
        degree term, and value, the value that the function will be evaluated
        at. '''
def calculateFunctionAtValue(coefficientList, value):  
    degreeOfPolynomial = len(coefficientList) - 1
    returnValue = 0
    if value == 0:
        return coefficientList[-1]
    for i in range(len(coefficientList)):
        returnValue += coefficientList[i] * (value ** (degreeOfPolynomial - i))
    return returnValue

''' Takes a coefficientList, a list of the coefficients of the n-th
        degree polynomial including the constant term starting with the highest
        degree term, and value, the value that the derivative will be evaluated
        at. '''
def calculateDerivativeAtValue(coefficientList, value):
    degreeOfPolynomial = len(coefficientList) - 1
    returnValue = 0
    if degreeOfPolynomial == -1:
        return 0
    elif degreeOfPolynomial == 0:
        return 0
    elif degreeOfPolynomial == 1:
        return coefficientList[-2]
    else:
        for i in range(len(coefficientList) - 1):
            returnValue += (degreeOfPolynomial - i) * coefficientList[i] * (value ** (degreeOfPolynomial - i - 1))
        return returnValue

''' Calculates the x-value that gives y = 0, where y is the tangent line to
        the function at the certain value. '''
def calculateTangentLineRoot(functionValue, derivativeValue, value):
    return ((-1 * functionValue) / derivativeValue) + value

''' Uses Newton's Method to approximate the root of a polynomial with
        coefficients in coefficientList including the constant term starting
        with the highest degree term with an initial guess (x-value) of
        initialGuess, which has to be reasonable for a good approximation, and
        iterating numberOfIterations times. '''
def newtonmethod(initialGuess, coefficientList, numberOfIterations):
    root = initialGuess
    for _ in range(numberOfIterations):
        root = calculateTangentLineRoot(calculateFunctionAtValue(coefficientList, root), calculateDerivativeAtValue(coefficientList, root), root)
    return root
