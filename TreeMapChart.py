import pandas as pd
import plotly.express as px

airbnb_df = pd.read_csv("Airbnb/Airbnb_Data.csv")
airbnb_df = airbnb_df.dropna(subset=['neighbourhood'])

fig = px.treemap(airbnb_df, path=['neighbourhood', 'room_type'], values='log_price')
fig.update_layout(title='Airbnb Listings TreeMap Chart')
fig.show()
