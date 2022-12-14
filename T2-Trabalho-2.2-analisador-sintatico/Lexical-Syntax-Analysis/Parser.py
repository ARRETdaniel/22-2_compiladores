import sys
from Lexer import *

next_token = None
l = None


def expr():
    global next_token
    global l
    print("Enter <expr>")
    term()
    while next_token.get_token().value == TokenTypes.ADD.value or \
            next_token.get_token().value == TokenTypes.SUB.value:
        next_token = l.lex()
        term()
    print("Exit <expr>")


# factor
# Parses strings in the language generated by the rules:
# <factor> -> ID
# <factor> -> INT_CONSTANT
# <factor> -> ( <expr> )
def factor():
    global next_token
    global l
    print("Enter <factor>")
    if next_token.get_token().value == TokenTypes.ID.value or \
       next_token.get_token().value == TokenTypes.INT.value:
        next_token = l.lex()
    else:  # if the RHS is ( <expr> ), pass over (, call expr, check for )
        if next_token.get_token().value == TokenTypes.LPAREN.value:
            next_token = l.lex()
            expr()
            if next_token.get_token().value == TokenTypes.RPAREN.value:
                next_token = l.lex()
            else:
                error("Expecting RPAREN")
                sys.exit(-1)
        else:
            error("Expecting LPAREN")
            sys.exit(-1)
    print("Exit <factor>")


def error(s):
    print("SYNTAX ERROR: "+s)


# term
# Parses strings in the language generated by the rule:
# <term> : <factor> {(*|/) <factor>}


def term():
    global next_token
    global l
    print("Enter <term>")
    factor()
    while next_token.get_token().value == TokenTypes.MUL.value or \
            next_token.get_token().value == TokenTypes.DIV.value:
        next_token = l.lex()
        factor()
    print("Exit <term>")


# expr
# Parses strings in the language generated by the rule:
# <expr> : <term> {(+|-) <term>}


def main():
    global next_token
    global l
    l = Lexer(sys.argv[1])
    next_token = l.lex()

    expr()
    if next_token.get_token().value == TokenTypes.EOF.value:
        print("PARSE SUCCEEDED")
    else:
        print("PARSE FAILED")


main()
