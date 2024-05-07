import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_data = load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target

plt.figure(figsize=(12,6))
pd.plotting.parallel_coordinates(iris_df, 'target', colormap='viridis')

plt.title('Parallel Coordinate Plot of Iris Flower Features')
plt.xlabel('Features')
plt.ylabel('Feature Values')

plt.show()
