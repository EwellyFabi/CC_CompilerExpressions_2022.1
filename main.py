import separador_lexemas as sep_lexemas
import analizador_lexico as analiz_lexico
import analizador_semantico as analiz_semant
import analizador_preditivo as analiz_pred
import time
import os

# lista para armazena os dados da analise sintatica
dados = []

def split(word):
    return [char for char in word]

def salvar_arquivo(nome, aux):
    with open(nome+'.txt', 'w') as arquivo:
        for i in aux:
            arquivo.write('{}\t\t{}\n'.format(i[0],i[1]))
        arquivo.close()

# Ler arquivo de texto
ref_arquivo = open('codigo.txt', 'r')

print('==========SEPARADOR DE LEXEMAS==========\n')
print('Lendo o arquivo\n')
time.sleep(1.5)

aux = []

with open('codigo.txt', 'r') as arquivo:
    # Criar lista de lexemas
    linha = arquivo.read()
    listaDeLexemas = linha.split()
    aux = sep_lexemas.analisarLexemas(listaDeLexemas)
    salvar_arquivo("1_analise_lexica",aux)
  
ref_arquivo.close()

print('=============ANALISE LEXICA=============\n')
time.sleep(1.5)

tokens = list(filter(lambda x: x[1]=='ID',aux))

for token in tokens:
    analiz_lexico.automato(token[0])
salvar_arquivo("2_analise_lexica",tokens)
print('Análise lexica concluida\n')
time.sleep(1.5)
    
ref_arquivo.close()

print('==============ANALISE SINTÁTICA===============\n')
print('=============ANALIZADOR PREDITIVO=============\n')
time.sleep(1.5)


# Criar lista de lexemas
linha = []
linha = listaDeLexemas
for l in linha:
    if l[0] in analiz_semant.tipo.keys():
        l.pop(0)
    if (len(l) == 1) or (l[1] != '='):
        l.clear()
linha  = list(filter(None, linha))
print(linha)

if(analiz_pred.automatoM(listaDeLexemas)):
    print('Analise Sintatica Concluida')

tokens = list(filter(lambda x: x[1]=='ID',aux))

for token in tokens:
    analiz_lexico.automato(token[0])
salvar_arquivo("3_analizador_pred",tokens)
print('Análise lexica concluida\n')
time.sleep(1.5)

analiz_pred.automatoM(str)