file = open("door1.txt")
list_of_stringy_numbers = file.read().split()
puzzle_input = list(map(int, list_of_stringy_numbers))
desired_number = 2020
    

def searchNumbers(puzzle_input, desired_number): 
    i = 0
    for number1 in puzzle_input:
        for number2 in puzzle_input[i + 1:]:
            if number1 + number2 == desired_number:
                return [number1, number2]
        i += 1

def multiplyNumbers(n1, n2):
    return n1*n2


print("Looking for your numbers... (╯°□°）╯︵ ┻━┻")
if searchNumbers(puzzle_input, desired_number):
    numbers_to_multiply = searchNumbers(puzzle_input, desired_number)
    print("Got it! ┬─┬ ノ( ゜-゜ノ)")
    print("/", numbers_to_multiply[0], "&", numbers_to_multiply[1], "/")
    print("Now multiplying the numbers...")
    print("Here is your final number:", multiplyNumbers(numbers_to_multiply[0], numbers_to_multiply[1]))
else:
    print("Couldn't find matching numbers. (╯°□°）╯︵ ┻━┻")