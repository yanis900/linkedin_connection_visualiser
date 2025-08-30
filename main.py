import pandas as pd
import networkx as nx
from pyvis.network import Network
import janitor
import matplotlib.pyplot as plt

connections_data = pd.read_csv('Connections.csv', skiprows=2)
# print(connections_data)
connections_data.info()


formatted_connections_data = (
    connections_data
    .clean_names() 
    .drop(columns=['first_name', 'last_name', 'email_address'])
    .dropna(subset=['company', 'position']) 
  )
formatted_connections_data['connected_on'] = pd.to_datetime(formatted_connections_data['connected_on'], format='%d %b %Y')


ax = formatted_connections_data['company'].value_counts().head(20).plot(kind="barh")
ax.invert_yaxis()
plt.show()
