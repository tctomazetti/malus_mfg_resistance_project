import streamlit as st
import pandas as pd
import plotly.express as px

formatador_brl = lambda x: f"R$ {x:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

# --- CONFIGURAÇÃO DA PÁGINA ---
# Define o título da página, o ícone (emoji de maçã) e o layout
st.set_page_config(
    page_title="Projeto Resistência MFG Herança e Alelismo",
    page_icon="🍎",
    layout="wide"
)

# --- CABEÇALHO ---
# Título principal do dashboard
st.title("🍎 Resistência MFG Herança e Alelismo")
st.markdown("---")

# --- BARRA LATERAL (MENU DE NAVEGAÇÃO) ---
# Cria um menu na lateral para navegar entre as seções do dashboard
st.sidebar.header("Navegação")
pagina_selecionada = st.sidebar.radio(
    "Selecione uma seção:",
    [
        "Resumo do Projeto",
        "A Equipe",
        "Cronograma de Execução",
        "Orçamento Detalhado",
        "Metodologia e Entregáveis"
    ]
)
st.sidebar.markdown("---")
st.sidebar.info(
    "Este dashboard contém informações complementares sobre o projeto de pesquisa apresentado. "
    "Navegue pelas seções para explorar os detalhes."
)


# --- CONTEÚDO DAS PÁGINAS ---

# 1. PÁGINA: RESUMO DO PROJETO
if pagina_selecionada == "Resumo do Projeto":
    st.header("🎯 Objetivo Geral")
    st.info(
        """
        **Caracterizar a herança genética da resistência à Mancha Foliar de Glomerella (MFG) na seleção 'Gala Gui', 
        investigando o modo de herança, o padrão de dominância e a relação de alelismo com o gene de resistência da cultivar Fuji.**
        """
    )

    st.subheader("Justificativa")
    st.write(
        """
        A produção de maçãs em Santa Catarina é altamente dependente de cultivares suscetíveis à MFG, como a 'Gala'. 
        A 'Fuji' possui resistência monogênica, mas a recente descoberta da resistência na seleção 'Gala Gui' abre uma nova fronteira. 
        No entanto, a base genética dessa nova resistência é desconhecida.
        
        Este projeto é crucial para determinar se a 'Gala Gui' carrega um novo gene de resistência, o que permitiria o desenvolvimento 
        de cultivares com resistência mais durável através da piramidação de genes, reduzindo a dependência de defensivos químicos e 
        aumentando a sustentabilidade da pomicultura.
        """
    )
    # Você pode adicionar uma imagem aqui se quiser
    st.image("img/mfg.jpg", caption="Folha com sintomas da Mancha Foliar de Glomerella")


# 2. PÁGINA: A EQUIPE
elif pagina_selecionada == "A Equipe":
    st.header("👥 Equipe Multidisciplinar")
    st.write("O sucesso do projeto é garantido por uma equipe com vasta experiência em áreas complementares.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tiago Camponogara Tomazetti")
        st.write("**Coordenação e Melhoramento Genético**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/5201113528430333" )

    with col2:
        st.subheader("Marcus Vinícius Kvitschal")
        st.write("**Melhoramento Genético**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/6890936860763328")

    st.markdown("---")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Ivan Dagoberto Faoro")
        st.write("**Melhoramento Genético e Seleção clonal**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/7644524602791533")

    with col4:
        st.subheader("Liane Bahr Thurow")
        st.write("**Melhoramento Genético e Genética Molecular**")
        st.write("Epagri - Estação Experimental de São Joaquim")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/3675128575984460")
    
    st.markdown("---")
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Marcelo Couto")
        st.write("**Fitotecnia**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/4833006168241192")

    with col6:
        st.subheader("Claudio Ogoshi")
        st.write("**Fitopatologia**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/1910689375970542")


