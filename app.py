import streamlit as st
import pandas as pd

from data_loader import load_data, resumo_kpis, get_top_produtos, get_top_clientes
from plots import (
    plot_vendas_clientes, 
    plot_vendas_barras, 
    plot_participacao_produto,
    plot_evolucao_ticket_medio,
    plot_heatmap_vendas,
    plot_comparacao_produtos
)
from utils import formatar_moeda, aplicar_estilo_customizado


def run_dashboard():
    # Configuração da página
    st.set_page_config(
        page_title="Dashboard de Vendas | Analytics",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Aplicar estilo customizado
    aplicar_estilo_customizado()
    
    # Sidebar - Filtros
    st.sidebar.title("🎯 Filtros")
    st.sidebar.markdown("---")
    
    # Carregar dados
    df = load_data("data/vendas.csv")
    
    # Filtro de período
    min_date = df["Data"].min().date()
    max_date = df["Data"].max().date()
    
    date_range = st.sidebar.date_input(
        "Período",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filtro de produto
    produtos = ["Todos"] + sorted(df["Produto"].unique().tolist())
    produto_selecionado = st.sidebar.selectbox("Produto", produtos)
    
    # Filtro de cliente
    clientes = ["Todos"] + sorted(df["Cliente"].unique().tolist())
    cliente_selecionado = st.sidebar.selectbox("Cliente", clientes)
    
    # Aplicar filtros
    df_filtrado = df.copy()
    
    if len(date_range) == 2:
        df_filtrado = df_filtrado[
            (df_filtrado["Data"].dt.date >= date_range[0]) & 
            (df_filtrado["Data"].dt.date <= date_range[1])
        ]
    
    if produto_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Produto"] == produto_selecionado]
    
    if cliente_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Cliente"] == cliente_selecionado]
    
    # Informações da sidebar
    st.sidebar.markdown("---")
    st.sidebar.info(f"📅 **Período:** {len(df_filtrado)} registros")
    st.sidebar.success(f"🎯 **Filtros ativos:** {sum([produto_selecionado != 'Todos', cliente_selecionado != 'Todos'])}")
    
    # Header
    st.title("📊 Dashboard de Vendas & Analytics")
    st.markdown("**Sistema de análise de desempenho comercial e inteligência de negócios**")
    st.markdown("---")
    
    # Verificar se há dados após filtros
    if len(df_filtrado) == 0:
        st.warning("⚠️ Nenhum dado encontrado com os filtros aplicados. Por favor, ajuste os filtros.")
        return
    
    # KPIs Principais
    kpis = resumo_kpis(df_filtrado)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💰 Receita Total", 
            formatar_moeda(kpis['Receita_Total']),
            delta=f"+{kpis['Crescimento_Receita']:.1f}%" if kpis.get('Crescimento_Receita', 0) != 0 else None
        )
    
    with col2:
        st.metric(
            "👥 Clientes Únicos", 
            f"{kpis['Clientes_Totais']:,}",
            delta=f"+{kpis['Novos_Clientes']}" if kpis.get('Novos_Clientes', 0) > 0 else None
        )
    
    with col3:
        st.metric(
            "🎯 Ticket Médio", 
            formatar_moeda(kpis['Ticket_Medio_Geral']),
            delta=f"{kpis['Variacao_Ticket']:.1f}%" if kpis.get('Variacao_Ticket', 0) != 0 else None
        )
    
    with col4:
        st.metric(
            "📦 Total de Vendas", 
            f"{kpis['Total_Transacoes']:,}",
            delta=f"+{kpis['Crescimento_Vendas']:.1f}%" if kpis.get('Crescimento_Vendas', 0) != 0 else None
        )
    
    st.markdown("---")
    
    # Seções de análise e gráficos...
    # (mantém igual ao que você já escreveu)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px;'>
            <p>Dashboard desenvolvido com ❤️ por Elinaldo
          usando Streamlit | Dados atualizados em tempo real</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    run_dashboard()
