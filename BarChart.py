import pandas as pd
import zipfile
import requests
import io
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank-additional.zip"
response = io.BytesIO(requests.get(url).content)
zip_file = zipfile.ZipFile(response, 'r')


csv_file_name = "bank-additional/bank-additional-full.csv"

df = pd.read_csv(zip_file.open(csv_file_name), sep=';')

categorical_variable = 'job'

category_counts = df[categorical_variable].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.xlabel(categorical_variable)
plt.ylabel('Count')
plt.title(f'Distribution of {categorical_variable}')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

from ucimlrepo import fetch_ucirepo

bank_marketing = fetch_ucirepo(id=222)

X = bank_marketing.data.features
y = bank_marketing.data.targets

print(bank_marketing.metadata)
print(bank_marketing.variables)
