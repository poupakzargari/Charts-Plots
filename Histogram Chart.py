import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

titanic_df = pd.read_csv("Titanic/tested.csv")

plt.hist(titanic_df['Age'], bins=20, color='skyblue', edgecolor='black')

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Passenger Ages on Titanic')

plt.show()
