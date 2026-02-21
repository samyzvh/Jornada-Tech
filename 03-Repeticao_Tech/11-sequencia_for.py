# Sequência númerica (Loop: Uso do FOR x IN RANGE())

x = int(input("Digite um número: "))

print(f"A sequência do número {x} é: ")
for y in range(0 ,x + 1, 1):
  # O "Fim" no range, sempre tem que ser um a mais de onde você que ele termine.
  # Exemplo: Você quer que ele de 10 voltas, se você colocar o número 10 no "fim" ele apenas vai dar 9 voltas, poque o limite é 10. Então sempre coloque um a mais.
  print(y)