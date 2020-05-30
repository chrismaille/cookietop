def only_numbers(value: str) -> str:
    return "".join([character for character in value if character.isdigit()])
