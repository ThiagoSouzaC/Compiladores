from lexico import SifraLexer
from sintatico import SifraParser

if __name__ == '__main__':
    lexer = SifraLexer()
    parser = SifraParser()

    comando = 'DESCRYPTO CRYPTO mensagem USING chave USING chave'

    print('Comando:', comando)

    for tok in lexer.tokenize(comando):
        print('type=%r, value=%r' % (tok.type, tok.value))

   
    result = parser.parse(lexer.tokenize(comando))
    print('Resultado:', result)
    
    