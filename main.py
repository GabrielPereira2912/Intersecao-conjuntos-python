conjunto_1 = set(map(int, input("Digite os números do primeiro conjunto separados por espaço: ").split()))

conjunto_2 = set(map(int, input("Digite os números do segundo conjunto separados por espaço: ").split()))

intersecao = []

def verificar_intersecao(conjunto_1,conjunto_2):
    for i in conjunto_1:
        for j in conjunto_2:
            if i == j:
                intersecao.append(i)
    return intersecao
    
print(f"Conjunto 1:{conjunto_1}")
print(f"Conjunto 2: {conjunto_2}")
print(f"A interseção entre os conjuntos 1 e 2 é: {verificar_intersecao(conjunto_1,conjunto_2)}")