from enum import(
  auto,
  Enum,
  unique,
)
from pickle import INT
from token import LPAR
from typing import Literal, NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    EOF = auto()
    FUNCTION = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()

class Token(NamedTuple):
    token_type = TokenType
    Literal: str

    def __str__(self) -> str:
      return f'Type: {self.token_type}, Literal: {self.literal}'
