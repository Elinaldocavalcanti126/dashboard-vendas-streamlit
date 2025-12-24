📊 Dashboard de Vendas – Streamlit

Dashboard interativo desenvolvido em Python com Streamlit para análise e visualização de dados fictícios de vendas, simulando o cenário comercial de uma empresa.

O projeto tem como objetivo demonstrar habilidades em análise de dados, visualização, organização de código e criação de dashboards interativos.

🚀 Funcionalidades

📌 KPIs Principais

Receita total

Total de clientes únicos

Ticket médio

📈 Evolução Temporal

Análise da evolução das vendas ao longo do tempo

📊 Análise Mensal

Gráfico de barras interativo com vendas por mês

🥧 Participação por Produto

Gráfico de pizza com distribuição da receita por produto

📋 Tabela Detalhada

Visualização completa dos dados brutos utilizados no dashboard

🧱 Estrutura do Projeto
VENDAS_DASHBOARD/
├── app.py                  # Arquivo principal da aplicação Streamlit
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação
├── data/
│   └── vendas.csv          # Base de dados fictícia
└── src/
    ├── __init__.py
    ├── config.py           # Configurações gerais
    ├── data_loader.py      # Carregamento e tratamento dos dados
    ├── plots.py            # Criação dos gráficos
    └── utils.py            # Funções auxiliares

🛠️ Tecnologias Utilizadas

Python 3.8+

Streamlit

Pandas

NumPy

Matplotlib

Plotly

⚙️ Instalação
Pré-requisitos

Python 3.8 ou superior

pip

Passo a passo

Clone o repositório ou baixe os arquivos do projeto

(Opcional, recomendado) Crie e ative um ambiente virtual:

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt

▶️ Como Executar

Na raiz do projeto, execute:

streamlit run app.py


O dashboard será aberto automaticamente no navegador em:

http://localhost:8501

📊 Estrutura dos Dados

O arquivo vendas.csv deve conter as seguintes colunas:

Coluna	Descrição
Data	Data da venda (YYYY-MM-DD)
Cliente	Identificador do cliente
Produto	Nome do produto
Quantidade	Quantidade vendida
Preco_Unitario	Preço unitário do produto
Exemplo de dados:
Data,Cliente,Produto,Quantidade,Preco_Unitario
2024-01-05,Cliente_A,Produto_X,10,50.00
2024-01-12,Cliente_B,Produto_Y,5,120.00

🎨 Personalização

Para utilizar seus próprios dados:

Substitua o arquivo data/vendas.csv

Mantenha o mesmo formato de colunas

Recarregue a aplicação

📈 KPIs Calculados

Receita Total

Clientes Únicos

Ticket Médio

Vendas Mensais

Receita por Produto

🤝 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para fazer um fork, criar melhorias e enviar um pull request.

📝 Licença

Projeto de caráter educacional e demonstrativo.
Os dados utilizados são totalmente fictícios.

👨‍💻 Autor

Elinaldo Cavalcanti
💼 Desenvolvedor Python | Dados | Automação
🔗 LinkedIn: https://www.linkedin.com/in/elinaldocavalcanti-dev

Nota: Este dashboard utiliza dados fictícios apenas para fins de demonstração. Nenhuma informação representa dados reais de empresas ou clientes.