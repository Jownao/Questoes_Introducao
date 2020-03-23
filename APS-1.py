import time
def linha():
    print('=-='*15)

def contador():
    print('Reiniciando em 3 segundos')
    time.sleep(1)
    print('Reiniciando em 2 segundos')
    time.sleep(1)
    print('Reiniciando em 1 segundo')
    time.sleep(1)
    linha()

nome_Atleta=True
n_Atleta=1

while nome_Atleta != '':
    notas=[]
    print(f'Nome do atleta {n_Atleta}\n')
    nome_Atleta=input('Digite o nome do atleta:\n')
    if nome_Atleta == '':
        break
    else:
        n_Jurado= 1
        linha()
        for i in range(7):
            print(f'Jurado nº {n_Jurado}')
            nota= float(input('Digite a nota: '))
            notas.append(nota)
            n_Jurado+=1
        print(f'Atleta:',nome_Atleta)
        n_Jurado=1
        posição=0
        for i in range (7):
            print(f'{n_Jurado} ° Jurado: {notas[posição]}')
            n_Jurado+=1
            posição+=1
            linha()
        print(f'''Resultados:\n
        Nome do atleta: {nome_Atleta}\n
        Melhor nota: {max(notas)}
        Pior nota: {min(notas)}
        ''')
        linha()
        notas.remove(max(notas))
        notas.remove(min(notas))
        media=sum(notas)/len(notas)

        print(f'A média de notas foi: {media}.')

        n_Atleta+=1

        contador()
