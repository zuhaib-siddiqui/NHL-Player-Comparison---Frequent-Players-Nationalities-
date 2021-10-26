import matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#Importing Data
nhl = pd.read_csv("NHL Player Stats.csv")
pd.set_option("display.max.rows", None)
pd.set_option("display.max.columns", None)

#Pie Chart, Country Variables
canada = nhl.loc[nhl.Nationality == "Canada"].count()[0]
us = nhl.loc[nhl.Nationality == "USA"].count()[0]
Sweden = nhl.loc[nhl.Nationality == "Sweden"].count()[0]
Russia = nhl.loc[nhl.Nationality == "Russia"].count()[0]
Slovak = nhl.loc[nhl.Nationality == "Slovakia"].count()[0]
Finland = nhl.loc[nhl.Nationality == "Finland"].count()[0]
Czech = nhl.loc[nhl.Nationality == "Czech Republic"].count()[0]
Slovenia = nhl.loc[nhl.Nationality == "Slovenia"].count()[0]
Germany = nhl.loc[nhl.Nationality == "Germany"].count()[0]

#Qol Variables
label = ["Canada", "USA", "Sweden", "Russia", "Slovakia", "Finland", "Czech", "Slovenia", "Germany"]
colour = ["Red", "Blue", "Yellow", "#82a2fa", "#ff7373", "#73faff", "#480ac4", "#7d0227", "Gold"]
explode = (0, 0, 0, 0, .8, .4, .4, .6, 0)

#Pie Chart for player nationality distribution
plt.pie([canada, us, Sweden, Russia, Slovak, Finland, Czech, Slovenia, Germany], labels=label, colors=colour, autopct="%.2f %%", explode=explode)
plt.title("NHL Top 10 Score Leaders Nationality from 2009-2021")
plt.show()

#Most frequent players
how_many_times = nhl["Name"].value_counts()[:5]
names = nhl["Name"].value_counts()[:5].index.tolist()
print(how_many_times)
labels =([names[0], names[1], names[2], names[3], names[4]])
plt.xticks(fontsize=6)
plt.bar(labels, how_many_times)
plt.xlabel("Players")
plt.ylabel("Number of Times in the Top 10")
plt.title("Most Frequent Goal Scoring Leaders 2009-2021")
plt.show()

