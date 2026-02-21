# Simulador de empréstimo (Aqui o estudo era sobre o uso de condicionais e como elas funcionam)

print("Verifique aqui se você está apto para solicitar o seu empréstimo.\n---------------------------------------\nApenas com sua idade e o valor do seu salário.")
print() # Para deixar um espaço em branco no terminal.
idade = int(input("Qual a sua idade? "))
salario = float(input("Qual o valor do seu salário? "))

if idade >= 18 and salario >= 2500:
  print("Empréstimo aprovado!!!")
elif salario < 2500:
  print("Você não recebe suficente\npara se comprometer com um empréstimo.")
else:
  print("Empréstimo negado!!")
