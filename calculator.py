def press(expression, value):
    return expression + str(value)


def clear():
    return ""


def backspace(expression):
    return expression[:-1]


def calculate(expression):
    if not expression:
        return ""

    try:
        expression = (
            expression
            .replace("×", "*")
            .replace("÷", "/")
            .replace("%", "/100")
        )

        result = eval(expression)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return str(result)

    except Exception:
        return "Error"
