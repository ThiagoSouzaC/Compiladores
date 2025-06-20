from sly import Parser
from lexico import SifraLexer
from vigenere import SifraVenegere

class SifraParser(Parser):
    tokens = SifraLexer.tokens
    vigenere = SifraVenegere()

    """"
    Análise sintática
        S → C F USING F
        F → S | TEXT
        C → CRYPTO | DESCRYPTO
    """

    """
    Análise semântica
    | Produções         | Ações                                         |
    | ----------        | -------------------------                     |
    | S → C F0 USING F1 | S.value = C.function (F0.value, F1.value)     |
    | F → S             | F.value = S.value                             |
    | F → TEXT          | F.value = TEXT                                |
    | C → CRYPTO        | C.function = cifra_vigenere                   |
    | C → DESCRYPTO     | C.function = decifra_vigenere                 |
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
    
    # C → CRYPTO (retorna a função de criptografia)
    @_('CRYPTO')
    def C(self, p):
        return self.vigenere.sifra
    
    # C → DESCRYPTO (retorna a função de descriptografia)
    @_('DESCRYPTO')
    def C(self, p):
        return self.vigenere.desifra