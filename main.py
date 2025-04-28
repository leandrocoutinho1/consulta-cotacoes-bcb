from src.model.cotacao_manager import CotacaoManager

def main():
    caminho_arquivo_moedas = 'src/input/moedas.xlsx'
    cotacao_manager = CotacaoManager(arquivo_moedas=caminho_arquivo_moedas)
    
    cotacao_manager.carregar_moedas()
    cotacao_manager.processar_cotacoes()
    cotacao_manager.gerar_relatorio_excel()

if __name__ == "__main__":
    main()
