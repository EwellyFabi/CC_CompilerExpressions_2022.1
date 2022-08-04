def automatoM(str):
    #delimitador
    str = str+"$"
    
    #declarando a tabela sintatica
    m = [[9, 1, 9, 1, 9], [2, 9, 3, 9, 3], [9, 4, 9, 4, 9]]

    #declarando a pilha
    pilha = []

    #colocando o delimitador na pilha
    pilha.append("$")

    #colocando o simbolo sentencial na pilha
    pilha.append("E")

    #variaveis para indexação na matriz
    terminais = 0
    n_terminais = 0
    i = 0

    #recebera as produções
    prod = ''

    #percorrendo toda a sentença de avaliação
    
    for i in str:
        print(prod)
        if i == '=':
            terminais = 0
        elif i == '(':
            terminais = 1
        elif i == ')':
            terminais = 2
        elif i == 'v':
            terminais = 3
        elif i == '$':
            terminais = 4
        else:
            return False

        while(1):
            #pilha[-1] == topo da pilha
            if pilha[-1] == 'E': 
                n_terminais = 0
            elif pilha[-1] == 'F': 
                n_terminais = 1
            elif pilha[-1] == 'M':
                n_terminais = 2
            else:
                return False
            
            #escolhendo a produção a ser aplicada pela tabela sintatica
            n_prod = m[n_terminais][terminais]
            print("Não terminais =",n_terminais, "Terminais =",terminais)
            print("Produçao ",n_prod)
            
            #fazendo equivalencia entre a produção e ordem inversa e o seu número da tabela
            if n_prod == 1:
                prod =  "EM"
            elif n_prod == 2:
                prod =  "EM="
            elif n_prod == 3:
                prod =  "&"
            elif n_prod == 4:
                prod =  ")E("
            elif n_prod == 5:
                prod = "v"
            else:
                return False
            
            #aplicando a produção que leva para a string vazia
            if prod[0] == '&':
                pilha.pop()            
            
            #aplicando outros tipos de produções
            else:
                pilha.pop()
                for j in prod:
                    pilha.append(j)
            
            #verificando se há igualdade no topo da pilha e o caractere em analise
            if pilha[-1] == i: # i == str[index], mas como foi utilizado 'for i in str' i == str[index]
                #reconhecimento da sentença
                if pilha[-1] == '$':
                    return True
                
                #mudança de estado do automato
                else:
                    pilha.pop()
                    break


if __name__ == "__main__":
    
    print("|----> Digite a sentenca para reconhecimento:")
    sentenca = input()
    res = automatoM(sentenca)

    if res == True:
        print("|----> O automato reconheceu a sentenca")
    else:
        print("|----> O automato NAO reconheceu a sentenca ")
        

