##ARQUIVO COM AS FUNCOES


# List[Mao] -> Mao
def poker(maos):
    return max(maos, key=pontuacao_mao)

# Mao -> Integer
def pontuacao_mao(mao):

    valores = pega_valores(mao)
    naipes = pega_naipes(mao)

    if straight(valores) and flush(naipes):
        return 10
    elif mesmo_tipo(valores,4):
        return 9
    elif mesmo_tipo(valores,3):
        return 5

# List[Valor] -> Boolean
def mesmo_tipo(valores,quantos):
    cont=0
    for i in range(len(valores)):
        if valores[i] == valores[i+1]:
            cont+=1
        else: break
    if cont == quantos-1:
        return True
    return False


# Mao -> List[alor]
def pega_valores(mao):
    valores = ["--23456789DJQKA".index(carta[0]) for carta in mao]

    # valores = []
    # for carta in mao:
    #     valor = carta[0]
    #     if valor == "D":
    #         valor = 10
    #     elif valor == "J":
    #         valor = 11
    #     elif valor == "Q":
    #         valor = 12
    #     elif valor == "K":
    #         valor = 13
    #     elif valor == "A":
    #         valor = 14
    #     valores.append(int(valor))
    valores.sort(reverse=True)
    return valores


def pega_naipes(mao):
    return [carta[1] for carta in mao]

def straight(valores):
    return valores[0] - valores[-1] == 4 and len(set(valores)) == 5

def flush(naipes):
    return len(set(naipes)) == 1
