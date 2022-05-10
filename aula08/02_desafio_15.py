# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
  def __init__(self):
    self.ligado = False
    self.cor = "vermelho"
    self.modelo = "corsa"
    self.velocidade = 10
    self.velocidade_min = 0
    self.velocidade_max = 140

  def ligar(self):
    self.ligado = True

  def deslidado(self):
    self.ligado = False

  def acelerar(self):
    if not self.ligado:
      return

    if self.velocidade < self.velocidade_max:
      self.velocidade += 1

  def desacelerar(self):
    if not self.ligado:
      return

    if self.velocidade > self.velocidade_min:
      self.velocidade -= 1

  def __str__(self) -> str:
      return f"Carro da cor: {self.cor}; modelo: {self.modelo}; com velocidade de: {self.velocidade} Km/h."


# Crie uma instância da classe carro.
carro_corsa = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro_corsa.ligar()
print(f"O carro ligou, velocidade {carro_corsa.velocidade} Km/h.")

for _ in range(5):
  carro_corsa.acelerar()
print(f"Carro corsa está a uma velocidade de {carro_corsa.velocidade} Km/h")

# Faça o carro "parar" utilizando os métodos da sua classe.
if carro_corsa.velocidade > carro_corsa.velocidade_min:
  for _ in range(carro_corsa.velocidade):
    carro_corsa.desacelerar()
  carro_corsa.deslidado()

print(f"Carro corsa parou, velocidade: {carro_corsa.velocidade} Km/h. Ele está ligado? {carro_corsa.ligado}")