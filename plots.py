import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from data_loader import agregar_dados_mensais, calcular_metricas_produto  # <-- ajuste aqui

# Paleta de cores profissional
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

def plot_vendas_clientes(df):
    df_mensal = agregar_dados_mensais(df)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(
        x=df_mensal["Mes"], y=df_mensal["Vendas"],
        name="Receita", mode='lines+markers',
        line=dict(color=COLORS['primary'], width=3),
        marker=dict(size=8),
        hovertemplate='<b>%{x}</b><br>Receita: R$ %{y:,.2f}<extra></extra>'
    ), secondary_y=False)
    fig.add_trace(go.Scatter(
        x=df_mensal["Mes"], y=df_mensal["Clientes"],
        name="Clientes Únicos", mode='lines+markers',
        line=dict(color=COLORS['secondary'], width=3, dash='dash'),
        marker=dict(size=8, symbol='square'),
        hovertemplate='<b>%{x}</b><br>Clientes: %{y}<extra></extra>'
    ), secondary_y=True)
    fig.update_xaxes(title_text="Período", tickangle=-45)
    fig.update_yaxes(title_text="<b>Receita (R$)</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Clientes Únicos</b>", secondary_y=True)
    fig.update_layout(
        title="Evolução de Receita e Base de Clientes",
        hovermode='x unified', template='plotly_white',
        height=400, showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_vendas_barras(df):
    vendas_produto = df.groupby("Produto")["Receita"].sum().reset_index()
    vendas_produto = vendas_produto.sort_values("Receita", ascending=True)
    fig = px.bar(
        vendas_produto, y="Produto", x="Receita",
        orientation='h', title="Receita por Produto",
        labels={"Receita": "Receita (R$)", "Produto": "Produto"},
        text="Receita", color="Receita", color_continuous_scale="Blues"
    )
    fig.update_traces(
        texttemplate='R$ %{text:,.0f}', textposition="outside",
        hovertemplate='<b>%{y}</b><br>Receita: R$ %{x:,.2f}<extra></extra>'
    )
    fig.update_layout(showlegend=False, template='plotly_white', height=400)
    return fig

def plot_participacao_produto(df):
    receita_por_produto = df.groupby("Produto")["Receita"].sum().reset_index()
    fig = px.pie(
        receita_por_produto, values="Receita", names="Produto",
        title="Share de Receita por Produto", hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(
        textposition='inside', textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Receita: R$ %{value:,.2f}<br>Participação: %{percent}<extra></extra>'
    )
    fig.update_layout(template='plotly_white', height=400, showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.05))
    return fig

def plot_evolucao_ticket_medio(df):
    df_mensal = agregar_dados_mensais(df)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_mensal["Mes"], y=df_mensal["Ticket_Medio"],
        mode='lines+markers', name='Ticket Médio', fill='tozeroy',
        line=dict(color=COLORS['success'], width=2), marker=dict(size=8),
        hovertemplate='<b>%{x}</b><br>Ticket Médio: R$ %{y:,.2f}<extra></extra>'
    ))
    fig.update_layout(
        title="Evolução do Ticket Médio", xaxis_title="Período",
        yaxis_title="Ticket Médio (R$)", template='plotly_white',
        height=400, hovermode='x unified'
    )
    fig.update_xaxes(tickangle=-45)
    return fig

def plot_heatmap_vendas(df):
    df['Dia_Semana_Nome'] = df['Data'].dt.day_name()
    df['Mes_Nome'] = df['Data'].dt.strftime('%b/%y')
    heatmap_data = df.groupby(['Dia_Semana_Nome', 'Mes_Nome'])['Receita'].sum().reset_index()
    heatmap_pivot = heatmap_data.pivot(index='Dia_Semana_Nome', columns='Mes_Nome', values='Receita')
    dias_ordem = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dias_pt = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
    heatmap_pivot = heatmap_pivot.reindex([d for d in dias_ordem if d in heatmap_pivot.index])
    heatmap_pivot.index = [dias_pt[dias_ordem.index(d)] for d in heatmap_pivot.index]
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_pivot.values, x=heatmap_pivot.columns, y=heatmap_pivot.index,
        colorscale='YlOrRd',
        hovertemplate='<b>%{y}</b><br>%{x}<br>Receita: R$ %{z:,.2f}<extra></extra>',
        colorbar=dict(title="Receita (R$)")
    ))
    fig.update_layout(
        title="Padrão de Vendas: Dia da Semana vs Período",
        xaxis_title="Mês", yaxis_title="Dia da Semana",
        template='plotly_white', height=400
    )
    return fig

def plot_comparacao_produtos(df):
    metricas = calcular_metricas_produto(df)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Receita Total', x=metricas['Produto'], y=metricas['Receita_Total'],
        marker_color=COLORS['primary'],
        hovertemplate='<b>%{x}</b><br>Receita: R$ %{y:,.2f}<extra></extra>'
    ))
    fig.add_trace(go.Bar(
        name='Quantidade Vendida', x=metricas['Produto'], y=metricas['Quantidade_Total'],
        marker_color=COLORS['secondary'], yaxis='y2',
        hovertemplate='<b>%{x}</b><br>Quantidade: %{y}<extra></extra>'
    ))
    fig.update_layout(
        title="Comparação de Performance por Produto",
        xaxis_title="Produto", yaxis_title="Receita (R$)",
        yaxis2=dict(title="Quantidade Vendida", overlaying='y', side='right'),
        barmode='group', template='plotly_white', height=400,
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

