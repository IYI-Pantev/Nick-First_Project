def simple_calculator(operator: str, number_one: float, number_two: float):
    if operator == "multiply":
        return number_one * number_two
    elif operator == "divide":
        return number_one / number_two
    elif operator == "add":
        return number_one + number_two
    elif operator == "subtract":
        return number_one - number_two


oper = input()
num1 = float(input())
num2 = float(input())

print(simple_calculator(oper,num1, num2))
