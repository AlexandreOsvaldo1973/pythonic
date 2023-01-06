import math

varA = float(input("Entre com o valor de a = "))
varB = float(input("Entre com o valor de b = "))
varC = float(input("Entre com o valor de c = "))

Delta = (varB ** 2) - 4*varA*varC
print("\n****************************************************\n")
print(" O valor de Delta é = ", Delta)
print("\n****************************************************\n")

if varA == 0:
	print("O valor de a deve ser diferente de 0")
elif Delta < 0:
	print("Sem raizes reais!")
else:
	x1 = (-varB + Delta ** (1 / 2)) / (2 * varA)
	x2 = (-varB - Delta ** (1 / 2)) / (2 * varA)

	print("x1: {}, x2: {}" .format(x1, x2))
print("\n****************************************************\n")
