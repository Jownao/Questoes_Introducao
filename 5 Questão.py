print("Preencha os campos")
h=float(input("Digite sua altura:"))
sexo=(input("Digite seu sexo:"))

if sexo == "masculino":
    IdealHomem=(72.7*h-58)
    print("Seu peso ideal é",IdealHomem)
elif sexo == "feminino":
    IdealMulher=(62.1*h-44.7)
    print("Seu peso ideal é",IdealMulher)

