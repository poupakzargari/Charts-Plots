import pandas as pd
import zipfile
import requests
import io
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

zip_file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00360/AirQualityUCI.zip"

response = requests.get(zip_file_url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))

zip_file.extractall("./air_quality_data")
excel_file_path = "./air_quality_data/AirQualityUCI.xlsx"
df = pd.read_excel(excel_file_path)

df.dropna(inplace=True)
df['Datetime'] = df['Date'].astype(str) + ' ' + df['Time'].astype(str)
df['Datetime'] = pd.to_datetime(df['Datetime'])
df_selected = df[['Datetime', 'CO(GT)']]

plt.figure(figsize=(10, 6))
plt.plot(df_selected['Datetime'], df_selected['CO(GT)'])

# Adjusting the range of x-axis and y-axis
plt.xlim(df_selected['Datetime'].min(), df_selected['Datetime'].max())
plt.ylim(0, df_selected['CO(GT)'].max() + 1)

plt.xlabel('Date')
plt.ylabel('CO(GT)')
plt.title('CO(GT) Levels Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
