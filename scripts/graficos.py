import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("../frontend/src/data/movies.csv")

# Top 10 Películas según IMDb
top_10 = df.sort_values(by = "rating", ascending = False).head(10)
plt.figure(figsize=(10, 5))
plt.barh(top_10["name"], top_10["rating"], color=plt.cm.Paired.colors)
plt.xticks(np.arange(0, 10.1, 0.5))
plt.xlabel("Puntuación")
plt.ylabel("Películas")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../frontend/src/assets/graficos/top_10_peliculas.jpg")

# Distribución de los géneros más comunes
generos_separados = df["genre"].dropna().str.split(",")
todos_los_generos = [g.strip() for lista in generos_separados for g in lista]
conteo_generos = pd.Series(todos_los_generos).value_counts()
generos_comunes = conteo_generos.head(10)
otros = conteo_generos[10:].sum()
generos_comunes["Otros"] = otros
colors = plt.cm.Set3.colors[:len(generos_comunes)]
plt.figure(figsize=(10, 10))
plt.pie(generos_comunes, labels=generos_comunes.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(edgecolor='white'))
plt.tight_layout()
plt.savefig("../frontend/src/assets/graficos/generos_comunes.jpg")
plt.close()

# Directores con más películas
directores_separados = df["directors"].dropna().str.split(",")
todos_los_directores = [d.strip() for lista in directores_separados for d in lista]
conteo_directores = pd.Series(todos_los_directores).value_counts()
directores_comunes = conteo_directores.head(10)
plt.figure(figsize=(10,5))
plt.barh(directores_comunes.index, directores_comunes.values, color=plt.cm.Paired.colors)
plt.xlabel("Cantidad")
plt.ylabel("Nombre de los Directores")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../frontend/src/assets/graficos/top_directores.jpg")

# Actores más solicitados 
actores_separados = df["casts"].dropna().str.split(",")
todos_los_actores = [actor.strip() for lista in actores_separados for actor in lista]
conteo_actores = pd.Series(todos_los_actores).value_counts()
top_10_actores = conteo_actores.head(10)
plt.figure(figsize=(10,5))
plt.barh(top_10_actores.index, top_10_actores.values, color = plt.cm.Set2.colors)
plt.xlabel("Películas interpretadas")
plt.gca().invert_yaxis()
plt.xticks(range(0, max(top_10_actores.values)+1))
plt.tight_layout()
plt.savefig("../frontend/src/assets/graficos/actores_solicitados.jpg")

# Conversión de valores "Not Available" a valores númericos
df["box_office"] = df["box_office"].replace("Not Available", pd.NA)
df["budget"] = df["budget"].replace("Not Available", pd.NA)

df["box_office"] = pd.to_numeric(df["box_office"], errors="coerce")
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")

# 10 Películas más Taquilleras
taquilla = df.sort_values(by="box_office", ascending=False).head(10)
plt.figure(figsize=(15, 5))
plt.barh(taquilla['name'], taquilla["box_office"] / 1e6, color = plt.cm.Set2.colors)
plt.xlabel("Recaudación (En millones de USD)")
plt.xticks(rotation = 45)
plt.ylabel("Películas")
plt.gca().invert_yaxis()
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}M'))
plt.tight_layout()
plt.savefig("../frontend/src/assets/graficos/peliculas_taquilleras.jpg")

# Conversión a Dolares
def convertir_a_dolares(row):
    if row['name'] == "Princess Mononoke":
        return row['budget'] * 0.0077
    elif row['name'] == "3 Idiots":
        return row['budget'] * 0.012
    return row['budget']

df['budget_usd'] = df.apply(convertir_a_dolares, axis = 1)

# 10 Películas más caras
presupuesto = df.sort_values(by=["budget_usd"], ascending=False).head(10)
plt.figure(figsize= (10,5))
plt.barh(presupuesto["name"], presupuesto["budget_usd"], color = plt.cm.Paired.colors)
plt.xlabel("Presupuesto")
plt.ylabel("Película")
plt.xticks(rotation = 45)
plt.gca().invert_yaxis()
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e6:,.0f}M'))   
plt.tight_layout()
plt.savefig("../frontend/src/assets/graficos/peliculas_caras.jpg")