# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.
import csv
import json

with open('exemplo2.csv', mode='r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    alunos = []
    for registro in leitor_csv:
        alunos.append(registro)

alunos_json = json.dumps(alunos)

print(alunos_json)
