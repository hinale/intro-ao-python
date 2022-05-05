from datetime import datetime, date, time, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario = input('Digite a data do seu próximo aniversário:(dd/mm/aaaa)')
aniversario_datetime = datetime.strptime(aniversario, '%d/%m/%Y')
print(f'Seu aniversário é dia {str(aniversario_datetime)}')

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
hoje = datetime.now()
print(f"Hoje é: {hoje}")
contagem = aniversario_datetime - hoje
print(f"Faltam {contagem.days} dias para seu aniversário!")

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
resposta_aniversario = input("Você gosta do seu aniversário?(s/n)")

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
resposta_festa = input("Você vai fazer uma festa no seu aniversário?(s/n)")

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if resposta_aniversario == "s" and resposta_festa == "s":
  print("Você ganhará um Presente!!!")
else:
  print("Você não vai ganhar um presente.")

