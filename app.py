import streamlit as st

st.set_page_config(page_title="Calculadora de Bônus", layout="wide")
st.title("💰 Calculadora de Bônus Trimestral")
st.markdown("Simule abaixo seu bônus trimestral marcando as metas cumpridas em cada mês.")

# Filtro de mês
mes_selecionado = st.radio(
    "📅 Visualizar mês:",
    options=["Trimestre", "Abril", "Maio", "Junho"],
    horizontal=True
)

# Funções disponíveis
funcoes = [
    "GERENTE", "SUPERVISOR", "VISTORIADOR",
    "ATENDENTE", "SERVIÇOS GERAIS", "ANALISTA", "SUPERVISOR ANALISE"
]
funcao_selecionada = st.selectbox("Selecione sua função:", funcoes)

# Metas e pesos por função
dados_funcoes = {
    "GERENTE": [
        ("Produção", 30),
        ("Vistorias de 190,00", 30),
        ("Pesquisa de Satisfação", 5),
        ("Liderança e Organização", 5),
        ("Recursos Humanos", 5),
        ("Lucratividade", 25),
    ],
    "SUPERVISOR": [
        ("Produção", 30),
        ("Vistorias de 190,00", 30),
        ("Pesquisa de Satisfação", 10),
        ("Liderança e Organização", 10),
        ("Recursos Humanos", 20),
    ],
    "VISTORIADOR": [
        ("Produção", 30),
        ("Vistorias de 190,00", 20),
        ("Pesquisa de Satisfação", 20),
        ("Erros de Vistoria", 10),
        ("Atendimento", 5),
        ("Organização da Loja", 5),
        ("Treinamento", 5),
        ("Adesão Pesquisa de Clima", 5),
    ],
    "ATENDENTE": [
        ("Produção", 20),
        ("Vistorias de 190,00", 30),
        ("Pesquisa de Satisfação", 15),
        ("Atendimento", 10),
        ("Organização da Loja", 5),
        ("Treinamento", 10),
        ("Adesão Pesquisa de Clima", 10),
    ],
    "SERVIÇOS GERAIS": [
        ("Organização da Loja", 60),
        ("Pesquisa de Satisfação", 10),
        ("Treinamento", 10),
        ("Atendimento", 10),
        ("Adesão Pesquisa de Clima", 10),
    ],
    "ANALISTA": [
        ("Produção", 20),
        ("Erros em Vistorias", 45),
        ("Apontamentos", 20),
        ("Conform. Processos", 15),
    ],
    "SUPERVISOR ANALISE": [
        ("Treinamentos", 40),
        ("Erros em Vistorias", 40),
        ("Auditoria", 20),
    ]
}

# Valor mensal por função
valor_mensal = {
    "GERENTE": 3000,
    "SUPERVISOR": 800,
    "VISTORIADOR": 400,
    "ATENDENTE": 350,
    "SERVIÇOS GERAIS": 350,
    "ANALISTA": 400,
    "SUPERVISOR ANALISE": 800
}

# Obter metas da função
metas = dados_funcoes[funcao_selecionada]
valor_base = valor_mensal[funcao_selecionada]
cumprimento_total = 0

if mes_selecionado == "Trimestre":
    st.markdown("### ✅ Marque as metas cumpridas em cada mês:")
    mes_cols = st.columns(3)
    meses = ["Abril", "Maio", "Junho"]
    meta_cumprida = {meta: 0 for meta, _ in metas}

    for i, mes in enumerate(meses):
        with mes_cols[i]:
            st.markdown(f"**{mes}**")
            for meta, peso in metas:
                key = f"{funcao_selecionada}_{meta}_{mes}"
                if st.checkbox(meta, key=key):
                    meta_cumprida[meta] += 1

    for meta, peso in metas:
        proporcao = meta_cumprida[meta] / 3  # 0, 0.33, 0.66 ou 1
        cumprimento_total += peso * proporcao

    valor_total = valor_base * 3

else:
    st.markdown(f"### ✅ Marque as metas cumpridas em {mes_selecionado}:")
    meta_colunas = st.columns(2)
    for i, (meta, peso) in enumerate(metas):
        with meta_colunas[i % 2]:
            key = f"{funcao_selecionada}_{meta}_{mes_selecionado}"
            if st.checkbox(f"{meta} ({peso}%)", key=key):
                cumprimento_total += peso

    valor_total = valor_base

# Calcular bônus
valor_recebido = valor_total * (cumprimento_total / 100)
valor_perdido = valor_total - valor_recebido

# Exibir resultado
st.markdown("---")
st.markdown(f"### 🎯 Resultado da Simulação - **{mes_selecionado}**")
st.success(f"💰 Valor possível: R$ {valor_total:,.2f}")
st.info(f"✅ Valor a receber: R$ {valor_recebido:,.2f}")
st.error(f"❌ Valor perdido: R$ {valor_perdido:,.2f}")
st.markdown(f"📊 Cumprimento total: **{cumprimento_total:.1f}%**")