# 3. PÁGINA: CRONOGRAMA DE EXECUÇÃO
elif pagina_selecionada == "Cronograma de Execução":
    st.header("📆 Cronograma de Execução (24 Meses)")

    dados_cronograma = [
        dict(
            Task="A1",
            Start='2026-06-01',
            Finish='2026-10-31',
            Resource="2026"
        ),
        dict(
            Task="A2",
            Start='2026-09-01',
            Finish='2027-01-31',
            Resource="2026 & 2027"
        ),
        dict(
            Task="A3",
            Start='2027-02-01',
            Finish='2027-09-30',
            Resource="2027"
        ),
        dict(
            Task="A4",
            Start='2027-10-01',
            Finish='2028-01-31',
            Resource="2027 & 2028"
        ),
        dict(
            Task="A5",
            Start='2028-02-01',
            Finish='2028-05-31',
            Resource="2028"
        ),
    ]
    df_cronograma = pd.DataFrame(dados_cronograma)

    # Criação do Gráfico de Gantt com Plotly Express
    fig = px.timeline(
        df_cronograma,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Resource",
        title="Fases e Atividades do Projeto",
        labels={"Task": "Atividades", "Resource": "Período"},
        color_discrete_map={
            "2026": "#FADADD",      # Rosa claro (Light Pink)
            "2026 & 2027": "#F4978E",  # Salmão (Salmon)
            "2027": "#D90429",      # Vermelho vibrante (Vibrant Red)
            "2027 & 2028": "#8D0801",  # Vermelho escuro (Dark Red)
            "2028": "#640D14"       # Bordô (Maroon/Burgundy)
        }
    )

    # Melhorando a visualização do gráfico
    fig.update_yaxes(autorange="reversed") # Inverte a ordem das tarefas para A1 ficar no topo
    fig.update_layout(
        title_font_size=20,
        font_size=14,
        xaxis_title="Linha do Tempo (Meses)",
        yaxis_title=None, # Remove o título do eixo Y
        legend_title_text='Período de Execução'
    )
    
    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        **Legenda das Atividades:**
        - **A1:** Planejamento, Preparo de Infraestrutura e Manejo dos Parentais.
        - **A2:** Execução dos Cruzamentos, Colheita e Processamento das Sementes.
        - **A3:** Germinação, Cultivo e Manejo das Populações F1.
        - **A4:** Inoculação, Avaliação Fenotípica e Análise Estatística dos Dados.
        - **A5:** Interpretação dos Resultados, Redação de Relatórios e Publicações.
        """
    )


# 4. PÁGINA: ORÇAMENTO DETALHADO
elif pagina_selecionada == "Orçamento Detalhado":
    st.header("💰 Orçamento Detalhado")
    st.write("O orçamento total solicitado é de **R$ 200.000,00**, distribuído ao longo de 24 meses.")

    # --- 1. CONSOLIDAR TODOS OS DADOS DO ORÇAMENTO ---
    dados_completos = [
        # Itens de Custeio
        {"Tipo": "Custeio", "Item": "Diárias", "Valor": 59_500},
        {"Tipo": "Custeio", "Item": "Material de Consumo", "Valor": 60_500},
        {"Tipo": "Custeio", "Item": "Passagens", "Valor": 10_000},
        {"Tipo": "Custeio", "Item": "Serviços de Terceiros Pessoa Jurídica", "Valor": 10_000},
        
        # Itens de Capital (Investimento)
        {"Tipo": "Investimento", "Item": "Câmara de Germinação (BOD)", "Valor": 18_800},
        {"Tipo": "Investimento", "Item": "Estereomicroscópio com Câmera", "Valor": 20_000},
        {"Tipo": "Investimento", "Item": "Medidor de Área Foliar", "Valor": 21_200},
    ]
    df_orcamento = pd.DataFrame(dados_completos)

    # --- 2. CRIAR O GRÁFICO DE EXPLOSÃO SOLAR (SUNBURST) ---
    st.subheader("Distribuição Hierárquica do Orçamento")

    fig_sunburst = px.sunburst(
        df_orcamento,
        path=['Tipo', 'Item'],  # Define a hierarquia: 1º anel é 'Tipo', 2º anel é 'Item'
        values='Valor',
        title='Orçamento: Custeio vs. Investimento',
        color='Tipo', # Colore os anéis com base na categoria principal
        color_discrete_map={
            'Custeio': '#D50000',      # Vermelho forte para Custeio
            'Investimento': '#FF8A65', # Vermelho/Laranja claro para Investimento
            '(?)': '#FADADD'          # Cor para o círculo central
        }
    )

    # Melhorando a aparência e informações
    fig_sunburst.update_traces(
        textinfo='label+percent entry', # Mostra o rótulo e o percentual da fatia
        hovertemplate='<b>%{label}</b> Valor: R$ %{value:,.2f} Percentual do Total: %{percentRoot:.2%}',
        insidetextorientation='radial' # Orienta o texto para facilitar a leitura
    )
    fig_sunburst.update_layout(
        title_font_size=20,
        font_size=14
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig_sunburst, use_container_width=True)
    
    st.info(
        """
        **Como ler o gráfico:** O anel interno mostra a divisão geral entre Custeio e Investimento. 
        O anel externo detalha os itens dentro de cada categoria. Clique em uma categoria no anel interno 
        para focar nela (dar "zoom").
        """
    )

    # --- TABELAS DETALHADAS (Opcional, podem ser mantidas para referência) ---
    st.header("💰 Orçamento Detalhado")
    st.write("O orçamento total solicitado é de **R$ 200.000,00**, distribuído ao longo de 24 meses.")

    st.subheader("Despesas de Custeio")
    # Criando um DataFrame do Pandas para a tabela de custeio
    dados_custeio = [
        {
            "Item": "Diárias",
            "Valor (R$)": 59_500,
            "Justificativa": "Deslocamento da equipe para atividades de campo e cruzamentos"
        },
        {
            "Item": "Material de Consumo",
            "Valor (R$)": 60_500,
            "Justificativa": "Insumos para condução das plantas em casa de vegetação (vasos, substrato, fertilizantes, defensivos, etc.)."
        },
        {
            "Item": "Passagens",
            "Valor (R$)": 10_000,
            "Justificativa": "Custos com passagens para participação e apresentação dos resultados em congressos e eventos científicos."
        },
        {
            "Item": "Serviços de Terceiros Pessoa Física",
            "Valor (R$)": 0,
            "Justificativa": "Não há previsão de contratação de serviços de pessoa física neste projeto."
        },
        {
            "Item": "Serviços de Terceiros Pessoa Jurídica",
            "Valor (R$)": 10_000,
            "Justificativa": "Custos com taxas de publicação de artigo científico e inscrição em eventos técnico-científicos."
        }
    ]

    df_custeio = pd.DataFrame(dados_custeio).set_index("Item")
    st.dataframe(
        df_custeio.style.format({
            "Valor (R$)": formatador_brl
        }),
        width="stretch",
        column_config={
            "Item": st.column_config.TextColumn(
                "Elemento de Despesa", # Renomeia o cabeçalho da coluna
                width="medium"
            ),
            "Valor (R$)": st.column_config.TextColumn(
                "Valor (R$)",
                width="small"
            ),
            "Justificativa": st.column_config.TextColumn(
                "Justificativa",
                width="large" # Força esta coluna a se expandir, corrigindo o layout
            )
        }
) # use_container_width faz a tabela ocupar toda a largura

    st.subheader("Despesas de Capital (Equipamentos)")
    # Criando um DataFrame do Pandas para a tabela de capital

    dados_capital = [
        {
            "Item": "Câmara de Germinação (BOD)",
            "Valor (R$)": 18_800,
            "Justificativa": "Controle preciso de temperatura e umidade para inoculação e avaliação"
        },
        {
            "Item": "Estereomicroscópio com Câmera",
            "Valor (R$)": 20_000,
            "Justificativa": "Avaliação detalhada dos sintomas e documentação fotográfica"
        },
        {
            "Item": "Medidor de Área Foliar Portátil e Não Destrutivo",
            "Valor (R$)": 21_200,
            "Justificativa": "Ferramenta de precisão que eleva o rigor da avaliação fenotípica."
        },
    ]

    df_capital = pd.DataFrame(dados_capital).set_index("Item")

    st.dataframe(
        df_capital.style.format({
            "Valor (R$)": formatador_brl
        }),
        width="stretch",
        column_config={
            "Item": st.column_config.TextColumn(
                "Elemento de Despesa", # Renomeia o cabeçalho da coluna
                width="medium"
            ),
            "Valor (R$)": st.column_config.TextColumn(
                "Valor (R$)",
                width="small"
            ),
            "Justificativa": st.column_config.TextColumn(
                "Justificativa",
                width="large" # Força esta coluna a se expandir, corrigindo o layout
            )
        }
    )


# 5. PÁGINA: METODOLOGIA E ENTREGÁVEIS
elif pagina_selecionada == "Metodologia e Entregáveis":
    st.header("🔬 Metodologia e Resultados Esperados")

    st.subheader("Desenho Experimental")

    st.image("img/ed.png")
    st.write(
        """
        O projeto se baseia em cruzamentos controlados para responder a três perguntas fundamentais:
        1.  **Teste de Alelismo:** Cruzamentos recíprocos entre 'Gala Gui' e 'Fuji'.
        2.  **Teste de Dominância:** Cruzamentos recíprocos entre 'Gala Gui' e a suscetível 'Golden Delicious'.
        3.  **Análise de Efeito Materno:** Avaliação dos resultados dos cruzamentos recíprocos.
        
        As populações F1 serão inoculadas com *Colletotrichum spp.* e a segregação fenotípica será analisada estatisticamente (Teste Qui-quadrado).
        """
    )

    st.subheader("Entregáveis do Projeto")
    st.success(
        """
        - **Populações F1:** Obtenção e caracterização de populações segregantes, base para futuros estudos.
        - **Conhecimento Científico:** Elucidação do padrão de dominância e da relação de alelismo do gene da 'Gala Gui'.
        - **Estratégia de Melhoramento:** Definição clara se a estratégia será de **substituição de fontes** ou **piramidação de genes**.
        - **Disseminação:** Publicação de um artigo científico em revista qualificada e apresentação dos resultados em congresso nacional.
        """
    )
    st.image("img/exp_results.png")
