# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod

class Pessoa:
  def __init__(self, nome, telefone, rendaMensal, sexo):
    self.nome = nome
    self.telefone = telefone
    self.rendaMensal = rendaMensal
    self.sexo = sexo

  def chequeEspecial(self):
    self.rendaMensal = self.rendaMensal * 2


class Conta(Pessoa):
  def __init__(self, nome, telefone, rendaMensal, sexo):
      super().__init__(nome, telefone, rendaMensal, sexo)
      self.titular = nome
      self.saldo = rendaMensal

  def sacar(self, valor):
    if valor < self.saldo:
      self.saldo = self.saldo - valor
    print(f"Você sacou R${valor}, seu saldo é de R${self.saldo}.")

  def deposito(self, valor):
    self.saldo = self.saldo + valor
    print(f"Você depositou R${valor}, seu saldo é de R${self.saldo}")

