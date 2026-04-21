from utils import *

while True:

    print("----- BEM VINDO AO INTERSEÇÃO COM PYTHON! ---\n[1] Iniciar\n[2] Sair")

    try:
        opcao = int(input("Digite um número equivalente a opção desejada:"))
    except ValueError as erro:
        print("Por favor, digite uma opção válida.")
        continue

    if opcao == 1:
        controle1 = True
        while controle1 == True:
            conjunto_1 = set(map(int, input("Digite os números do primeiro conjunto separados por espaço: ").split()))

            conjunto_2 = set(map(int, input("Digite os números do segundo conjunto separados por espaço: ").split()))

            intersecao = []   
            
            print(f"Conjunto 1:{conjunto_1}")
            print(f"Conjunto 2: {conjunto_2}")
            print(f"A interseção entre os conjuntos 1 e 2 é: {verificar_intersecao(conjunto_1,conjunto_2, intersecao)}")

            controle2 = True

            while controle2 == True:

                pergunta = input("Deseja descobrir a interseção de dois conjuntos novamente?s/n: ").lower()

                if pergunta == "s":
                    controle2 = False
                
                elif pergunta == "n":
                    print("Voltando para o menu...")
                    controle2 = False
                    controle1 = False

                else:
                    print("Por favor, digite s ou n.")

    elif opcao == 2:
        print("Você desejou sair...")
        break

    else:
        print("Por favor, digite uma opção válida.")
        continue