# o algoritmo calcula o montante economixado de acordo com o salário e os gastos informados
# 13/09/2022 - Dia do Programador

salario_mensal = input('Digite o valor do seu salario: ')
salario_mensal = float(salario_mensal)

gasto_mensal = input('Digite o valor de seus gastos mensais: ')
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print('O montante economizado ao fim do ano é: ', montante_economizado)