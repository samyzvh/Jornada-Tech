# Manipulação com strings 2

texto = "     aprender python é muito legal"

print("Texto original: ", texto)
print("-" * 30)

#1. Removendo espaços inúteis
texto_limpo = texto.strip() #
print("Sem espaços extras: ", texto_limpo)

#2. Mudando a caixa (Maiúscula/Minúscula)
print(f"Tudo Maiúsculo: {texto_limpo.upper()}")
print(f"Tudo Minúsculo: {texto_limpo.lower()}")
print(f"Formato de Título: {texto_limpo.title()}")
print(f"Apenas a 1⁰ letra: {texto_limpo.capitalize()}")

#3. substituindo palavras
frase_nova = texto_limpo.replace("legal","PODEROSO")
print("Substituindo: ", frase_nova)

#4. Contando caracteres
tamanho = len(texto_limpo) # Conta a quantidade de caracteres
print(f"O texto tem {tamanho} caracteres.")