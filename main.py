from lexico import SifraLexer
from sintatico import SifraParser

if __name__ == '__main__':
    lexer = SifraLexer()
    parser = SifraParser()

    print('Digite comandos para serem analisados. Digite "exit" para sair.')

    while True:
        comando = input('Comando: ')
        if comando.strip().lower() == 'exit':
            print('Encerrando o analisador.')
            break

        result = parser.parse(lexer.tokenize(comando))
        print('Resultado:', result)