# 🌍 AI Economic Intelligence Platform

> Une plateforme d'intelligence économique alimentée par l'IA combinant Data Engineering, Machine Learning, Business Intelligence et Intelligence Artificielle Générative.

[![Python](https://img.shields.io/badge/Python-3.14-blue)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)]()
[![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)]()
[![Ollama](https://img.shields.io/badge/Ollama-LLM%20Local-green)]()
[![DeepSeek](https://img.shields.io/badge/DeepSeek-R1%208B-purple)]()

---

# 🚀 Démonstration

### 🌐 Application Streamlit

👉 **Accéder à l'application :**

**(https://aieconomicintelligenceplatform-fqcyieya29bhhgmybbwi4n.streamlit.app/)**

---

# 📖 Présentation du projet

Ce projet consiste à développer une plateforme d'intelligence économique capable de :

- Collecter automatiquement des données macroéconomiques ;
- Stocker les données dans PostgreSQL ;
- Construire des modèles de Machine Learning ;
- Réaliser des prévisions jusqu'en 2030 ;
- Produire des tableaux de bord interactifs ;
- Générer automatiquement des rapports économiques ;
- Répondre à des questions en langage naturel grâce à l'IA.

---

# ✨ Fonctionnalités

## 📊 Tableau de bord exécutif

- Dashboard Streamlit interactif
- Filtres par pays
- Sélection des années
- Indicateurs économiques
- Visualisation des tendances du PIB

---

## 🤖 Assistant IA économique

L'utilisateur peut poser des questions telles que :

- Quel pays aura le PIB le plus élevé en 2030 ?
- Comparer le Ghana et le Sénégal.
- Quel pays connaît la plus forte croissance ?
- Quel est le pays le plus attractif pour les investisseurs ?

L'assistant est basé sur :

- Ollama
- DeepSeek-R1 8B

---

## 🧠 Analyse économique en langage naturel

Génération automatique :

- Résumé exécutif ;
- Analyse par pays ;
- Comparaison régionale ;
- Recommandations stratégiques ;
- Prévisions économiques.

---

## 📈 Prévisions économiques

Prévisions jusqu'en **2030** à l'aide de :

- Random Forest Regressor

Indicateurs étudiés :

- PIB ;
- Inflation ;
- Population ;
- Chômage.

---

## 📄 Génération automatique de rapports

Production automatique :

- Rapports texte ;
- Rapports PDF professionnels.

---

## 📊 Business Intelligence

Tableaux de bord Power BI :

- Évolution du PIB ;
- Analyse de l'inflation ;
- Population ;
- Chômage.

---

# 🏗 Architecture du projet

```text
API World Bank
       │
       ▼
Python ETL
(extract_worldbank.py)
       │
       ▼
PostgreSQL
(economic_data)
       │
       ▼
Machine Learning
(train_model.py)
       │
       ▼
Table predictions
       │
       ▼
Vue SQL
(v_gdp_real_predicted)
       │
       ▼
Power BI
       │
       ▼
Application Streamlit
       │
       ▼
Ollama + DeepSeek
       │
       ▼
Rapports IA
```

---

# 🛠 Technologies utilisées

## Data Engineering

- Python
- Pandas
- SQLAlchemy
- PostgreSQL

## Machine Learning

- Scikit-Learn
- Random Forest

## Business Intelligence

- Power BI
- Plotly

## Application Web

- Streamlit

## Intelligence Artificielle

- Ollama
- DeepSeek-R1 8B

## Base de données

- PostgreSQL 17
- Render PostgreSQL

---

# 📂 Structure du projet

```text
global-economic-intelligence-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│     └── raw/
│           └── worldbank_data.csv
│
├── reports/
│     ├── economic_ai_report.txt
│     └── economic_ai_report.pdf
│
├── sql/
│
├── src/
│     ├── extract_worldbank.py
│     ├── load_postgres.py
│     ├── train_model.py
│     ├── ai_report.py
│     ├── ai_report_local.py
│     └── ai_assistant.py
│
└── .env
```

---

# ⚙ Installation

## Cloner le dépôt

```bash
git clone https://github.com/VOTRE_USERNAME/ai-economic-intelligence-platform.git

cd ai-economic-intelligence-platform
```

---

## Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# 🗄 Configuration PostgreSQL

Créer un fichier `.env` :

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=economic_ai
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
```

---

# 📥 Extraction des données

```bash
python src/extract_worldbank.py
```

---

# 🗃 Chargement dans PostgreSQL

```bash
python src/load_postgres.py
```

---

# 📈 Entraînement du modèle

```bash
python src/train_model.py
```

Les prédictions sont enregistrées dans :

```text
predictions
```

---

# 🤖 Génération de rapports IA

```bash
python src/ai_report_local.py
```

---

# 📊 Lancement du dashboard Streamlit

```bash
streamlit run app.py
```

---

# 🌐 Déploiement

## Frontend

- Streamlit Cloud

## Base de données

- Render PostgreSQL

## Gestion du code

- GitHub

---

# 🔒 Sécurité

Les informations sensibles sont protégées grâce à :

```python
st.secrets["DATABASE_URL"]
```

Aucun identifiant n'est exposé dans le dépôt GitHub.

---

# 🎯 Compétences mises en œuvre

Ce projet mobilise des compétences en :

### Data Engineering

- Python
- ETL
- PostgreSQL

### Data Science

- Machine Learning
- Prévisions économiques

### Business Intelligence

- Power BI
- Data Visualisation

### Intelligence Artificielle

- LLM
- Ollama
- DeepSeek

### Développement

- Streamlit
- SQLAlchemy

### Déploiement

- GitHub
- Streamlit Cloud
- Render

---

# 📌 Feuille de route

## ✅ Réalisé

- [x] Extraction des données World Bank
- [x] Chargement PostgreSQL
- [x] Prévisions Machine Learning
- [x] Dashboard Power BI
- [x] Dashboard Streamlit
- [x] Génération de rapports IA
- [x] Déploiement PostgreSQL sur Render
- [x] Connexion sécurisée via Streamlit Secrets

## 🚀 Prochaines améliorations

- [ ] Export PDF professionnel
- [ ] Authentification des utilisateurs
- [ ] Docker
- [ ] GitHub Actions
- [ ] Pipeline MLOps
- [ ] Cartographie mondiale interactive
- [ ] Assistant IA multi-modèles
- [ ] Déploiement AWS

---

# 👨‍💻 Auteur

## Gael Kodia

- LinkedIn : https://www.linkedin.com/in/gael-kodia
- GitHub : https://github.com/gael199

---

# ⭐ Si ce projet vous intéresse, n'hésitez pas à laisser une étoile sur le dépôt GitHub !
