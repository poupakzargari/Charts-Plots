from ucimlrepo import fetch_ucirepo
import pandas as pd
import requests
import zipfile
import io
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets
print(iris.metadata)
print(iris.variables)

url = "http://archive.ics.uci.edu/static/public/53/iris.zip"
response = requests.get(url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))
zip_file.extractall("./iris_data")

csv_file_name = "iris.data"
df = pd.read_csv(zip_file.open(csv_file_name), header=None)

x_column = 0  # Assuming 'sepal_length' is the first column
y_column = 1  # Assuming 'sepal_width' is the second column

plt.figure(figsize=(10, 6))
plt.scatter(df[x_column], df[y_column])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot of Sepal Length vs. Sepal Width")
plt.grid(True)
plt.tight_layout()
plt.show()

