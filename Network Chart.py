import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv('github_repo/Github_data.csv')
print(df.head())

collaborations = df[['user', 'fork']].drop_duplicates()

def convert_forks_to_numeric(fork):
    if 'k' in fork:
        return float(fork.replace('k', '')) * 1000  # Convert '18.1k' to 18100
    elif 'M' in fork:
        return float(fork.replace('M', '')) * 1000000  # Convert '2.5M' to 2500000
    else:
        return float(fork)  # Convert other numerical values to float


collaborations['fork'] = collaborations['fork'].apply(convert_forks_to_numeric)
G = nx.DiGraph()

for index, row in collaborations.iterrows():
    owner = row['user']
    forks = row['fork']
    G.add_node(owner)
    G.add_edge(owner, 'repository', weight=forks)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', linewidths=1, font_size=12)

plt.show()
