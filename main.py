import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the JSON data
data = """
{
    "entities": [
        {
            "name": "John",
            "type": "Person",
            "role": "Software Engineer",
            "organization": "SpaceX"
        },
        {
            "name": "SpaceX",
            "type": "Organization"
        },
        {
            "name": "Mars Colonization Project",
            "type": "Project",
            "participants": ["John"]
        },
        {
            "name": "Sarah",
            "type": "Person",
            "role": "Biologist",
            "organization": "NASA"
        },
        {
            "name": "NASA",
            "type": "Organization"
        },
        {
            "name": "Research on potential life forms on Mars",
            "type": "Project",
            "participants": ["Sarah"]
        }
    ],
    "relationships": [
        {
            "source": "John",
            "target": "SpaceX",
            "relationship": "works at"
        },
        {
            "source": "John",
            "target": "Mars Colonization Project",
            "relationship": "works on"
        },
        {
            "source": "Sarah",
            "target": "NASA",
            "relationship": "works at"
        },
        {
            "source": "Sarah",
            "target": "Research on potential life forms on Mars",
            "relationship": "works on"
        },
        {
            "source": "John",
            "target": "Sarah",
            "relationship": "collaborates with"
        }
    ]
}
"""
data_dict = json.loads(data)

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for entity in data_dict['entities']:
    G.add_node(entity['name'])

# Add edges to the graph
for relationship in data_dict['relationships']:
    G.add_edge(relationship['source'], relationship['target'], label=relationship['relationship'])

# Draw the graph
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='seagreen', alpha=0.9,
        labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
plt.show()
