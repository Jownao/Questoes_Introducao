#Questão 3
'''
def linha():
    print('=-='*20)

desc=0

produto = input('\nDigite o nome do produto:\n')
linha()
quant = float(input('\nDigite a quantidade do produto:\n'))
linha()
print('\nColoque "." em vez de "," Ex: 10.3')
preco = float(input('\nDigite o preço do produto:\n'))
linha()

if quant <= 10:
    desc= 0.00
elif quant <= 20:
    desc= 0.10
elif quant <= 50:
    desc= 0.20
else:
    desc= 0.25

total= quant*preco*(1-desc)

print(f'O produto comprado foi: {produto}.')
print(f'O total a pagar é {total}.')
'''
#Questão 4
'''
salario= float(input('Digite seu salário para obter o desconto do INSS:\n'))
inss=''
if salario < 200:
    inss= 8.0
elif salario <500:
    inss= 8.5
elif salario <1000:
    inss= 9.0
elif salario >=1000:
     inss= 9.5

print(f'O desconto do seu INSS é {inss} %.')
'''
#Questão 8
'''
numero=[]
numeros=1

while numeros !=30:
    numero.append(numeros)
    numeros+=1

soma=sum(numero)

print(f'A soma dos números entre 0 e 30 é {soma}.')
'''
#Questão 9
'''
import sys
quant=0
media=''
idades=[]
loop=True
while loop:
    resposta=(input('Você quer digitar sua idade ?(Responda com S ou N)\n'))
    if resposta == '1':
        idades.append(int(input('Digite sua idade:\n')))
        quant+=1
    if resposta == '0':
        sys.exit()


media=(sum(idades)/quant)

print(f'A média de idades foi: {media}')
'''
#QUestão 10
'''
numeros=[]
escolha=0
escolha=(int(input('Quantos números quer digitar ?\n')))
for i in range (escolha):
    i+=1
    numeros.append(int(input(f'Digite o número para posição {i}\n')))

max=max(numeros)
min=min(numeros)
soma=max+min
produto=max*min

print(f'O maior número foi {max} e o menor foi {min} a soma entre ele é {soma} e o produto é {produto}.')
'''
