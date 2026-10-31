import sys

from src.geno.frontend.lexer.token import Token
from src.geno.frontend.lexer.lexer import Tokenize

def Exit(code: int) -> None:
    if (code != 0):
        print(f"Code: {code}")

    sys.exit(code)

def Load(filepath: str) -> str:
    with open(filepath, 'r') as file:
        return file.read()

def Compile(content: str, filepath: str) -> None:
    tokens: list[Token] = Tokenize(content, filepath)

    for token in tokens:
        print(f"  - {token}")

def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Geno: No input files.")
        Exit(1)

    filepath: str = argv[1]
    content: str = Load(filepath)

    Compile(content, filepath)

if __name__ == "__main__":
    argv: list[str] = sys.argv
    main(argv)
