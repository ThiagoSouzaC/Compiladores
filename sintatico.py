from sly import Parser
from lexico import SifraLexer

class SifraParser(Parser):
    tokens = SifraLexer.tokens

    """
    Cifra de Vigenère
    * Usa uma palavra-chave para definir o deslocamento de cada letra
    * Substituição polialfabética
    * A palavra-chave é repetida para cobrir todo o texto
    * É case sensitive
    """

    def sifra(self, texto, chave):
        """Função que simula a criptografia"""
        resultado = []
        chave = chave.upper()
        texto = texto.upper()
        tamanho_chave = len(chave)

        for i, letra in enumerate(texto):
            if letra.isalpha():
                deslocamento = ord(chave[i % tamanho_chave]) - ord('A')
                nova_letra = chr((ord(letra) - ord('A') + deslocamento) % 26 + ord('A'))
                resultado.append(nova_letra)
            else:
                resultado.append(letra)

        return ''.join(resultado)
    
    def desifra(self, texto, chave):
        """Função que simula a descriptografia."""
        resultado = []
        chave = chave.upper()
        texto = texto.upper()
        tamanho_chave = len(chave)

        for i, letra in enumerate(texto):
            if letra.isalpha():
                deslocamento = ord(chave[i % tamanho_chave]) - ord('A')
                nova_letra = chr((ord(letra) - ord('A') - deslocamento) % 26 + ord('A'))
                resultado.append(nova_letra)
            else:
                resultado.append(letra)

        return ''.join(resultado)

    """"
    Análise sintática
        S → C F USING F
        F → S | TEXT
        C → CRYPTO | DESCRYPTO
    """
    
    # S → C F USING F (retorna a criptografia ou descriptografia)
    @_('C F USING F')
    def S(self, p):
        return p.C(p.F0, p.F1)
    
    # F → S 
    @_('S')
    def F(self, p):
        return p.S
    
    # F → TEXT
    @_('TEXT')
    def F(self, p):
        return p.TEXT
    
    # C → CRYPTO
    @_('CRYPTO')
    def C(self, p):
        return self.sifra
    
    # C → DESCRYPTO
    @_('DESCRYPTO')
    def C(self, p):
        return self.desifra


if __name__ == '__main__':
    lexer = SifraLexer()
    parser = SifraParser()

    while True:
        try:
            text = input('calc > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break
