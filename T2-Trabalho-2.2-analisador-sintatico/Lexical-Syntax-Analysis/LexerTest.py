from Lexer import *
from TokenTypes import *


def main():

    input = "(sum + 47) / total"
    lexer = Lexer(input)
    print("Tokenizing ", end="")
    print(input)
    while True:
        t = lexer.lex()
        if t.get_token().value == TokenTypes.EOF.value:
            break


main()
