# 🔐 Compilador de Cifras com Vigenère (Usando SLY)

## 📈 Trabalho de Compiladores (2025.1)

**Professora:** Myrna Amorim

**Grupo:** Ana Clara da Costa Souza, Guilherme Felippe da Silva Boiko, Thiago Conceição de Souza, e Renan Alves Lima

Este projeto implementa um compilador para comandos de **criptografia e descriptografia** usando a **cifra de Vigenère**, sensível a letras maiúsculas e minúsculas (*case sensitive*), com suporte a **frases completas** como chave e texto.

## 🛠️ Tecnologias usadas

- [Python 3](https://www.python.org/)
- [SLY (Simple Lexer & Parser)](https://sly.readthedocs.io/en/latest/index.html)

---

## 🔤 Léxico da Linguagem

- Palavras-chave:
  - `CRYPTO`: cifra uma mensagem usando uma chave
  - `DESCRYPTO`: decifra uma mensagem usando uma chave
  - `USING`: separador entre argumentos
- `TEXT`: deve ser uma **string entre aspas (`"`)**, podendo conter **espaços, números e sinais de pontuação**.

---

## 📜 Sintaxe da Linguagem

A linguagem aceita comandos de **criptografia** (`CRYPTO`) e **descriptografia** (`DESCRYPTO`), com a seguinte gramática:

```
S → C F USING F
F → S | TEXT
C → CRYPTO | DESCRYPTO
```

---

## ⚙️ Semântica da Linguagem

| Produções         | Ações                                         |
| ----------        | -------------------------                     |
| S → C F0 USING F1 | S.value = C.function (F0.value, F1.value)     |
| F → S             | F.value = S.value                             |
| F → TEXT          | F.value = TEXT                                |
| C → CRYPTO        | C.function = cifra_vigenere                   |
| C → DESCRYPTO     | C.function = decifra_vigenere                 |

## 🧪 Exemplos de uso

### Cifrar uma mensagem

```
CRYPTO "mensagem secreta" USING "palavra-chave"
```

### Decifrar a mensagem

```
DESCRYPTO "beysvxem zexvtip" USING "palavra-chave"
```

> ❗ Importante: A cifra é sensível a maiúsculas e minúsculas. Ou seja, `"Chave"` e `"chave"` são tratadas de forma diferente.

---

## ⚙️ Como executar

### 1. Instale o SLY:

```bash
pip install sly
```

### 2. Estrutura esperada dos arquivos

```
.
├── lexico.py         # Lexer (SifraLexer)
├── sintatico.py      # Parser (SifraParser)
├── vigenere.py       # Implementação da cifra
└── main.py           # Execução do compilador
```

### 3. Use o lexer e o parser da linguagem

```
lexer = SifraLexer()
parser = SifraParser()
result = parser.parse(lexer.tokenize(comando))
```

## 💡 Observações

- Apenas letras de A–Z/a–z são cifradas. Caracteres como `ç`, `é`, `1`, `@`, etc., são mantidos como estão.
- A chave é repetida automaticamente para cobrir o tamanho da mensagem, como na cifra original de Vigenère.
- É possível aninhar comandos: `CRYPTO USING DESCRYPTO USING ...` (gramática suporta recursão com `F → S`).

---

## 📚 Fontes de referência

- [Cifra de Vigenère – Wikipédia](https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re)
- [SLY - Simple Lexer and Parser](https://sly.readthedocs.io/en/latest/index.html)

---
