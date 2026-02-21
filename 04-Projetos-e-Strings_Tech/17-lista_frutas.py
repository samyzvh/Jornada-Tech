# Utilizando Listas (Entendendo como funcionam as listas)

frutas = ["Maçã", "Banana", "Uva", "Tamarindo"] # Uma lista sempre é feita com colchetes
print(f"Primeira fruta da lista: {frutas[0]}") # Posição de cada intem na lista [0, 1, 2, 3]
print(f"Ultima fruta da lista: {frutas[3]}")
print()

print("Comprei Laranja")
frutas.append("Laranja") # ".append " é um comando para adicionar algo em uma lista
print(frutas)
print()

print("Comi a Laranja")
frutas.remove("Laranja") # ".remove " é um comando para remover qualquer item da lista
print(frutas)
print()

print("Comprei Abacate e Melancia")
frutas.append("Abacate")
frutas.append("Melancia")
print(frutas)

print() # Print vazio é para pular uma linha

for item in frutas: # Traduzindo: Para cada item na lista de frutas faça isso (não precisa determinar o fim, porque o fim é o último item da lista frutas)
# O "item" a cada volta ele recebe o valor de cada item da lista "frutas"
  print(f"Preciso comprar: {item}")
  # Exemplo: quando item for "0" ele vai printar "0" da lista frutas e quando item for "1" vai printar o item "1" e assim por diante