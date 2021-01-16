puzzleInput = [1722, 1010, 300, 1337, 200, 299, 683]


def searchNumbers(): 
    i = 0
    desiredNumber = 2020
    print("Looking for your numbers... (╯°□°）╯︵ ┻━┻")

    for number1 in puzzleInput:
        for number2 in puzzleInput[i + 1:]:
            if number1 + number2 == desiredNumber:
                print("Got it! ┬─┬ ノ( ゜-゜ノ)")
                print("/", number1, "&", number2, "/")
                print("Now multiplying the numbers...")
                print("Here is your final number:", number1*number2)
                return [number1*number2]
        i += 1

searchNumbers()