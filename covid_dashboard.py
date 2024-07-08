import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL des données COVID-19
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Lire les données directement depuis l'URL
data = pd.read_csv(url)

# Filtrer les données pour la France
france_data = data[data["location"] == "France"]

# Sélectionner les colonnes pertinentes
france_data = france_data[
    ["date", "new_cases", "new_deaths", "total_cases", "total_deaths"]
]

# Convertir la colonne date en type datetime
france_data["date"] = pd.to_datetime(france_data["date"])

# Configurer les paramètres de Seaborn
sns.set(style="darkgrid")

# Créer une figure et des axes
fig, ax = plt.subplots(2, 1, figsize=(14, 10))

# Visualiser les nouveaux cas quotidiens
sns.lineplot(x="date", y="new_cases", data=france_data, ax=ax[0])
ax[0].set_title("Nouveaux Cas Quotidiens en France")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Nouveaux Cas")

# Visualiser les nouveaux décès quotidiens
sns.lineplot(x="date", y="new_deaths", data=france_data, ax=ax[1])
ax[1].set_title("Nouveaux Décès Quotidiens en France")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Nouveaux Décès")

# Afficher les graphiques
plt.tight_layout()
plt.show()
