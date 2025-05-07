from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'full_house': -1,
        'quadra': -1,
        'cinco_iguais': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'sem_combinacao': -1
    }
}

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    jogada_feita = False

    while not jogada_feita:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            lista_temporaria = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = lista_temporaria[0]
            dados_guardados = lista_temporaria[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            lista_temporaria = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = lista_temporaria[0]
            dados_guardados = lista_temporaria[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()

        elif opcao == "4":
            imprime_cartela(cartela)
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()

        elif opcao == "0":
            print("Digite a combinação desejada:")
            categoria = input()
            jogada_valida = False

            if categoria.isdigit():
                categoria_int = int(categoria)
                if categoria_int in cartela['regra_simples']:
                    if cartela['regra_simples'][categoria_int] == -1:
                        jogada_valida = True
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            elif categoria in cartela['regra_avancada']:
                if cartela['regra_avancada'][categoria] == -1:
                    jogada_valida = True
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")
                categoria = input()

            if jogada_valida:
                todos_os_dados = dados_rolados + dados_guardados
                cartela = faz_jogada(todos_os_dados, categoria, cartela)
                jogada_feita = True

        else:
            print("Opção inválida. Tente novamente.")
            opcao = input()

# fim do jogo
imprime_cartela(cartela)

pontos_simples = 0
pontos_avancados = 0

for valor in cartela['regra_simples'].values():
    if valor != -1:
        pontos_simples += valor

for valor in cartela['regra_avancada'].values():
    if valor != -1:
        pontos_avancados += valor

total = pontos_simples + pontos_avancados

if pontos_simples >= 63:
    total += 35

print(f"Pontuação total: {total}")
