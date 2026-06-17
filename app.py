import os
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
from sqlalchemy import create_engine
from ollama import chat

load_dotenv()

st.set_page_config(
    page_title="AI Economic Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

DATABASE_URL = "postgresql://economic_ai_user:Qk0Zgpqhwrx7YXwo7FA93SKdaP15UzrB@dpg-d8ph2ia8qa3s73bsa0mg-a.oregon-postgres.render.com/economic_ai"

engine = create_engine(DATABASE_URL)


@st.cache_data
def load_data():
    query = """
    SELECT
        country_name,
        year,
        value,
        data_type
    FROM v_gdp_real_predicted
    ORDER BY country_name, year;
    """
    return pd.read_sql(query, engine)

df = load_data()

st.title("📊 AI Economic Intelligence Platform")
st.caption("PostgreSQL · Python · Machine Learning · Power BI · Ollama · DeepSeek")

countries = st.sidebar.multiselect(
    "Choisir les pays",
    sorted(df["country_name"].unique()),
    default=sorted(df["country_name"].unique())
)

year_range = st.sidebar.slider(
    "Période",
    int(df["year"].min()),
    int(df["year"].max()),
    (2020, int(df["year"].max()))
)

filtered = df[
    (df["country_name"].isin(countries)) &
    (df["year"].between(year_range[0], year_range[1]))
]

col1, col2, col3 = st.columns(3)

latest_year = filtered["year"].max()
latest_df = filtered[filtered["year"] == latest_year]

col1.metric("Dernière année", latest_year)
col2.metric("Nombre de pays", filtered["country_name"].nunique())
col3.metric("PIB total", f"{latest_df['value'].sum()/1e9:,.2f} Md $")

st.subheader("📈 PIB réel et prédit")

fig = px.line(
    filtered,
    x="year",
    y="value",
    color="country_name",
    line_dash="data_type",
    markers=True,
    title="PIB réel vs PIB prédit"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 Données économiques")
st.dataframe(filtered, use_container_width=True)

st.subheader("🤖 Assistant IA économique")

question = st.text_input(
    "Pose une question à l'assistant IA",
    placeholder="Exemple : Quel pays aura le PIB le plus élevé en 2030 ?"
)

if st.button("Analyser avec l'IA"):
    if question.strip() == "":
        st.warning("Écris une question.")
    else:
        with st.spinner("Analyse en cours avec DeepSeek..."):
            prompt = f"""
Tu es un assistant économique intelligent.

Réponds en français, clairement et professionnellement.
Utilise uniquement les données ci-dessous.

Question :
{question}

Données :
{filtered.to_string(index=False)}
"""

            response = chat(
                model="deepseek-r1:8b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.success("Analyse terminée")
            st.write(response.message.content)

st.subheader("📄 Rapport PDF")

if st.button("Générer un rapport économique"):
    with st.spinner("Génération du rapport IA..."):
        prompt = f"""
Tu es un économiste senior.

Rédige un rapport économique professionnel en français avec :

1. Résumé exécutif
2. Analyse par pays
3. Comparaison régionale
4. Prévisions jusqu'en 2030
5. Recommandations stratégiques

Données :
{filtered.to_string(index=False)}
"""

        response = chat(
            model="deepseek-r1:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        os.makedirs("reports", exist_ok=True)

        with open("reports/streamlit_report.txt", "w", encoding="utf-8") as f:
            f.write(response.message.content)

        st.success("Rapport généré : reports/streamlit_report.txt")
        st.download_button(
            label="Télécharger le rapport TXT",
            data=response.message.content,
            file_name="economic_report.txt",
            mime="text/plain"
        )
