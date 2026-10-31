
from .token import Token
from .token_type import TokenType

from .constant import (
    is_space,
    is_identifier_open,
    is_identifier_part,
    is_digit
)
from .keyword import is_keyword

class Lexer:
    def __init__(
        self,
        text: str, filepath: str
    ) -> None:
        self.text: str = text
        self.filepath: str = filepath

        self.index: int = 0
        self.line: int = 1
        self.column: int = 1

        self.current_char: str = self.text[self.index]

        self.tokens: list[Token] = []

    def advance(self) -> None:
        self.index += 1
        self.column += 1

        if (self.current_char == '\n'):
            self.line += 1
            self.column = 1

        if self.index >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.index]

    def copy_position(self) -> tuple(int, int):
        line: int = self.line
        column: int = self.column

        return line, column

    def skip_whitespace(self) -> None:
        while (
            self.current_char is not None and
            is_space(self.current_char)
        ):
            self.advance()

    def make_identifier(self) -> None:
        result: str = ""

        line, column = self.copy_position()

        while (
            self.current_char is not None and
            is_identifier_part(self.current_char)
        ):
            result += self.current_char
            self.advance()

        token_type: TokenType = TokenType.IDENTIFIER
        if is_keyword(result):
            token_type = TokenType.KEYWORD

        self.tokens.append(Token(
            token_type,
            result,
            line, column
        ))

    def make_number(self) -> None:
        result: str = ""
        decimal_dot_count: int = 0

        line, column = self.copy_position()

        while (
            self.current_char is not None and
            is_digit(self.current_char)
        ):
            if (self.current_char == '.'):
                if (decimal_dot_count > 0):
                    break

                decimal_dot_count += 1

            result += self.current_char
            self.advance()

        if result.startswith('.'):
            result = '0' + result
        elif result.endswith('.'):
            result += '0'

        if decimal_dot_count > 0:
            self.tokens.append(Token(
                TokenType.FLOAT,
                float(result),
                line,
                column
            ))
        else:
            self.tokens.append(Token(
                TokenType.INTEGER,
                int(result),
                line,
                column
            ))

    def make_string(self) -> None:
        result: str = ""

        open_quote: str = self.current_char

        line, column = self.copy_position()

        self.advance()

        while (
            self.current_char is not None
        ):
            if self.current_char == open_quote:
                self.advance()

                if self.current_char in ["'", '"']:
                    raise SyntaxError(
                        f"StringError: {self.line}:{self.column}"
                    )

                self.tokens.append(Token(
                    TokenType.STRING,
                    str(result),
                    line, column
                ))

                return

            if self.current_char == '\n':
                raise SyntaxError(
                    f"StringError: {self.line}:{self.column}"
                )

            result += self.current_char
            self.advance()

        raise SyntaxError(
            f"StringError: unterminated string {self.line}:{self.column}"
        )

    def generate_tokens(self) -> list[Token]:
        while (self.current_char is not None):
            self.skip_whitespace()

            if self.current_char is None:
                break

            char = self.current_char

            if is_identifier_open(char):
                self.make_identifier()
            elif is_digit(char):
                self.make_number()
            elif char in ["'", '"']:
                self.make_string()

            elif char == "=":
                line, column = self.copy_position()
                self.tokens.append(Token(
                    TokenType.EQUAL,
                    "=",
                    line, column
                ))
                self.advance()

            else:
                raise Exception(
                    f"Illegal Characther: '{char}'\n" +
                    f"Line: {self.line}\n" +
                    f"Column: {self.column}"
                )

        return self.tokens

def Tokenize(content: str, filepath: str) -> list[Token]:
    lexer = Lexer(content, filepath)
    tokens: list[Token] = lexer.generate_tokens()

    return tokens
