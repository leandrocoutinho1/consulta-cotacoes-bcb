import pandas as pd
import requests
import logging
import time
from datetime import datetime
from openpyxl import Workbook
import os

class CotacaoManager:
    def __init__(self, arquivo_moedas: str):
        self.arquivo_moedas = arquivo_moedas
        self.moedas_saida = []
        self.resultados = []
        self.url_api = 'https://economia.awesomeapi.com.br/json/last/BRL-{moeda}'
        self.moeda_entrada = 'BRL'
        self.taxa_fixa = 1
        self.data_hoje = datetime.now()
        self.data_formatada = self.data_hoje.strftime('%d/%m/%Y')
        self.inicializar_logger()

    def inicializar_logger(self):
        os.makedirs('src/logs', exist_ok=True)  # <-- cria o diretório se não existir

        logging.basicConfig(
            filename='src/logs/log_processo.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def carregar_moedas(self):
        df = pd.read_excel(self.arquivo_moedas)
        self.moedas_saida = df['MoedaSaida'].dropna().str.strip().str.upper().tolist()
        logging.info(f'{len(self.moedas_saida)} moedas carregadas do arquivo.')

    def consultar_cotacao(self, moeda_saida):
        url = self.url_api.format(moeda=moeda_saida)
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            chave = f'BRL{moeda_saida}'
            valor_cotacao = round(float(data[chave]['bid']), 4) if chave in data else ''

        except Exception as e:
            valor_cotacao = ''
            logging.error(f'Erro na consulta da moeda {moeda_saida}: {str(e)}')

        end_time = time.time()
        tempo_gasto = round(end_time - start_time, 2)
        logging.info(f'Moeda: {moeda_saida} | Tempo gasto: {tempo_gasto}s')

        return {
            'moeda_entrada': self.moeda_entrada,
            'taxa': self.taxa_fixa,
            'moeda_saida': moeda_saida,
            'valor_cotacao': valor_cotacao,
            'data': self.data_formatada
        }

    def processar_cotacoes(self):
        for moeda in self.moedas_saida:
            resultado = self.consultar_cotacao(moeda)
            self.resultados.append(resultado)



    def gerar_relatorio_excel(self):
        nome_arquivo = f"src/output/Resultado Cotações {self.data_hoje.strftime('%d_%m - %H_%M')}.xlsx"

        wb = Workbook()
        ws = wb.active
        ws.title = 'Cotações'

        ws.append(['Moeda entrada', 'Taxa', 'Moeda saída', 'Valor cotação', 'Data'])

        for resultado in self.resultados:
            ws.append([
                resultado['moeda_entrada'],
                resultado['taxa'],
                resultado['moeda_saida'],
                resultado['valor_cotacao'],
                resultado['data']
            ])

        os.makedirs('src/output', exist_ok=True)
        wb.save(nome_arquivo)
        logging.info(f'Relatório gerado: {nome_arquivo}') 