import time
import pandas as pd

# Variáveis Globais
tabela = []
exp = [ "+", "-", "{", "}", "<", ">", "=", "%d", "%c", ",", "(", ")",'"']
palavras_reservadas = ["main", "scanf", "printf", "return",
                        "if", "else", "elif","for", "do", "while", "int", "char", "or"]

def split(word):
    return [char for char in word]

def separarAnalise(lexema):
    temp = split(lexema)
    result = ''
    for i in temp:
        if (i in exp) or (i == ';'):
            result += ' '+i+' '
        else:
            result += i
    novalista = result.split()
    analisarLexemas(novalista)

# Analisador de Lexemas
def analisarLexemas(listaDeLexemas):
    # Variáveis globais
    global tabela, exp, palavras_reservadas

    # Adicionar rótulos
    for lexema in listaDeLexemas:
        num = lexema.isnumeric()

        if lexema == ';':
            tabela.append([lexema, '$'])
            continue
        if lexema in exp:
            tabela.append([lexema, lexema])
            continue
        if lexema in palavras_reservadas:
            tabela.append([lexema, 'PR'])
            continue
        if num:
            tabela.append([lexema, 'NUM'])
            continue
        # Separar IDs de símbolos com ' ' e analisar os lexemas
        for i in lexema:
            if (i in exp) or (i == ';'):
                separarAnalise(lexema)
                break
            if i == lexema[-1]:
                tabela.append([lexema, 'ID'])
                break
    return tabela


# Imprimindo separador de lexemas
df = pd.DataFrame(tabela, columns = ['LEXEMA', 'ROTULO'])


