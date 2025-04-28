import pandas as pd
import os

os.makedirs('src/input', exist_ok=True)

dados = {
    'MoedaSaida': ['USD', 'EUR', 'JPY', 'COP', 'GBP']
}

df = pd.DataFrame(dados)

caminho_arquivo = 'src/input/moedas.xlsx'
df.to_excel(caminho_arquivo, index=False)

print(f'Arquivo criado em: {caminho_arquivo}')

