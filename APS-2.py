def linha():
    print('=-='*15)
#Votos dos Candidatos
votosC1=0
votosC2=0
votosC3=0
votosC4=0
#código dos candidatos
c1=1
c2=2
c3=3
c4=4
#Nome dos candidatos
nome1='Raimundo'
nome2='Robinson'
nome3='Edinaldo'
nome4='Darkseid'
#Votos
total=0
validos=0
nulos=0
brancos=0
#Variáveis
resposta=0
voto=0
reposta=int(input('===================================\n'+
                  'Deseja executar a sessão eleitoral ?\n'+
                  '===================================\n'+
                  '[1] -> Sim\n'+
                  '[-1] -> Não\n'+
                  '===================================\n\n'))
vencedor = -9999999
nomeVencedor=''
codigoVencedor=0

while resposta != -1:
    voto=int(input('Digite o código do seu canditado:\n'))
    tituloEleitor=int(input('Digite seu título de eleitor:\n'))
    nomeEleitor=input('Digite o seu nome:\n')
    if voto == c1:
        votosC1+=1
        total+=1
        validos+=1
    if voto == c2:
        votosC2+=1
        total+=1
        validos+=1
    if voto == c3:
        votosC3+=1
        total+=1
        validos+=1
    if voto == c4:
        votosC4+=1
        total+=1
        validos+=1
    if voto == 0:
        nulos+=1
        total+=1
    if voto != 1 and voto != 2 and voto != 3 and voto != 4 and voto != 0:
        brancos+=1
        total+=1
    resposta=int(input('===================================\n'+
                      '             Finalizar ?            \n'+
                      '====================================\n'+
                      '[1] -> Sim                          \n'+
                      '[-1] -> Fechar sessão               \n'+
                      '====================================\n\n'))
if votosC1 > vencedor:
    vencedor=votosC1
    nomeVencedor=nome1
    codigoVencedor=c1
if votosC2 > votosC1:
    vencedor=votosC2
    nomeVencedor=nome2
    codigoVencedor=c2
if votosC3 > votosC2 and votosC3 > votosC1:
    vencedor=votosC3
    nomeVencedor=nome3
    codigoVencedor=c3
if votosC4 > votosC3 and votosC4 > votosC2 and votosC4 > votosC1 :
    vencedor=votosC4
    nomeVencedor=nome4
    codigoVencedor=c4


print(f'= Código == Nome do Candidato == Votos =\n'+
      f'= {c1}    ==     {nome1}       ==    {votosC1} votos =\n'+
      f'= {c2}    ==     {nome2}       ==    {votosC2} votos =\n'+
      f'= {c3}    ==     {nome3}       ==    {votosC3} votos =\n'+
      f'= {c4}    ==     {nome4}       ==    {votosC4} votos =\n\n')

linha()

percentualV= (vencedor/validos) * 100
percentualB= (brancos/total) * 100
percentualN= (nulos/total) * 100

print(f'Votos nulos {nulos} , votos brancos {brancos}  ,  votos válidos {validos} , votos totais {total}')

print(f'==== Tabela do Vencedor ====                            \n'+
      f'Código: {codigoVencedor}                                \n'+
      f'Nome do Candidato:  {nomeVencedor}                      \n'+
      f'Percentual em relação aos votos válidos: {percentualV}% \n\n')

print(f'==== Percentual de votos brancos em relação ao total ====\n'+
      f'                    {percentualB}%                       \n')

print(f'==== Percentual de votos nulos em relação ao total ====\n'+
      f'                    {percentualN}%                     \n')

print('Fim.')
