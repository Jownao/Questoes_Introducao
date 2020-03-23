#QUESTÃO 02

lista_inscricoes = []
lista_nomes = []
lista_idades = []
lista_sexos = []
lista_experiencias = []
totalFeminino = 0
totalMasculino = 0
lista_idade_homens_experiencia = []

contador = 0

while True:
    print('Inscrição do {}º candidato:'.format(contador + 1))
    inscricao = int(input('Digite o número de inscrição: '))
    if inscricao < 0:
        break
    else:
        lista_inscricoes.append(inscricao)
        lista_nomes.append(input('Digite o nome: '))
        lista_idades.append(int(input('Digite a idade: ')))
        while True:
            sexo = (int(input('Sexo. Digite "1" para MASCULINO ou "2" para FEMININO: ')))
            if sexo == 1 or sexo == 2:
                lista_sexos.append(sexo)
                break
            else:
                print('Opção inválida! Digite novamente!')
        while True:
            experiencia = int(input('Experiência. Digite "0" para NÃO ou "1" para SIM: '))
            if experiencia == 0 or experiencia == 1:
                lista_experiencias.append(experiencia)
                break
            else:
                print('Opção inválida! Digite novamente!')
    print('_'*50)
    print('Digite um número NEGATIVO para encerar o programa!')
    contador += 1

for i in range(len(lista_inscricoes)):
    if lista_sexos[i] == 1:
        totalMasculino += 1
    else:
        totalFeminino += 1
    if lista_sexos[i] == 1:
        if lista_experiencias[i] == 1:
            lista_idade_homens_experiencia.append(lista_idades[i])
media = sum(lista_idade_homens_experiencia) / len(lista_idade_homens_experiencia)
print('_'*50)
print('{} candidatos do sexo feminino.\n{} candidatos do sexo masculino.'.format(totalFeminino, totalMasculino))
print('Média de idade dos homens que possuem experiência no serviço: {:.2f} anos.'.format(media))

print('_'*50,'\nRelação de homens com mais de 40 anos sem experiência no serviço:')
print('INSCRIÇÂO    NOME    IDADE')
for i in range(len(lista_inscricoes)):
    if lista_sexos[i] == 1:
        if lista_idades[i] > 40:
            if lista_experiencias[i] == 0:
                print('{:9}{:^12}{:^4}'.format(lista_inscricoes[i], lista_nomes[i], lista_idades[i]))

print('_'*50,'\nRelação de mulheres com experiência no serviço:')
print('INSCRIÇÂO    NOME    IDADE')
for i in range(len(lista_inscricoes)):
    if lista_sexos[i] == 2:
        if lista_experiencias[i] == 1:
            print('{:9}{:^12}{:^4}'.format(lista_inscricoes[i], lista_nomes[i], lista_idades[i]))
