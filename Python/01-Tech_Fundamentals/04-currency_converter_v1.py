# Conversor de moedas 
DL = float(5.22)
RL = float(input("Digite o valor em real: ")) # O float serve para dizer que o valor dessa váriavel é da classe real (flutuar).
# Float fora do parênteses significa que qualquer coisa que for colocada nesse input será um valor considerado real.
dolares = float
dolares = RL / DL # Não precisava criar outra variável chamada "dolares", apenas atribuir o DL como RL * 5.22

print(f"R${RL:.2f} reais é exatamente U${dolares:.2f} doláres.")
# "f"{variavel:.2f}"" quer dizer: para só considerar duas casas decimais depois do número inteiro
# Exemplo: 1.23