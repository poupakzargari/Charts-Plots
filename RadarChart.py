import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('UCI/heart_disease_uci.csv')

print(df.head())

patient_index = 0

metrics = ['age', 'trestbps', 'chol', 'oldpeak']

values = df.iloc[patient_index][metrics].values.tolist()

num_metrics = len(metrics)
angles = np.linspace(0, 2 * np.pi, num_metrics, endpoint=False).tolist()

values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.6)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics)
ax.set_title('Heart Disease Diagnosis Radar Chart (Patient {})'.format(patient_index))

plt.show()
