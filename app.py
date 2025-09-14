import pandas as pd
import networkx as nx
from pyvis.network import Network
import janitor
from IPython.display import display, HTML

connections_data = pd.read_csv("Connections.csv", skiprows=2)
formatted_connections_data = (
    connections_data.clean_names()
    .drop(columns=["email_address"])
    .dropna(subset=["company", "position"])
)
formatted_connections_data["connected_on"] = pd.to_datetime(
    formatted_connections_data["connected_on"], format="%d %b %Y"
)

recommendations_data = pd.read_csv("Recommendations_Received.csv")
recommendations_data = recommendations_data.clean_names().dropna(
    subset=["first_name", "text", "creation_date", "status"]
)

messages_data = pd.read_csv('Messages.csv')
messages_data = messages_data.clean_names()
message_senders = messages_data['from'].dropna().unique()

nt = Network(notebook=True)
g = nx.Graph()

default_icon = {"face": "FontAwesome", "code": "\uf0c0", "size": 50, "color": "blue"}

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
        # color="blue",
        title=f"{company} ({company_count} connections)",
        shape="circularImage",
        image=logo_url,
    )
    g.add_edge("You", company, color="lightgray")

    persons = formatted_connections_data[formatted_connections_data["company"] == company]
    for _, person in persons.iterrows():
        person_name = f"{person['first_name']} {person['last_name']}".strip()
        position = person["position"]
        title = f"{person_name} - {position}"
        color = "red" if person_name in message_senders else "lightblue"
        g.add_node(person_name, size=5, color=color, title=title)
        g.add_edge(company, person_name, color="lightgray")

for idx, rec in recommendations_data.iterrows():
    person_name = f"{rec['first_name']} {rec.get('last_name', '').strip()}".strip()
    rec_label = f"{rec.get('job_title', 'Recommendation')}"
    rec_text = rec["text"]
    rec_url = rec.get("url", "")

    rec_node_id = f"{person_name}_rec_{idx}"
    title_html = (
        f"<a href='{rec_url}' target='_blank'>{rec_label}</a><br>{rec_text}"
        if rec_url
        else f"{rec_label}<br>{rec_text}"
    )

    g.add_node(
        rec_node_id,
        label=rec_label,
        title=title_html,
        size=8,
        color="lightgreen",
        shape="box",
    )
    if g.has_node(person_name):
        g.add_edge(person_name, rec_node_id, color="lightgray")

nt.from_nx(g)
nt.show("nodes.html")
display(HTML("nodes.html"))
