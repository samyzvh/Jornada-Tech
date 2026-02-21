# Saudação personalizada (uso do .upper)

nome = input("Digite o seu nome: ").upper()
match nome:
  case "SAMY":
     print(f"Olá, {nome}. Tenha um bom dia!")
  case _:
    print(f"Olá, {nome}. Tenha um mal dia!")
