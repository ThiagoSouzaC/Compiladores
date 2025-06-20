class SifraVenegere:
    """
    Cifra de Vigenère
    * Usa uma palavra-chave para definir o deslocamento de cada letra
    * Substituição polialfabética
    * A palavra-chave é repetida para cobrir todo o texto
    * É case sensitive
    """

    """Função de criptografia sensível a maiúsculas e minúsculas (case-sensitive)"""
    def sifra(self, texto, chave):
        resultado = []
        tamanho_chave = len(chave)

        for i, letra in enumerate(texto):
            c = chave[i % tamanho_chave]
            if letra.isalpha() and letra.lower() in 'abcdefghijklmnopqrstuvwxyz':
                deslocamento = ord(c.lower()) - ord('a')
                base = ord('A') if letra.isupper() else ord('a')
                nova_letra = chr((ord(letra) - base + deslocamento) % 26 + base)
                resultado.append(nova_letra)
            else:
                resultado.append(letra)

        return ''.join(resultado)

    """Descriptografia sensível a maiúsculas e minúsculas (case-sensitive)"""
    def desifra(self, texto, chave):
        resultado = []
        tamanho_chave = len(chave)

        for i, letra in enumerate(texto):
            c = chave[i % tamanho_chave]
            if letra.isalpha() and letra.lower() in 'abcdefghijklmnopqrstuvwxyz':
                deslocamento = ord(c.lower()) - ord('a')
                base = ord('A') if letra.isupper() else ord('a')
                nova_letra = chr((ord(letra) - base - deslocamento) % 26 + base)
                resultado.append(nova_letra)
            else:
                resultado.append(letra)

        return ''.join(resultado)