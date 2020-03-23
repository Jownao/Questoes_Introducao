import os

grupo_setor = []
total_setor = []

def cadastro_matricula():
    return input('Digite a matrícula, SOMENTE NÚMEROS:\n')


def cadastro_nome():
    return input('Digite o nome:\n')


def cadastro_email():
    return input('Digite o email:\n')


def cadastro_telefone():
    return input('Digite o telefone, SOMENTE NÚMEROS:\n')


def cadastro_celular():
    return input('Digite o celular, SOMENTE NÚMEROS:\n')


def cadastro_endereco():
    return input('Digite o endereço:\n')


def cadastro_numero():
    return input('Digite o número:\n')


def cadastro_complemento():
    return input('Digite o complemento:\n')


def cadastro_bairro():
    return input('Digite o bairro:\n')


def cadastro_cidade():
    return input('Digite a cidade:\n')


def cadastro_uf():
    return input('Digite o UF:\n')


def cadastro_cargo():
    return input('Digite o cargo:\n')


def cadastro_setor():
    return input('Digite o setor:\n')


def cadastro_salario():
    return input('Digite o salario, SENTAVOS SAPARADO POR PONTO:\n')


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
    return (salario - (calcular_inss(salario) + calcular_irrf(salario)))


def cadatro_geral():
    print('_' * 50)
    print('Dados Pessoais:')
    matricula = cadastro_matricula()
    nome = cadastro_nome()
    print('_' * 50)
    print('Dados para Contato:')
    while True:
        email = cadastro_email()
        if '@' in email:
            break
        else:
            print('E-mail inálido, por favor, digite novamente!')
    while True:
        telefone = cadastro_telefone()
        if len(telefone) >= 8:
            break
        else:
            print('Telefone inválido, por favor, digite novamente!')
    while True:
        opcao_celular = input(
            'Deseja cadastra um celular paar contato, Digite S para SIM ou N para NÃO:\n').upper().strip()
        if opcao_celular == 'S' or opcao_celular == 'N':
            if opcao_celular == 'S':
                while True:
                    celular = cadastro_celular()
                    if len(celular) >= 8:
                        break
                    else:
                        print('Celular inválido, por favor, digite novamente!')
                break
            else:
                celular = 'xxxx-xxxx'
                break
        else:
            print('Opção inválida, por favor, digite novamente!')
    print('_' * 50)
    print('Endereço do Funcionario:')
    endereco = cadastro_endereco()
    numero = cadastro_numero()
    while True:
        opcao_complemento = input('Possui complemento, Digite S para SIM ou N para NÃO:\n').upper().strip()
        if opcao_complemento == 'S' or opcao_complemento == 'N':
            if opcao_complemento == 'S':
                complemento = cadastro_complemento()
                break
            else:
                complemento = ' '
                break
        else:
            print('Opção inválida, por favor, digite novamente!')
    bairro = cadastro_bairro()
    cidade = cadastro_cidade()
    uf = cadastro_uf()
    print('_' * 50)
    print('Dados da Função:')
    cargo = cadastro_cargo()
    setor = cadastro_setor()
    salario = cadastro_salario()
    inss = calcular_inss(int(salario))
    irrf = calcular_irrf(int(salario))
    salario_liquido = calcular_salario_liquido(int(salario))
    if setor not in grupo_setor:
        grupo_setor.append(setor)
        total_setor.append(0)
    posicao = grupo_setor.index(setor)
    total_setor[posicao] += float(salario)
    if os.path.exists('cadastro_funcionarios.txt'):
        arquivo = open('cadastro_funcionarios.txt', 'a')
        arquivo.write('\n')
        arquivo.write('_' * 80)
        arquivo.write('\n')
        arquivo.write('Funcionario: ')
        arquivo.write('\n')
        arquivo.write('Matrícula: ')
        arquivo.write(matricula)
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
        arquivo.write(numero)
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
        arquivo.write(salario)
        arquivo.write('\n')
        arquivo.write('INSS: R$')
        arquivo.write(str(inss))
        arquivo.write(' IFFR: R$')
        arquivo.write(str(irrf))
        arquivo.write(' Salário Líquido: R$')
        arquivo.write(str(salario_liquido))
    else:
        arquivo = open('cadastro_funcionarios.txt', 'a')
        arquivo.write('\n')
        arquivo.write('_' * 80)
        arquivo.write('LISTA DE FUNCIONARIOS.\n')
        arquivo.write('Funcionario: ')
        arquivo.write('\n')
        arquivo.write('Matrícula: ')
        arquivo.write(matricula)
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
        arquivo.write(numero)
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
        arquivo.write(salario)
        arquivo.write('\n')
        arquivo.write('INSS: R$')
        arquivo.write(str(inss))
        arquivo.write(' IFFR: R$')
        arquivo.write(str(irrf))
        arquivo.write(' Salário Líquido: R$')
        arquivo.write(str(salario_liquido))
    arquivo.close()


while True:
    print('_' * 50)
    print('OPÇÕES:\n01 - Cadastro.\n02 - Listar Cadastros.\n03 - Listar Custo por Setor.\n04 - Encerar o Programa.')
    print('_' * 50)
    opcao = int(input('Digite a opção:\n'))
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
        if opcao == 1:
            print('_' * 50)
            print('Cadastro.')
            cadatro_geral()
        elif opcao == 2:
            print('Funcionarios Cadastrados.')
            print('_' * 100)
            arquivo = open('cadastro_funcionarios.txt', 'r')
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
