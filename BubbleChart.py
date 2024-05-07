import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
df = pd.read_csv(url, delimiter=';')

x_variable = 'fixed acidity'
y_variable = 'alcohol'

bubble_size_variable = 'quality'

plt.figure(figsize=(10, 6))
plt.scatter(df[x_variable], df[y_variable], s=df[bubble_size_variable] * 10, alpha=0.5)
plt.xlabel(x_variable)
plt.ylabel(y_variable)
plt.title(f'Bubble Chart of Wine Quality ({x_variable} vs. {y_variable})')
plt.grid(True)
plt.tight_layout()
plt.show()
