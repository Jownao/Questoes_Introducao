import os

lista_matricula = []
lista_nome = []
lista_email = []
lista_telefone = []
lista_celular = []
lista_endereco = []
lista_numero = []
lista_complemento = []
lista_bairro = []
lista_cidade = []
lista_uf = []
lista_cargo = []
lista_salario = []
lista_setor = []
grupo_setor = []
total_setor = []
lista_salario_liquido = []
lista_inss = []
lista_irrf = []


def calcular_inss(salario):
    inss = 0
    if salario <= 1039:
        inss = salario * 0.075
    elif salario > 1039 and salario <= 2089.60:
        inss = salario * 0.09
    elif salario > 2089.60 and salario <= 3314.40:
        inss = salario * 0.12
    elif salario > 3314.40 and salario <= 6101.06:
        inss = salario * 0.14
    return inss

def calcular_irrf(salario):
    irrf = 0
    if salario <= 1903.98:
        irrf = 0
    elif salario >= 1903.99 and salario <= 2826.65:
        irrf = (salario * 0.075) + 142.80
    elif salario >= 2826.66 and salario <= 3751.05:
        irrf = (salario * 0.15) + 354.80
    elif salario >= 3751.06 and salario <= 4664.68:
        irrf = (salario * 0.225) + 636.13
    else:
        irrf = (salario * 0.275) + 869.36
    return irrf

def calcular_salario_liquido(salario):
    salario_liquido =  salario - (calcular_inss(salario) + calcular_irrf(salario))
    return salario_liquido

