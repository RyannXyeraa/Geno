import string

WHITESPACE: str = [
    ' ',
    '\n',
    '\t'
]

LETTERS: str = string.ascii_letters
DIGITS: str = string.digits

IDENTIFIER_OPEN: str = LETTERS + '_'
IDENTIFIER_PART = IDENTIFIER_OPEN + DIGITS

def is_space(value: str) -> bool:
    return value in WHITESPACE

def is_identifier_open(value: str) -> bool:
    return value in IDENTIFIER_OPEN

def is_identifier_part(value: str) -> bool:
    return value in IDENTIFIER_PART

def is_digit(value: str) -> bool:
    return value in DIGITS + '.'
