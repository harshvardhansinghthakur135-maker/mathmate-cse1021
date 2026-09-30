"""Input validation helpers.

Course concepts: values and types (Unit 2), conditionals and while loops (Unit 3),
functions with parameters (Unit 2), lists (Unit 5).
Every user input goes through these functions so that bad input never reaches
the algorithm modules.
"""


def read_int(prompt, minimum=None, maximum=None):
    """Keep asking until the user enters a whole number inside [minimum, maximum]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Invalid input: please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"  Value must be at most {maximum}.")
            continue
        return value


def parse_int_list(text):
    """Convert text such as '4, 7 2' into [4, 7, 2]. Raises ValueError if invalid."""
    parts = text.replace(",", " ").split()
    if len(parts) == 0:
        raise ValueError("The list is empty. Enter at least one number.")
    numbers = []
    for part in parts:
        try:
            numbers.append(int(part))
        except ValueError:
            raise ValueError(f"'{part}' is not a whole number.")
    return numbers


def read_int_list(prompt):
    """Keep asking until the user enters a valid list of whole numbers."""
    while True:
        try:
            return parse_int_list(input(prompt))
        except ValueError as error:
            print(f"  Invalid input: {error}")


def read_text(prompt):
    """Read a non-empty line of text."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  Input cannot be empty.")
