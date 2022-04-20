# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
cidade = input('Qual cidade você mora?')
estado = input('Qual estado você mora?')

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
print(f'Olá! Você mora na cidadade de {cidade.upper()}.')

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
print('Olá! Você mora no estado do {}.'.format(estado.upper()))