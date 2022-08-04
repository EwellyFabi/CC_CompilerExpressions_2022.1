import string

# alfabeto
alfabeto = {'a': 0, 'b': 1, 'c': 2}
def verifica(i):
    if i.isalpha():
        return 'a'
    elif (i == '#'):
        return 'b'
    elif i.isalnum():
        return 'c'
    return i

def automato(lexema):
    M = [[1, 777, 2], [777, 2, 2], [777, 777, 2]]
    e = 0 #estado inicial
    for char in lexema:
        l  = verifica(char)
        #print(l)
        if l in alfabeto.keys():
            e = M[alfabeto[l]][e]
            if e == 777:
                print('Variavel nao declarada corretamente\n' + lexema)
                return False
        else:
            print('Simbolo nao aceito\n'+ char + ' em ' + lexema)
            return False
    
    '''Estado Final '''
    if e == 2:
        print('Variavel reconhecida: '+ lexema)
        return True
    else:
        print('Variavel nao reconhecida: ' + lexema)
        return False