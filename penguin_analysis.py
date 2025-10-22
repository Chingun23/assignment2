import pandas as pd
import matplotlib.pyplot as plt

#load the data set
df = pd.read_csv("penguins.csv")

summary = df.describe()
species_counts = df['species'].value_counts()

summary.to_csv("summary_output.csv")
species_counts.to_csv("species_counts.csv")

species_counts.plot(kind='bar', title='Penguin Species Count')
plt.tight_layout()
plt.savefig("penguin_species_plot.png")

print("Analysis Complete! FIles saved in this folder")

#Add Scatterplot of bill length vs body mass
df.plot.scatter(x='bill_length_mm', y='body_mass_g', title='Bill Length vs Body Mass')
plt.tight_layout()
plt.savefig("penguin_scatterplot.png")

print("Added Scatterplot to analysis")


import statsmodels.api as sm
from statsmodels.formula.api import ols


# Running a typical OLS model
ols_model = ols('body_mass_g ~ C(species) * C(year) + island', 
                data=penguins).fit()
print(ols_model.summary2())

