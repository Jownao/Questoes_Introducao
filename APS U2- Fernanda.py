import os
nomeTime=[]
nomeTec=[]
pont=[]
quaTimes=cont=0
resposta=0
resposta=int(input(f'========== MENU ==========\n'+
      f'[1] Cadastrar Time \n'+
      f'[2] Cadastrar Jogo \n'+
      f'[3] Exibir Classificação \n'+
      f'[4] Exibir Time Campeão \n'+
      f'[5] Exibir Time Rebaixado\n'+
      f'[6] Encerrar Campeonato\n'))
os.system("cls")
while resposta != 6:
    if resposta == 1:
        nomeTemp=str(input('Digite o nome do time:\n')).upper()
        nomeTime.append(nomeTemp)
        #nomeTec.append(str(input('Digite o nome do técnico do time:\n')))
        quaTimes+=1
    elif resposta == 2:
        time1=input('Qual nome do primeiro time ?\n').upper()
        while time1 not in nomeTime:
            print('Time não cadastrado!')
            time1=input('Qual nome do primeiro time ?\n').upper()

        time2=input('Qual nome do segundo time ?\n').upper()
        while time2 not in nomeTime:
            print('Time não cadastrado!')
            time2=input('Qual nome do segundo time ?\n').upper()
        resultado=(int(input('Qual time ganhou, 1 ou 2 , 3 para empate ?')))
        #simulaão que deu errado
        if resultado == 1:
            print(f'Time {time1} Ganhou 3 pontos')
            pont.append(3)
            time1=time2=0

        elif resultado == 2:
            print(f'Time {time2} Ganhou 3 pontos')
            pont.append(3)
            time1=time2=0

        elif resultado ==3:
            print('Os dois times ganharam 1 ponto pelo empate')
            posição=nomeTime.index(time1)
            posição2=nomeTime.index(time2)
            #pont[posição]=+1
            #pont[posição2]=+1

        else:
            print('Opção inválida!')
    elif resposta == 3:
        print('Time ----- Pontos -')
        for i in range (quaTimes):
            #pela metade
            print(nomeTime[i],"---",pont[i])
    elif resposta == 4:
        time_max_ponto= max(pont)
        time_max_posicao=pont.index(time_max_ponto)
        campeão = nomeTime.index(time_max_posicao)
        print(f'O time campeão foi:')
    elif resposta == 5:
        print('O time rebaixado foi:')
    else:
        print('Opção invalida digite novamente!')

    resposta=int(input(f'========== MENU ==========\n'+
          f'[1] Cadastrar Time \n'+
          f'[2] Cadastrar Jogo \n'+
          f'[3] Exibir Classificação \n'+
          f'[4] Exibir Time Campeão \n'+
          f'[5] Exibir Time Rebaixado\n'+
          f'[6] Encerrar Campeonato\n'))
    os.system("cls")
for i in range (quaTimes):
    cont+=1
    print('Time-',cont,'-',nomeTime[i])

print('=== FIM ===')
