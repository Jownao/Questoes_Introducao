nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')
twitter = input('Digite seu twitter: ')
facebook = input('Digite seu facebook: ')
site = input('Digite o seu site: ')
tamanho=len(telefone)
print(tamanho)
while True:
    if '@' not in email:
        print('Email inválido!\n')
        email = input('Digite seu email: \n')
    else:
        break
while True:
    if tamanho !=8:
        print('Seu número de telefone é inválido\n')
        telefone = input('Digite seu telefone: \n')
        tamanho = len(telefone)
    else:
        break
while True:
    if 'www' not in site:
        print('Site inválido!\n')
        site = input('Digite o seu site: \n')
    else:
        break

agenda = open('agenda.txt', 'w')
agenda.write(nome)
agenda.write('\n')
agenda.write(email)
agenda.write('\n')
agenda.write(telefone)
agenda.write('\n')
agenda.write(twitter)
agenda.write('\n')
agenda.write(facebook)
agenda.write('\n')
agenda.write(site)
agenda.write('\n')
agenda.close()

agenda = open('agenda.txt', 'r')
texto = agenda.read()
print(texto)
agenda.close()
