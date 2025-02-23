# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.
import colorama

alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]


# Comece o programa perguntando o nome da aluna.
nome = input("Qual seu nome?")

# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.
def encontrar_nome():
  i = 0
  for aluna in alunas:
    if nome == aluna:
      break
    elif nome != aluna:
      i += 1
  return i 

def encontrar_nota():
  i = encontrar_nome()
  if i < 10:
    nota = notas[i]
    return nota
  else:
    return "Erro"

def imprimir_nota():
  nota = encontrar_nota()
  if nota == "Erro":
    print(colorama.Fore.RED + f"Aviso: nome não escontrado!")
  elif nota < 60:
    print(f"Aluna {nome} tirou nota " + colorama.Fore.RED + str(nota))
  elif nota > 90:
    print(f"Aluna {nome} tirou nota " + colorama.Fore.GREEN + str(nota))
  else:
    print(f"Aluna {nome} tirou nota {nota}.")

imprimir_nota()