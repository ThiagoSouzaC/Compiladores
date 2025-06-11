
from sly import Lexer

class SifraLexer(Lexer):
    tokens = { CRYPTO, DESCRYPTO, USING, TEXT }

    ignore = ' \t'

    # ------------------------------------------
    # Definição dos tokes 
    # ------------------------------------------

    # Palavras reservadas
    CRYPTO = r'CRYPTO'
    DESCRYPTO = r'DESCRYPTO'
    USING = r'USING'

    # Regra para textos (mensagem e chave)
    TEXT = r'[a-zA-Z0-9]+'   
