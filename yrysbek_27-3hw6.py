def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_numbers(2, 3, 4, 5))


def is_palindrome(string, hello='hello'):
    if string == string[::-1]:
        return True
    elif string == hello:
        return "This is 'hello'"
    else:
        return False
print(is_palindrome('racecar')) # True
print(is_palindrome('hello')) # This is 'hello'
print(is_palindrome('world')) # False


def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid operator"

print(calculator(2, "**", 3)) # 8
print(calculator(5, "+", 9.6)) # 14.6
print(calculator(20, "%", 3)) # 2

