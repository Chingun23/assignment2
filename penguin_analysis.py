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