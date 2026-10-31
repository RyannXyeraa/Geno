from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()

    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()

    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    EQUAL = auto()
    SEMICOLON = auto()
