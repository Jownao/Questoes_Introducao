#não consegui fazer como indentificar quantos emprestimos tem cada matricula,consequentemente não deu pra fazer muita coisa
import os
resposta=0
def linha():
    print('=-='*15)
codigoL=[]
tituloL=[]
qntExemplar=[]
matricula=[]
qntExemplarAluno=[]
codigoLAluno=[]

resposta=int(input(f'========== MENU ==========\n'+
          f'[1] Cadastrar exemplar \n'+
          f'[2] Registrar empréstimo \n'+
          f'[3] Emitir relátorio de empréstimo \n'+
          f'[4] Indicar livro mais solicitado \n'+
          f'[5] Indicar livro menos solicitado \n'+
          f'[6] Indicar livros não solicitados \n'+
          f'[7] Digite senha de finalização \n'))

os.system("cls")
linha()
while resposta != 123:
    if resposta == 1:
        codigoL.append(int(input('Digite código do livro para registrar:\n')))
        tituloL.append(str(input('Digite o título do livro para registrar:\n')))
        qntExemplar.append(int(input('Digite a quantidade de exemples para este livro:\n')))
    if resposta == 2:
        resposta=''
        matricula.append(int(input('Digite seu número de matricula:\n')))
        codigoLAluno.append(int(input('Digite o código do livro para empréstimo:\n')))


    if resposta == 3:
        tamanhoR=len(matricula)
        for i in range(tamanhoR):
            print(f'== MATRICULA === QUANTIDADE DE EXEMPLARES ==\n')
            print(matricula[i],'-----')

    if resposta == 4:
        print('4')
    if resposta == 5:
        print('5')
    if resposta == 6:
        print('6')
    resposta=int(input(f'========== MENU ==========\n'+
              f'[1] Cadastrar exemplar \n'+
              f'[2] Registrar empréstimo \n'+
              f'[3] Emitir relátorio de empréstimo \n'+
              f'[4] Indicar livro mais solicitado \n'+
              f'[5] Indicar livro menos solicitado \n'+
              f'[6] Indicar livros não solicitados \n'+
              f'[7] Digite senha de finalização \n'))
    os.system("cls")
    linha()
