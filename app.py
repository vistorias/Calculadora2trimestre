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
    "GERENTE", "SUPERVISOR", "VISTORIADOR", "ATENDENTE",
    "SERVIÇOS GERAIS", "ANALISTA", "SUPERVISOR ANALISE"
]
funcao_selecionada = st.selectbox("Selecione sua função:", funcoes)

# Filtro de empresa
empresas = ["LOG", "StarCheck", "Tokyo", "Velox"]
empresa_selecionada = None
if funcao_selecionada in ["GERENTE", "SUPERVISOR"]:
    empresa_selecionada = st.selectbox("Selecione a empresa:", empresas)

# Dados das metas e pesos
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

valor_mensal = {
    "GERENTE": 3000,
    "SUPERVISOR": 800,
    "VISTORIADOR": 400,
    "ATENDENTE": 350,
    "SERVIÇOS GERAIS": 350,
    "ANALISTA": 400,
    "SUPERVISOR ANALISE": 800
}

pesos_producao_por_empresa = {
    "LOG": {
        "Açailândia": 15,
        "Carolina": 2,
        "Presidente Dutra": 12,
        "São Luís": 58,
        "Timon": 13
    },
    "StarCheck": {
        "Bacabal": 20,
        "Balsas": 20,
        "Caxias": 7,
        "Codó": 5,
        "Pinheiro": 11,
        "São Luís": 39
    },
    "Tokyo": {
        "Barra do Corda": 11,
        "Chapadinha": 9,
        "Santa Inês": 38,
        "São José dos Patos": 7,
        "São José de Ribamar": 34
    },
    "Velox": {
        "Estreito": 7,
        "Grajaú": 7,
        "Imperatriz": 50,
        "Pedreiras": 9,
        "São Luís": 27
    }
}

cidades_por_supervisor = {
    "MARTA OLIVEIRA COSTA RAMOS": ["São Luís"],
    "ELEILSON DE SOUSA ADELINO": ["Açailândia", "Carolina", "Presidente Dutra", "Timon"],

    "SAMMYRA JISELE BRITO REIS": ["Bacabal", "Codó"],
    "GEISE ALINE MACEDO DE MEDEIROS": ["Balsas", "Pinheiro", "Riachão"],
    "CHRISTIANE SILVA GUIMARÃES": ["São Luís", "Caxias"],

    "MADSON": ["São José de Ribamar"],

    "ARYSON PAULINELLE GUTERES COSTA": ["São Luís", "Pedreiras", "Estreito", "Grajaú"],
    "LUCAS SAMPAIO NEVES": ["Imperatriz"]
}

# Determina os meses ativos
if mes_selecionado == "Trimestre":
    meses = ["Abril", "Maio", "Junho"]
else:
    meses = [mes_selecionado]

# Variáveis de cálculo
metas = dados_funcoes[funcao_selecionada]
valor_base = valor_mensal[funcao_selecionada]
cumprimento_total = 0

# Layout horizontal para o Trimestre
if mes_selecionado == "Trimestre":
    st.markdown("### ✅ Marque as metas cumpridas em cada mês:")
    mes_cols = st.columns(3)
else:
    mes_cols = [st]

# Loop de meses
for idx, mes in enumerate(meses):
    with mes_cols[idx if mes_selecionado == "Trimestre" else 0]:
        st.markdown(f"**{mes}**")
        for meta, peso in metas:
            if meta == "Produção":
                if funcao_selecionada == "GERENTE" and empresa_selecionada:
                    st.markdown(f"🔸 **Produção por Cidade - {empresa_selecionada}**")
                    for cidade, cidade_peso in pesos_producao_por_empresa[empresa_selecionada].items():
                        key = f"{meta}_{empresa_selecionada}_{cidade}_{mes}"
                        if st.checkbox(f"{cidade} ({cidade_peso}% da produção)", key=key):
                            proporcao = cidade_peso / 100
                            cumprimento_total += proporcao * peso

                elif funcao_selecionada == "SUPERVISOR" and empresa_selecionada:
                    st.markdown(f"🔸 **Produção por Cidade - Supervisor ({empresa_selecionada})**")
                    supervisor_nome = st.text_input(f"Nome do Supervisor - {mes}:", key=f"super_{mes}")
                    if supervisor_nome.upper() in cidades_por_supervisor:
                        cidades_supervisor = cidades_por_supervisor[supervisor_nome.upper()]
                        peso_por_cidade = peso / len(cidades_supervisor)
                        for cidade in cidades_supervisor:
                            key = f"{meta}_{cidade}_{mes}"
                            if st.checkbox(f"{cidade} ({peso_por_cidade:.1f}% da Produção)", key=key):
                                cumprimento_total += peso_por_cidade
                    else:
                        st.warning("⚠️ Supervisor não encontrado. Digite exatamente como cadastrado.")

                elif funcao_selecionada in ["VISTORIADOR", "ATENDENTE"]:
                    key = f"{meta}_{mes}"
                    if st.checkbox(f"{meta} ({peso}%)", key=key):
                        cumprimento_total += peso
            else:
                key = f"{meta}_{mes}"
                if st.checkbox(f"{meta} ({peso}%)", key=key):
                    cumprimento_total += peso

# Cálculo final
valor_total = valor_base * len(meses)
valor_recebido = valor_total * (cumprimento_total / 100)
valor_perdido = valor_total - valor_recebido

st.markdown("---")
st.markdown(f"### 🎯 Resultado da Simulação - **{mes_selecionado} | {empresa_selecionada if empresa_selecionada else ''}**")
st.success(f"💰 Valor possível: R$ {valor_total:,.2f}")
st.info(f"✅ Valor a receber: R$ {valor_recebido:,.2f}")
st.error(f"❌ Valor perdido: R$ {valor_perdido:,.2f}")
st.markdown(f"📊 Cumprimento total: **{cumprimento_total:.1f}%**")
