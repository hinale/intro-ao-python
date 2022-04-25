from datetime import datetime, date, time, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario = input('Digite sua data de aniversário(dd/mm/aaaa)')
aniversario_datetime = datetime.strptime(aniversario, '%d/%m/%Y')
print(f'Seu aniversário é dia {str(aniversario_datetime)}')

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
hoje = datetime.now().date()
print('Hoje é: ' + hoje.strftime('%d/%m/%y'))

contagem = hoje.strftime('%d/%m/%y') - aniversario_datetime
print('Faltam ' + contagem.strftime('%d') + ' dias para o seu aniversário.')
# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.

