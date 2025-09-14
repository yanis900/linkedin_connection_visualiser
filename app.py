import pandas as pd
import networkx as nx
from pyvis.network import Network
import janitor
from IPython.display import display, HTML

connections_data = pd.read_csv("Connections.csv", skiprows=2)
formatted_connections_data = (
    connections_data.clean_names()
    .drop(columns=["last_name", "email_address"])
    .dropna(subset=["company", "position"])
)
formatted_connections_data["connected_on"] = pd.to_datetime(
    formatted_connections_data["connected_on"], format="%d %b %Y"
)

messages_data = pd.read_csv('Messages.csv')
messages_data = messages_data.clean_names()

message_senders_full = messages_data['from'].dropna().unique()
message_senders = set(name.split()[0] for name in message_senders_full)
nt = Network(notebook=True)
g = nx.Graph()

default_icon = {"face": "FontAwesome", "code": "\uf0c0", "size": 50, "color": "#3449eb"}

companies = formatted_connections_data["company"].unique()
for company in companies:
    company_count = formatted_connections_data[
        formatted_connections_data["company"] == company
    ].shape[0]
    clean_company = company.replace(" ", "").lower()
    logo_url = f"https://logo.clearbit.com/{clean_company}.com"

    g.add_node(
        company,
        size=company_count * 5,
        # color="#3449eb",
        title=f"{company} ({company_count} connections)",
        shape="circularImage",
        image=logo_url,
    )
    g.add_edge("You", company, color="grey")

    persons = formatted_connections_data[formatted_connections_data["company"] == company]
    for _, person in persons.iterrows():
        person_name = person["first_name"]
        position = person["position"]
        title = f"{person_name} - {position}"
        color = "#e74c3c" if person_name in message_senders else "#85c1b0"
        g.add_node(person_name, size=5, color=color, title=title)
        g.add_edge(company, person_name, color="lightblue")

nt.from_nx(g)
nt.show("nodes.html")
display(HTML("nodes.html"))
