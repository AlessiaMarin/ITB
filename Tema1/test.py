import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report


#1
drive.mount('/content/drive')
base = '/content/drive/MyDrive/Colab Notebooks/archive'
pokemon = pd.read_csv(f'{base}/pokemon.csv')
combats = pd.read_csv(f'{base}/combats.csv')

print("Header:\n", pokemon.columns.tolist())
print("\nPrimele randuri:\n", pokemon.head())
print("\nInformatii:")
pokemon.info()
print("\nDimensiune:", pokemon.shape)
print("\nStatistici:\n", pokemon.describe())
print("\nValori lipsa:\n", pokemon.isna().sum())

pokemon['Type 2'] = pokemon['Type 2'].fillna('None')
pokemon = pokemon.dropna(subset=['Name'])
print("\nDupa curatare, valori lipsa:\n", pokemon.isna().sum())

pokemon['Legendary'] = pokemon['Legendary'].astype(int)

pokemon_enc = pd.get_dummies(pokemon, columns=['Type 1', 'Type 2'], dtype=int)
print("\nDupa one-hot:", pokemon_enc.shape)

#2
stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Legendary']
p = pokemon.set_index('#')
lupte = combats[combats['First_pokemon'].isin(p.index) & combats['Second_pokemon'].isin(p.index)]

X = p.loc[lupte['First_pokemon'], stats].values - p.loc[lupte['Second_pokemon'], stats].values
y = (lupte['Winner'] == lupte['First_pokemon']).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model1 = LogisticRegression(max_iter=1000)
model1.fit(X_train, y_train)

model2 = RandomForestClassifier(random_state=42)
model2.fit(X_train, y_train)


print(f"Cate sunt in train ,cate in test: ", X_train.shape, X_test.shape)
print(f"Scor de acuratete regresie logistica: ",model1.score(X_test, y_test))
print(f"Scor de acuratete random forest: ",model2.score(X_test, y_test))

def lupta(pokemon1, pokemon2):
  pok1=p[p['Name']==pokemon1][stats].values
  pok2=p[p['Name']==pokemon2][stats].values
  dif=pok1-pok2
  predictie=model2.predict(dif)[0]
  prob = model2.predict_proba(dif)[0][1]
  if predictie==1:
    castig=pokemon1
  else:
    castig=pokemon2
  print(castig)
lupta('Charizard', 'Bidoof')
