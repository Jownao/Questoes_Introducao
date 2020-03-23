#não entendi se relação era quantidade ou todas informações do usuario , fiz pela mais simples
def linha():
    print('=-='*35)
resposta=0
idade=sexoF=sexoM=sexo=idadeH=homem=0
idadeMedia=0
homem40=mulherExp=0
experiencia=''
resposta=int(input('Digite seu número de inscrição:\n'))
while resposta >=0:
    nome=str(input('Digite o seu nome:\n'))
    idade=int(input('Digite a sua idade:\n'))
    sexo=int(input('Digite 1 para masculino e 2 para feminino:\n'))
    experiencia=int(input('Digite se possue ou não experiencia com 1 ou 2 respectivamente:\n'))

    if sexo == 1:
        sexoM+=1
        homem+=1
    elif sexo == 2:
        sexoF+=1
    if sexo == 1 and experiencia == 1:
        idadeH += idade
    if sexo == 1 and idade > 40 and experiencia == 2:
        homem40+=1
    if sexo == 2 and experiencia == 1:
        mulherExp+=1


    resposta=int(input('Digite seu número de inscrição:\n'))


idadeMedia=(idadeH/homem)
linha()
print(f'O número de candidatos do sexo feminino é {sexoF}, e do sexo masculino é {sexoM}.\n')
linha()
print(f'A idade média dos homens que ja têm experiência e do sexo masculino é de {idadeMedia}.\n')
linha()
print(f'A relação dos homens com mais de 40 anos que não possuem experiência no serviço é de\n{homem40}')
linha()
print(f'A relação das mulheres que já tem experiência no serviço é de:\n{mulherExp} .')
linha()
