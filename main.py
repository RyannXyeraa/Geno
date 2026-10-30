import sys

def Exit(code: int) -> None:
    if (code != 0):
        print(f"Code: {code}")

    sys.exit(code)

def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Geno: No input files.")
        Exit(1)

if __name__ == "__main__":
    argv: list[str] = sys.argv
    main(argv)
