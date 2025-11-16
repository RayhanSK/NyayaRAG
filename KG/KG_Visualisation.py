import matplotlib.pyplot as plt
import networkx as nx
from all_law_KG import build_law_kg, get_all_law_triplets
from Defamation_KG import get_defamation_triplets
from Culpable_Homicide_KG import get_culpable_homicide_triplets
from Criminal_Conspiracy_KG import get_criminal_conspiracy_triplets
from Assault_KG import get_assault_triplets
from Murder_KG import get_murder_triplets
from Kidnapping_Abduction_KG import get_kidnapping_abduction_triplets
from Attempt_to_murder_KG import get_attempt_to_murder_triplets

def visualize_graph(G, title="Knowledge Graph", num_nodes=100):
    sub_G = G
    if len(G) > num_nodes:
        nodes = list(G.nodes())[:num_nodes]
        sub_G = G.subgraph(nodes)
    pos = nx.spring_layout(sub_G, k=0.6)
    plt.figure(figsize=(50, 40))
    nx.draw_networkx_nodes(sub_G, pos, node_size=100, node_color='skyblue')
    nx.draw_networkx_edges(sub_G, pos, arrows=True)
    nx.draw_networkx_labels(sub_G, pos, font_size=3)
    nx.draw_networkx_edge_labels(sub_G, pos, edge_labels={(u, v): d["relation"] for u, v, d in sub_G.edges(data=True)}, font_size=3)
    plt.title(title)
    plt.axis('off')
    plt.show()
if __name__ == "__main__":
    triplets = get_murder_triplets()
    G = build_law_kg(triplets)
    visualize_graph(G, title="Murder (Section 302) KG")

