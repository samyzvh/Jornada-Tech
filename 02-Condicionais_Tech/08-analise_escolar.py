# Análise de notas e frequência de uma escola de uma escola. (Quebrei bastante a cabeça nesse código por ser o meu primeiro um pouco complexo)

p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
p3 = float(input("Digite a terceira nota: "))
FR = float(input("Qual foi a sua frequência escolar? "))
M = 0
M = (p1 + p2 + p3)/3

if FR >= 75 and M >= 6:
  print(f"APROVADO!! Sua média é de: {M:.1f} e sua frenquência de: {FR}%") # O uso das {}(chaves) é para separar variáveis e tbm posso usar a opção de definir qunatas casas decimais eu quero.
elif FR >= 75 and M >= 5 and M < 6:
  print(f"RECUPERAÇÃO!! Sua média é de: {M:.1f} e sua frenquência de: {FR}%")
  RC = float(input(f"Digite a nota de recuperação: "))
  if RC >= 6:
# Explicação do uso de outro if: para chegar nesse terceiro elif, o segundo (onde você pergunta o valor de RC) teria que ter sido Falso.
# Se o segundo foi falso, a variável RC nunca nasceu.
    print(f"APROVADO!! Sua nota foi de: {RC:.1f} e sua frenquência de: {FR}%")
  else:
    print(f"Reprovado no exame!! Sua média é de: {M:.1f} e sua frenquência de: {FR}%")
else:
  print(f"REPROVADOO!!! Sua média é de: {M:.1f} e frenquência de: {FR}%")
