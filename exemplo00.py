def soma(valor_1: float, valor_2: float = 10) -> float:
  resultado = valor_1 + valor_2
  return resultado

valor_1 = soma(3,5)
valor_2 = soma(4,9)
valor_3 = soma(15)
valor_4 = soma(0)

print(valor_1)
print(valor_2)
print(valor_3)
print(valor_4)