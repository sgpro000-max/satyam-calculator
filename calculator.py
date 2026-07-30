def press(expression, value):
    return expression + str(value)


def clear():
    return ""


def backspace(expression):
    return expression[:-1]


def calculate(expression):
    try:
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        result = str(eval(expression))
        return result
    except:
        return "Error"
