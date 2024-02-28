numbers = []

def interface():
    print(numbers)
    userInput = input("Enter number or operation: ")
    solution = 0
    if userInput == "+":
        for val in numbers:
            solution += val
        print(solution)
        interface()
    elif userInput == "-":
        solution = numbers[0]
        for val in numbers[1:]:
            solution -= val
        print(solution)
        interface()
    elif userInput == "*":
        solution = numbers[0]
        for val in numbers[1:]:
            solution *= val
        print(solution)
        interface()
    elif userInput == "/":
        solution = numbers[0]
        for val in numbers[1:]:
            solution /= val
        print(solution)
        interface()
    elif userInput == "cls":
        numbers.clear()
        interface()
    else:
        try:
            numbers.append(float(userInput))
            interface()
        except:
            print("Not a number!")
        finally:
            interface()

interface()