while True:
    print('_'*50)
    print('OPÇÕES:\n01 - Cadastro.\n02 - Listar Cadastros.\n03 - Listar Custo por Setor.\n04 - Encerar o Programa.')
    print('_'*50)
    opcao = int(input('Digite a opção:\n'))
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
        if opcao == 1:
            print('_' * 50)
            print('Cadastro.')
            matricula = int(input('Digite a matrícula, SOMENTE OS NÚMEROS:\n'))
            lista_matricula.append(matricula)
            nome = input('Digite o nome:\n').capitalize().strip()
            lista_nome.append(nome)
            print('_' * 50)
            print('Dados de Contato.')
            while True:
                email = input('Digite o e-mail:\n')
                if "@" in email:
                    lista_email.append(email)
                    break
                else:
                    print('E-mail inválido, por favor, tente novamente!')
            while True:
                telefone = input('Digite o telefone, SOMENTE NÚMEROS:\n')
                if len(telefone) >= 8:
                    lista_telefone.append(telefone)
                    break
                else:
                    print('O telefone deve ter no mínimo 8 digitos, por favor, tente novamente!')
            while True:
                opcao_celular = input(
                    'Desejá adicionar um telefone celular para contato?\nDigite: S para SIM ou N para NÃO:\n').strip().upper()
                if opcao_celular == 'S' or opcao_celular == 'N':
                    if opcao_celular == 'S':
                        celular = input('Digite o número do celular, SOMENTE NÚMEROS:\n')
                        break
                    else:
                        celular = 'xxxx-xxxx'
                        break
                else:
                    print('Opção inválida, por favor, tente novamente!')
            lista_celular.append(celular)
            print('_' * 50)
            print('Dados de Endereço.')
            endereco = input('Digite o nome da rua:\n').capitalize().strip()
            lista_endereco.append(endereco)
            numero = int(input('Digite o número:\n'))
            lista_numero.append(numero)
            opcao_complemento = input('Possui complemento? Digite: S para SIM ou N para NÃO:\n').upper().strip()
            while True:
                if opcao_complemento == 'S' or opcao_complemento == 'N':
                    if opcao_complemento == 'S':
                        complemento = input('Digite o complemento:\n').strip().upper()
                        break
                    else:
                        complemento = ' '
                        break
                else:
                    print('Opção inválida, por favor, tente novamente!')
            lista_complemento.append(complemento)
            bairro = input('Digite o bairro:\n').strip().capitalize()
            lista_bairro.append(bairro)
            cidade = input('Digite a cidade:\n').strip().capitalize()
            lista_cidade.append(cidade)
            uf = input('Digite o UF:\n').strip().upper()
            lista_uf.append(uf)
            print('_' * 50)
            print('Dados da Função.')
            cargo = input('Digite o cargo:\n').strip().capitalize()
            lista_cargo.append(cargo)
            setor = input('Digite o setor:\n').strip().capitalize()
            lista_setor.append(setor)
            salario = float(input('Digite o salário, CENTAVOS SEPARADO POR PONTO:\n'))
            lista_salario.append(salario)
            if setor not in grupo_setor:
                grupo_setor.append(setor)
                total_setor.append(0)
            posicao = grupo_setor.index(setor)
            total_setor[posicao] += salario
            inss = calcular_inss(salario)
            lista_inss.append(inss)
            irrf = calcular_irrf(salario)
            lista_irrf.append(irrf)
            salario_liquido = calcular_salario_liquido(salario)
            lista_salario_liquido.append(salario_liquido)
            if os.path.exists('funcionarios.txt'):
                arquivo = open('funcionarios.txt', 'a')
                arquivo.write('\n')
                arquivo.write('_'*80)
                arquivo.write('\n')
                arquivo.write('Funcionario: ')
                arquivo.write('\n')
                arquivo.write('Matrícula: ')
                arquivo.write(str(matricula))
                arquivo.write(' Nome: ')
                arquivo.write(nome)
                arquivo.write('\n')
                arquivo.write('Dados de Contato: ')
                arquivo.write('\n')
                arquivo.write('E-mail: ')
                arquivo.write(email)
                arquivo.write(' Telefone: ')
                arquivo.write(telefone)
                arquivo.write(' Celular: ')
                arquivo.write(celular)
                arquivo.write('\n')
                arquivo.write('Dados de Endereço: ')
                arquivo.write('\n')
                arquivo.write('Endereço: ')
                arquivo.write(endereco)
                arquivo.write(' Número: ')
                arquivo.write(str(numero))
                arquivo.write(' Complemento: ')
                arquivo.write(complemento)
                arquivo.write(' Bairro: ')
                arquivo.write(bairro)
                arquivo.write(' Cidade: ')
                arquivo.write(cidade)
                arquivo.write(' UF: ')
                arquivo.write(uf)
                arquivo.write('\n')
                arquivo.write('Dados da Função: ')
                arquivo.write('\n')
                arquivo.write('Cargo: ')
                arquivo.write(cargo)
                arquivo.write(' Setor: ')
                arquivo.write(setor)
                arquivo.write(' Salário: R$')
                arquivo.write(str(salario))
                arquivo.write('\n')
                arquivo.write('INSS: R$')
                arquivo.write(str(inss))
                arquivo.write(' IFFR: R$')
                arquivo.write(str(irrf))
                arquivo.write(' Salário Líquido: R$')
                arquivo.write(str(salario_liquido))
            else:
                arquivo = open('funcionarios.txt', 'w')
                arquivo.write('_'*80)
                arquivo.write('\n')
                arquivo.write('LISTA DE FUNCIONARIOS.\n')
                arquivo.write('Funcionario: ')
                arquivo.write('\n')
                arquivo.write('Matrícula: ')
                arquivo.write(str(matricula))
                arquivo.write(' Nome: ')
                arquivo.write(nome)
                arquivo.write('\n')
                arquivo.write('Dados de Contato: ')
                arquivo.write('\n')
                arquivo.write('E-mail: ')
                arquivo.write(email)
                arquivo.write(' Telefone: ')
                arquivo.write(telefone)
                arquivo.write(' Celular: ')
                arquivo.write(celular)
                arquivo.write('\n')
                arquivo.write('Dados de Endereço: ')
                arquivo.write('\n')
                arquivo.write('Endereço: ')
                arquivo.write(endereco)
                arquivo.write(' Número: ')
                arquivo.write(str(numero))
                arquivo.write(' Complemento: ')
                arquivo.write(complemento)
                arquivo.write(' Bairro: ')
                arquivo.write(bairro)
                arquivo.write(' Cidade: ')
                arquivo.write(cidade)
                arquivo.write(' UF: ')
                arquivo.write(uf)
                arquivo.write('\n')
                arquivo.write('Dados da Função: ')
                arquivo.write('\n')
                arquivo.write('Cargo: ')
                arquivo.write(cargo)
                arquivo.write(' Setor: ')
                arquivo.write(setor)
                arquivo.write(' Salário: R$')
                arquivo.write(str(salario))
                arquivo.write('\n')
                arquivo.write('INSS: R$')
                arquivo.write(str(inss))
                arquivo.write(' IFFR: R$')
                arquivo.write(str(irrf))
                arquivo.write(' Salário Líquido: R$')
                arquivo.write(str(salario_liquido))
            arquivo.close()
        elif opcao == 2:
            print('Funcionarios Cadastrados.')
            print('_'*100)
            arquivo = open('funcionarios.txt', 'r')
            funcionarios = arquivo.read()
            arquivo.close()
            print(funcionarios)
        elif opcao == 3:
            for i in range(len(grupo_setor)):
                print(f'Setor: {grupo_setor[i]} - Gasto total: {total_setor[i]}')
        else:
            break
    else:
        print('Opção inválida, por favor, digite novamente!')
