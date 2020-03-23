from sistema_modular import cadastro_email, cadastro_telefone, cadastro_celular, calcular_inss, calcular_irrf, calcular_salario_liquido

email = cadastro_email()
telefone = cadastro_telefone()
celular = cadastro_celular()

inss = float(calcular_inss(200))
irrf = float(calcular_irrf(2000))
salario_liquido = float(calcular_salario_liquido(2000))

assert '@' in email, '"@" não encontrado.'
assert len(telefone) >= 8, 'Telefone com menos de 8 digitos!'
assert len(celular) >= 8, 'Celular com menos de 8 digitos!'

assert inss == 180, 'Calculo errado!'
assert irrf == 292.80, 'Calculo errado!'
assert salario_liquido == 1527.20, 'Calculo errado!'
