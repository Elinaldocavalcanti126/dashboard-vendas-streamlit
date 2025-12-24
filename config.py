"""
Configurações globais do dashboard.
"""

# Configurações de visualização
PLOT_CONFIG = {
    'height': 400,
    'template': 'plotly_white',
    'colorway': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
}

# Paleta de cores
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff9800',
    'info': '#17a2b8',
    'purple': '#9467bd',
    'pink': '#e377c2',
    'gray': '#7f7f7f'
}

# Configurações de formato
FORMATO_MOEDA = "R$ {:,.2f}"
FORMATO_NUMERO = "{:,.0f}"
FORMATO_PERCENTUAL = "{:.2f}%"

# Configurações de dados
CAMINHO_DADOS = "data/vendas.csv"

# Textos do dashboard
TEXTOS = {
    'titulo': '📊 Dashboard de Vendas & Analytics',
    'subtitulo': 'Sistema de análise de desempenho comercial e inteligência de negócios',
    'sem_dados': '⚠️ Nenhum dado encontrado com os filtros aplicados. Por favor, ajuste os filtros.',
    'carregando': '⏳ Carregando dados...',
    'erro_carregamento': '❌ Erro ao carregar dados. Verifique o arquivo CSV.',
}

# Configurações de métricas
METRICAS_LABELS = {
    'receita': '💰 Receita Total',
    'clientes': '👥 Clientes Únicos',
    'ticket': '🎯 Ticket Médio',
    'vendas': '📦 Total de Vendas'
}

# Ordem dos dias da semana
DIAS_SEMANA = {
    'Monday': 'Segunda',
    'Tuesday': 'Terça',
    'Wednesday': 'Quarta',
    'Thursday': 'Quinta',
    'Friday': 'Sexta',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

# Configurações de exportação
EXPORT_CONFIG = {
    'csv_encoding': 'utf-8',
    'csv_separator': ',',
    'excel_engine': 'openpyxl'
}