l1=float(input("Digite o lado A:"))
l2=float(input("Digite o lado B:"))
l3=float(input("Digite o lado C:"))

if l1<l2+l3 and l2<l1+l3 and l3<l2+l1:
    if l1==l2 or l1==l3 and l2==l1 or l2==l3:
        print("Triângulo isósceles")


else:
    print("Não é um triângulo")