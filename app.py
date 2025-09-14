import pandas as pd
import networkx as nx
from pyvis.network import Network
import janitor
import matplotlib.pyplot as plt
from IPython.display import display, HTML
import requests # type: ignore

connections_data = pd.read_csv('Connections.csv', skiprows=2)
formatted_connections_data = (
    connections_data
    .clean_names()
    .drop(columns=['last_name', 'email_address'])
    .dropna(subset=['company', 'position'])
)
formatted_connections_data['connected_on'] = pd.to_datetime(formatted_connections_data['connected_on'], format='%d %b %Y')

nt = Network(notebook=True)
g = nx.Graph()

default_icon = {"face": "FontAwesome", "code": "\uf0c0", "size": 50, "color": "#3449eb"}

def test_logo_url(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=2)
        if r.status_code == 200 and r.headers.get('content-type', '').startswith('image'):
            return True
        else:
            return False
    except Exception as e:
        return False

companies = formatted_connections_data["company"].unique()
for company in companies:
    company_count = formatted_connections_data[formatted_connections_data["company"] == company].shape[0]
    clean_company = company.replace(" ", "").lower()
    logo_url = f'https://logo.clearbit.com/{clean_company}.com'
    has_logo = test_logo_url(logo_url)
    print(f"{company}: {logo_url} - {'OK' if has_logo else 'NOT FOUND'}")

    if has_logo:
        g.add_node(
            company,
            size=company_count * 5,
            color="#3449eb",
            title=f"{company} ({company_count} connections)",
            shape="image",
            image=logo_url
        )
    else:
        g.add_node(
            company,
            size=company_count * 5,
            color="#3449eb",
            title=f"{company} ({company_count} connections)"
        )
    g.add_edge("You", company, color="grey")
    
    persons = formatted_connections_data[formatted_connections_data["company"] == company]
    for _, person in persons.iterrows():
        person_name = person["first_name"]
        position = person["position"]
        title = f"{person_name} - {position}"
        g.add_node(person_name, size=10, color="#85c1b0", title=title)
        g.add_edge(company, person_name, color="lightblue")

nt.from_nx(g)
nt.show('nodes.html')
display(HTML('nodes.html'))
