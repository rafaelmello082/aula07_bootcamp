import csv

path_arquivo = 'vendas.csv'

def ler_csv(nome_csv: str) -> list[dict]:
  lista = []
  with open(nome_csv, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
      lista.append(linha)
  return lista

def filtrar_nao_entregues(lista: list[dict]) -> list[dict]:
  lista_filtrados = []
  for produto in lista:
    if produto.get('entregue') == 'True':
      lista_filtrados.append(produto)
  return lista_filtrados

def somar_valores(lista_filtrados: list[dict]) -> int:
  valor_total = 0
  for produto in lista_filtrados:
    valor_total += int(produto.get('price'))
  return valor_total


vendas_itens = list[dict]

lista_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_nao_entregues(lista_produtos)
valor_entregues = somar_valores(produtos_entregues)
print(valor_entregues)