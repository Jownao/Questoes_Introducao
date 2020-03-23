lista_times = []
lista_tecnicos = []
lista_pontos = []
lista_placar = []

inscricoes = 0

print('''1 - Cadastrar Time
2 - Cadastrar Jogo
3 - Exibir Classificação
4 - Exibir Time Campeão
5 - Exibir Time Rebaixado
6 - Encerrar Campeonato''')

while True:
    print('_'*50,'\nEscolha um aopção entre "1" e "6"!')
    menu = int(input('Digite a opção do menu: '))
    if 1 <= menu <= 6:
        if menu == 1:
            while inscricoes != 8:
                print('_'*50,'\nCadastro de time.')
                lista_times.append(input('Digite o nome do {}º time: '.format(inscricoes + 1)))
                lista_tecnicos.append(input('Digite o nome do técnico responsável: '))
                lista_pontos.append(0)
                lista_placar.append(0)
                inscricoes += 1
                if inscricoes < 8:
                    print('{} vagas disponiveis.'.format(8 - (inscricoes)))
                    continuar = int(input('Deseja continuar cadastrando times? "0" - NÂO, "1" - SIM: '))
                    if continuar == 0:
                        break
        elif menu == 2:
            print('_'*50,'\nCadastro de jogo.')
            while True:
                time_01 = input('Digite o nome do 1º time: ')
                if time_01 in lista_times:
                    gols_01 = int(input('Digite a quantidade de gols feitos pelo time {}: '.format(time_01)))
                    posicao_01 = lista_times.index(time_01)
                    lista_placar[posicao_01] += gols_01
                    break
                else:
                    print('Time não cadastrado! Por favor, digite novamente!')
                    print(  'Tiems cadastrados:\n{}'.format(lista_times))
            while True:
                time_02 = input('Digite o noem do 2º time: ')
                if time_02 in lista_times:
                    gols_02 = int(input('Digite a quantidade de gols feitos pelo time {}: '.format(time_02)))
                    posicao_02 = lista_times.index(time_02)
                    lista_placar[posicao_02] += gols_02
                    break
                else:
                    print('Time não cadastrado! Por favor, digite novamente!')
                    print('Tiems cadastrados:\n{}'.format(lista_times))
                if lista_placar[posicao_01] > lista_placar[posicao_02]:
                    lista_pontos[posicao_01] += 3
                elif lista_placar[posicao_02] > lista_placar[posicao_01]:
                    lista_pontos[posicao_02] += 3
                else:
                    lista_pontos[posicao_01] += 1
                    lista_pontos[posicao_02] += 1
            lista_placar[posicao_01] = 0
            lista_placar[posicao_02] = 0
        elif menu == 3:
            print('_'*50,'\nClassificação.')
            print('Time     Técnico responsável     Pontos acumulados')
            for i in range(len(lista_times)):
                print('{:9}{:21}{:10}'.format(lista_times[i], lista_tecnicos[i], lista_pontos[i]))
        elif menu == 4:
            campeao = max(lista_pontos)
            posicao_capeao = lista_pontos.index(campeao)
            percentual_campeao = lista_pontos[posicao_capeao] * (sum(lista_pontos) / 100)
            print('O time campeão é {}, técnico {}, com {} pontos.'.format(lista_times[posicao_capeao], lista_tecnicos[posicao_capeao], lista_pontos[posicao_capeao]))
            print('O percentual de pontos, com relação oa campeonato é de: {}%'.format((percentual_campeao)))
        elif menu == 5:
            rebaixado = min(lista_pontos)
            posicao_rebaixado = lista_pontos.index(rebaixado)
            percentual_rebaixado = lista_pontos[posicao_rebaixado] * (sum(lista_pontos) / 100)
            print('O time rebaixado é {}, técnico {}, com {} pontos.'.format(lista_times[posicao_rebaixado], lista_tecnicos[posicao_rebaixado], lista_pontos[posicao_rebaixado]))
            print('O percentual de pontos, com relação oa campeonato é de: {}%'.format(percentual_rebaixado))
        else:
            print('_'*50,'\nClassificação.')
            print('Time     Técnico responsável     Pontos acumulados')
            for i in range(len(lista_times)):
                print('{:9}{:21}{:10}'.format(lista_times[i], lista_tecnicos[i], lista_pontos[i]))
            break
    else:
        print('_'*50,'\nOpção inválida. Tente novamente!')
