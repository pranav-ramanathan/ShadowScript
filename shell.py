from lexer import Lexer
while True:
    text = input("ShadowScript: ")
    tokeniser = Lexer(text)
    tokens = tokeniser.tokenize()

    print(tokens)