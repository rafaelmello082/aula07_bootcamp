from etl import ler_csv, filtrar_nao_entregues, somar_valores

path_arquivo = 'vendas.csv'

lista_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_nao_entregues(lista_produtos)
valor_entregues = somar_valores(produtos_entregues)
print(valor_entregues)