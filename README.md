
# Cotação Manager

Este projeto realiza consultas de cotações de moedas para o real (BRL) utilizando APIs externas. Ele processa essas cotações e gera um relatório em Excel, além de registrar logs detalhados das operações. É possível também gerar o arquivo de moedas a ser utilizado no processo de cotação.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
src/
│
├── input/
│   └── arquivo_moedas.xlsx             # Arquivo contendo a lista de moedas para consulta
│
├── output/
│   └── resultado_cotacoes_<data>.xlsx  # Relatório gerado com os resultados das cotações
│
├── logs/
│   └── log_processo.log                # Arquivo de log com informações detalhadas do processo
│
├── model/
│   └── cotacao_manager.py              # Consulta de cotações de moedas e geração de relatórios
│
├── gerador_arquivo_moedas.py           # Script para gerar o arquivo de moedas a ser usado em input
│
main.py                                 # Arquivo principal que executa o processo de cotação
README.md                               # Instruões sobre o projeto
requirements.txt                        # Arquivo de dependências do projeto
```

## Como Usar

### Gerar o arquivo de moedas

O arquivo de moedas pode ser gerado automaticamente utilizando o script `gerador_arquivo_moedas.py`, que irá criar um arquivo Excel com a lista de moedas a serem consultadas.

1. **Execute o script `gerador_arquivo_moedas.py`**:

   ```bash
   python src/gerador_arquivo_moedas.py
   ```

   Isso irá gerar o arquivo `moedas.xlsx` na pasta `input`, com uma lista de moedas para consulta.

### Consultar as cotações

1. **Carregar as moedas e gerar o relatório**:

   O arquivo `main.py` executa o processo de consulta de cotações utilizando o arquivo gerado anteriormente (`moedas.xlsx`).

   ```bash
   python main.py
   ```

   O script irá:
   - Ler as moedas no arquivo `input/moedas.xlsx`
   - Consultar a cotação para cada moeda utilizando a API
   - Gerar um relatório em Excel em `output/Resultado Cotações <data> <horário>.xlsx`
   - Criar um arquivo de log em `logs/log_processo.log`

### Arquivo de Logs

Os logs detalhados das operações são salvos no diretório `logs/` com o nome `log_processo.log`. O log inclui informações sobre o tempo gasto para consultar cada moeda, o status de cada consulta e quaisquer erros que possam ocorrer durante o processo.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalar as dependências, basta executar:

```bash
pip install -r requirements.txt
```

**P.S.:** Durante o desenvolvimento deste projeto, tentei utilizar a API do Banco Central do Brasil para obter as cotações. No entanto, constatei que a API estava retornando resultados vazios de forma consistente. Diante dessa dificuldade, optei por utilizar a Awesome API ([https://docs.awesomeapi.com.br/api-de-moedas](https://docs.awesomeapi.com.br/api-de-moedas)), que se mostrou uma alternativa gratuita e de fácil utilização para a obtenção dos dados de cotação necessários.
