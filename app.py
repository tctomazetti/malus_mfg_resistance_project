import streamlit as st
import pandas as pd

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
st.title("🍎 Projeto: Caracterização da Herança e Teste de Alelismo para a " \
"Resistência à Mancha Foliar de Glomerella em Macieira")
st.markdown("---")

# --- BARRA LATERAL (MENU DE NAVEGAÇÃO) ---
# Cria um menu na lateral para navegar entre as seções do dashboard
st.sidebar.header("Navegação")
pagina_selecionada = st.sidebar.radio(
    "Selecione uma seção:",
    ["Resumo do Projeto", "A Equipe", "Orçamento Detalhado", "Metodologia e Entregáveis"]
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
    # st.image("caminho/para/imagem_da_doenca.jpg", caption="Folha com sintomas da Mancha Foliar de Glomerella")


# 2. PÁGINA: A EQUIPE
elif pagina_selecionada == "A Equipe":
    st.header("👥 Equipe Multidisciplinar")
    st.write("O sucesso do projeto é garantido por uma equipe com vasta experiência em áreas complementares.")

    # Crie duas ou mais colunas para organizar os membros da equipe
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

    # Adicione mais membros conforme necessário, criando novas linhas de colunas
    st.markdown("---")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Liane Bahr Thurow")
        st.write("**Melhoramento Genético e Genética Molecular**")
        st.write("Epagri - Estação Experimental de São Joaquim")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/3675128575984460")

    with col4:
        st.subheader("Marcelo Couto")
        st.write("**Fitotecnia**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/4833006168241192")
    
    st.markdown("---")
    col5, _ = st.columns(2)

    with col5:
        st.subheader("Claudio Ogoshi")
        st.write("**Fitopatologia**")
        st.write("Epagri - Estação Experimental de Caçador")
        st.link_button("Acessar Currículo Lattes", "http://lattes.cnpq.br/1910689375970542")


# 3. PÁGINA: ORÇAMENTO DETALHADO
elif pagina_selecionada == "Orçamento Detalhado":
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
            "Item": "Sistema de Irrigação Automatizado",
            "Valor (R$)": 21_200,
            "Justificativa": "Garantir a uniformidade no manejo hídrico das plantas do experimento"
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


# 4. PÁGINA: METODOLOGIA E ENTREGÁVEIS
elif pagina_selecionada == "Metodologia e Entregáveis":
    st.header("🔬 Metodologia e Resultados Esperados")

    st.subheader("Desenho Experimental")
    # Você pode usar a imagem do fluxograma que criamos para os slides
    # st.image("caminho/para/fluxograma_metodologia.png")
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

