# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
contador = 0
lista = []
while(contador<60):
  numero = contador + 1
  lista.append(numero)
  contador += 1
print(lista)
print()

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
for par in range(2, 61, 2):
  print(par, end=' ')
print()