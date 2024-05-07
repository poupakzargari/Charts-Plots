import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_df = pd.read_csv(url, sep=";")

plt.figure(figsize=(12, 6))
sns.boxplot(data=wine_quality_df)
plt.title('Box Plot of Physiocochemical Properties and Quality Ratings of Red Wine')
plt.ylabel('Values')

plt.show()
