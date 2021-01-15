puzzleInput = [1722, 1010, 300, 1337, 200, 299, 683]
i = 0
desiredNumber = 2020
summands = []
numbersFound = False

def checkForDesiredNumber(n1, n2):
    if n1 + n2 == desiredNumber:
        print("Got it!")
        numbersFound = True
        summands.append(n1)
        summands.append(n2)
        print(summands)
        return summands

for number1 in puzzleInput:
    for number2 in puzzleInput[i + 1:]:
        checkForDesiredNumber(number1, number2)
    i = i + 1
    print(i)




"""
for number1 in puzzleInput:
    for number2 in puzzleInput[i + 1:]:
        if number1 + number2 == desiredNumber:
            print("Got it!")
            summands.append(number1)
            summands.append(number2)
            break
    i = i + 1
"""