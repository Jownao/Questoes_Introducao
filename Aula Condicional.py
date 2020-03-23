print("Digite as notas e os pesos:")

nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
peso1 = int(input())
peso2 = int(input())
media = (nota1*peso1+nota2*peso2)/(peso1+peso2)

if media >= 6:
    print ("Aprovado")

elif media >= 4:
    print("Recuperação")

else:
    print("Reprovado")

print ("A média foi", media)
