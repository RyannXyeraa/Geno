import sys

def Exit(code: int) -> None:
    if (code != 0):
        print(f"Code: {code}")

    sys.exit(code)

def Load(filepath: str) -> str:
    with open(filepath, 'r') as file:
        return file.read()

def Compile(content: str) -> None:
    ...

def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Geno: No input files.")
        Exit(1)

    filepath: str = argv[1]
    content: str = Load(filepath)

    Compile(content)

if __name__ == "__main__":
    argv: list[str] = sys.argv
    main(argv)
