KEYWORDS = [
    "int",
    "string",
    "float",
    "bool"

    "const",

    "for",
    "while",

    "func",
    "class"
]

def is_keyword(value: str) ->  bool:
    return value in KEYWORDS
