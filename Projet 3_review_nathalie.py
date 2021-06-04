import numpy as np
import pandas as pd

# Chargement du df1 à partir du fichier csv ou à partir d'un pickle
df1 = pd.DataFrame({
    'energy_100g': np.random.uniform(-1, 4000, size=100),
    'sugars_100g': np.random.uniform(-10, 200, size=100),
    'saturated-fat_100g': np.random.uniform(size=100)
})

"""
 1. Utilisation de la méthode .items() sur un dictionnaire pour faire une boucle for plus Pythonesque
"""
liste_variables_pour_nettoyage = {
    'energy_100g': [0, 3800],  # 3800kJ correspondent à 100g de lipides
    'sugars_100g': [0, 100],  # il y a au maximum 100g de sucre dans 100g d'aliment
    'saturated-fat_100g': [0, 100],
}

for nom, (min_x, max_x) in liste_variables_pour_nettoyage.items():
    count_avant = df1[nom].count()
    df1.loc[(df1[nom] > max_x) | (df1[nom] < min_x), nom] = np.nan
    count_apres = df1[nom].count()
    print(nom, count_avant, count_apres)

"""
2. Possibilité de tester des inégalités sur une pd.Series, pas besoin d'utiliser la méthode .apply() dans ce cas
"""


def boite_moustaches(colonne='energy-kj_100g',
                     min_x=None,
                     max_x=None,
                     unite=None):
    # extraction du dataframe
    ser = df1[colonne]
    # (...)
    ser_bool = (min_x <= ser) & (ser <= max_x)
    # (...)


"""
3. Utiliser un format standard pour la documentation des fonctions, 
par exemple : https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html 
"""


def scatter_plot(ser_x,
                 ser_y,
                 min_x=0,
                 max_x=100,
                 min_y=0,
                 max_y=100,
                 alpha=0.002,
                 unite_x=None,
                 unite_y=None):
    """
    Cette fonction sert à ...

    Args:
        ser_x (pd.Series): cet argument est ...
        ser_y (pd.Series): cet argument est ...
        min_x (float): cet argument est ...
        max_x (float): cet argument est ...
        max_x (float): cet argument est ...
        max_x (float): cet argument est ...
        max_x (float): cet argument est ...
        max_x (float): cet argument est ...

    Returns: (None) displays plot
    """
    pass


"""
4. Utiliser les list comprehensions: https://www.programiz.com/python-programming/list-comprehension
"""

moyennes = [1, 2, 3, 4, 3]
moyenne_globale = 3
effectifs = [10, 122, 23, 1222, 76]

# Option 1
SCE = 0
for i in range(0, len(moyennes)):
    SCE += effectifs[i] * (moyennes[i] - moyenne_globale) ** 2
print(SCE)

# option 2
SCE = sum([effectif * (moyenne - moyenne_globale) ** 2 for effectif, moyenne in zip(effectifs, moyennes)])
print(SCE)
