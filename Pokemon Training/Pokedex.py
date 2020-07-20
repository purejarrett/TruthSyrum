import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
# %matplotlib inline

pokemon = pd.read_csv("pokemon.csv")

print(pokemon.head(5))

pokemon2 = pokemon["abilities"].str.split(", ", n = 1, expand = True)
pokemon2