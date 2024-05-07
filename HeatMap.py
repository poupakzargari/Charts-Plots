import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

url = "Covid19/country_vaccinations.csv"
covid_vaccination_df = pd.read_csv(url)

print(covid_vaccination_df.dtypes)

numeric_columns = covid_vaccination_df.select_dtypes(include=['float64', 'int64']).columns
covid_vaccination_numeric_df = covid_vaccination_df[numeric_columns].dropna()

plt.figure(figsize=(12, 8))
sns.heatmap(covid_vaccination_numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of COVID-19 Vaccination Progress Data')
plt.show()
