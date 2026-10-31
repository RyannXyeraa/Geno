from dataclasses import dataclass

from .token_type import TokenType

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

    def __repr__(self) -> str:
        return (
            self.type.name +
            f"({self.value})" +
            f" {self.line}:{self.column}"
        )
