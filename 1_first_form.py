import pandas as pd

# Forma de ler poucos arquivos CSV dentro de um zip.
tabela = pd.read_csv('zip-file.zio', compression="zip")

print(tabela)
