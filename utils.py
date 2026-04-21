def verificar_intersecao(conjunto_1,conjunto_2, intersecao):
    for i in conjunto_1:
        for j in conjunto_2:
            if i == j:
                intersecao.append(i)
    return intersecao