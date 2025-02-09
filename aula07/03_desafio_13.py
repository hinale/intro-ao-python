import time

# Crie um decorator que calcule o tempo de execução de uma determinada função
def logger(func):
    def wrapper(x, y):
        print(f'Começando a função {func.__name__}')
        func(x, y)
        print(f'Terminando a função {func.__name__}')
    return wrapper


# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas
@logger
def encontrar_item(container, item):
    return item in container

def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)

if __name__ == '__main__':
    main()