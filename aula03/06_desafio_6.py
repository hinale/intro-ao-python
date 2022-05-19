# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.
from operator import indexOf


alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]


# Comece o programa perguntando o nome da aluna.
nome = input("Qual seu nome?")


# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
def procurar_nota(nome):
  for aluna in alunas:
    if aluna == nome:
      i = alunas[i]
  print(f"Aluna número: {i}")

  for nota in notas:
    if indexOf(notas) == i:
      nota_aluna = notas[i]
  print(f"Nota da aluna {nome}: {nota_aluna}.")


# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.
procurar_nota(nome)

