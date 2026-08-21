valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))

valorDelta = (valorB ** 2) - (4 * valorA * valorC) # **2 elevado ao quadrado
print("O valor de Delta e: ", valorDelta)

valorx1 = (-valorB + (valorDelta **0.5)) /(2 * valorA) # **0.5 raiz quadrada
valorx2 = (-valorB - (valorDelta **0.5))/(2 * valorA)
print("Os valores das raizes sao: ", valorx1, "e", valorx2)