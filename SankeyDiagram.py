import pandas as pd
import plotly.graph_objects as go
import zipfile
import io
import requests

url_red = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
url_white = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
df_red = pd.read_csv(url_red, delimiter=';')
df_white = pd.read_csv(url_white, delimiter=';')

df_red['Type'] = 'Red'
df_white['Type'] = 'White'

df = pd.concat([df_red, df_white])
sankey_data = df.groupby(['quality', 'Type']).size().reset_index(name='count')

source_nodes = list(sankey_data['quality'])
target_nodes = list(sankey_data['Type'])
values = list(sankey_data['count'])

# Creating the Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=list(set(source_nodes + target_nodes))
    ),
    link=dict(
        source=[source_nodes.index(source) for source in source_nodes],
        target=[len(source_nodes) + target_nodes.index(target) for target in target_nodes],
        value=values
    )
)])

fig.update_layout(title_text="Wine Quality Sankey Diagram", font_size=10)
fig.show()
