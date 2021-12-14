def fizz_buzz(number_input: int) -> str:
    """generates fizzbuzz string

    Args:
        number_input (int): number input

    Returns:
        str: combination of fizz, buzz
    """
    output = ""
    if number_input % 15 == 0:
        output = "fizzbuzz"
    elif number_input % 5 == 0:
        output = "buzz"
    elif number_input % 3 == 0:
        output = "fizz"

    return str(output)
