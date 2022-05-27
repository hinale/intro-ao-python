# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO

from distutils import archive_util


arquivo = 'entrada_desafio_11.txt'

def ler_arquivo(entrada):
    with open(entrada, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        
def escrever_arquivo(entrada):
    with open(entrada, 'a+') as arquivo:
        arquivo.write('\n!saleDurtsnoC od nohtyP ed osruc od sasohlivaram serehlum iO')
        return arquivo

ler_arquivo(arquivo)
escrever_arquivo(arquivo)
ler_arquivo(arquivo)