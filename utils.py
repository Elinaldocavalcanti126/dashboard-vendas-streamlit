import streamlit as st

def formatar_moeda(valor):
    """
    Formata valor numérico para formato de moeda brasileira.
    
    Args:
        valor (float): Valor a ser formatado.
    
    Returns:
        str: Valor formatado como moeda.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def aplicar_estilo_customizado():
    """
    Aplica CSS customizado para melhorar a aparência do dashboard.
    """
    st.markdown("""
        <style>
        /* Fonte principal */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        
        /* Header customizado */
        .main > div {
            padding-top: 2rem;
        }
        
        /* Métricas */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 600;
            color: #1f77b4;
        }
        
        [data-testid="stMetricDelta"] {
            font-size: 1rem;
        }
        
        /* Títulos */
        h1 {
            color: #1e293b;
            font-weight: 700;
            padding-bottom: 0.5rem;
        }
        
        h2, h3 {
            color: #334155;
            font-weight: 600;
            margin-top: 2rem;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #f8fafc;
        }
        
        [data-testid="stSidebar"] h1 {
            color: #1e293b;
            font-size: 1.5rem;
        }
        
        /* Botões */
        .stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.5rem 2rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #1557a0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Expander */
        [data-testid="stExpander"] {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            background-color: #ffffff;
        }
        
        /* DataFrame */
        [data-testid="stDataFrame"] {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
        }
        
        /* Cards de métricas */
        [data-testid="stMetric"] {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }
        
        /* Divisores */
        hr {
            margin: 2rem 0;
            border: none;
            border-top: 2px solid #e2e8f0;
        }
        
        /* Info boxes */
        .stAlert {
            border-radius: 8px;
            border-left: 4px solid #1f77b4;
        }
        
        /* Remover padding extra */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Tooltips */
        [data-testid="stTooltipHoverTarget"] {
            color: #64748b;
        }
        
        /* Select boxes e inputs */
        [data-testid="stSelectbox"], [data-testid="stDateInput"] {
            border-radius: 8px;
        }
        
        /* Melhorias de espaçamento */
        .element-container {
            margin-bottom: 1rem;
        }
        
        /* Tabelas */
        .dataframe {
            font-size: 0.9rem;
        }
        
        .dataframe thead th {
            background-color: #f1f5f9;
            color: #1e293b;
            font-weight: 600;
        }
        
        .dataframe tbody tr:hover {
            background-color: #f8fafc;
        }
        </style>
    """, unsafe_allow_html=True)


def exibir_insight(titulo, conteudo, tipo="info"):
    """
    Exibe um card de insight destacado.
    
    Args:
        titulo (str): Título do insight.
        conteudo (str): Conteúdo do insight.
        tipo (str): Tipo do insight ('info', 'success', 'warning', 'error').
    """
    cores = {
        "info": "#3b82f6",
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444"
    }
    
    cor = cores.get(tipo, cores["info"])
    
    st.markdown(f"""
        <div style="
            padding: 1.5rem;
            background-color: white;
            border-left: 4px solid {cor};
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 1rem 0;
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: {cor};">{titulo}</h4>
            <p style="margin: 0; color: #334155;">{conteudo}</p>
        </div>
    """, unsafe_allow_html=True)


def calcular_crescimento(valor_atual, valor_anterior):
    """
    Calcula percentual de crescimento entre dois valores.
    
    Args:
        valor_atual (float): Valor atual.
        valor_anterior (float): Valor anterior.
    
    Returns:
        float: Percentual de crescimento.
    """
    if valor_anterior == 0:
        return 0
    return ((valor_atual - valor_anterior) / valor_anterior) * 100


def gerar_insights_automaticos(df):
    """
    Gera insights automáticos baseados nos dados.
    
    Args:
        df (pd.DataFrame): DataFrame de vendas.
    
    Returns:
        list: Lista de insights.
    """
    insights = []
    
    # Produto mais vendido
    produto_top = df.groupby("Produto")["Receita"].sum().idxmax()
    receita_top = df.groupby("Produto")["Receita"].sum().max()
    insights.append(f"🏆 {produto_top} é o produto mais lucrativo com R$ {receita_top:,.2f} em receita")
    
    # Cliente VIP
    cliente_top = df.groupby("Cliente")["Receita"].sum().idxmax()
    receita_cliente_top = df.groupby("Cliente")["Receita"].sum().max()
    insights.append(f"👑 {cliente_top} é o cliente mais valioso com R$ {receita_cliente_top:,.2f} em compras")
    
    # Ticket médio
    ticket_medio = df.groupby("Cliente")["Receita"].sum().mean()
    insights.append(f"💰 Ticket médio por cliente: R$ {ticket_medio:,.2f}")
    
    return insights