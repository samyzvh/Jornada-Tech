# Loja do Match (uso do match)

print("-----LOJA DE ROUPAS----")
print("1. Casaco")
print("2. Blusa")
print("3. Saia")
print("4. Calça")

opcao = input("Digite o número do seu departamento: ")

match opcao:
  case "1":
    print("Você escolheu CASACO")
  case "2":
    print("Você escolheu BLUSA")
  case "3":
    print("Você escolheu SAIA")
  case "4":
    print("Você escolheu CALÇA")
  case _:
    print("Opção inválida.")