n1=float(input("Digite sua primeira nota:"))
n2=float(input("Digite sua segunda nota:"))
aulas=int(input("Digite quantidade de aulas:"))
p=int(input("Digite quantas aulas você assistiu:"))

nota=(n1+n2)/2

freq=p/aulas


if nota>=6 and freq >=0.75:
    print("Aprovado ,parabéns sua nota foi:", nota)

else:
    print("Reprovado")