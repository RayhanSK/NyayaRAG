from Assault_KG import get_assault_triplets
from Attempt_to_murder_KG import get_attempt_to_murder_triplets
from Culpable_Homicide_KG import get_culpable_homicide_triplets
from Criminal_Conspiracy_KG import get_criminal_conspiracy_triplets
from Kidnapping_Abduction_KG import get_kidnapping_abduction_triplets
from Murder_KG import get_murder_triplets
from Defamation_KG import get_defamation_triplets

import networkx as nx

# 1. Combine all triplets
def get_all_law_triplets():
    return (
        get_assault_triplets() +
        get_attempt_to_murder_triplets() +
        get_culpable_homicide_triplets() +
        get_criminal_conspiracy_triplets() +
        get_kidnapping_abduction_triplets() +
        get_murder_triplets() +
        get_defamation_triplets()
    )

def build_law_kg(triplets):
    G = nx.DiGraph()
    for subj, pred, obj in triplets:
        G.add_edge(subj, obj, relation=pred)
    return G

def query_section_properties(G, section):
    return [
        (section, G[section][target]['relation'], target)
        for target in G.successors(section)
    ]

def query_by_relation(G, relation):
    return [
        (src, data['relation'], tgt)
        for src, tgt, data in G.edges(data=True)
        if data['relation'] == relation
    ]

def keyword_query(G, keyword):
    matches = []
    keyword_lower = keyword.lower()
    for src, tgt, data in G.edges(data=True):
        if keyword_lower in str(src).lower() or keyword_lower in str(tgt).lower() or keyword_lower in str(data['relation']).lower():
            matches.append((src, data['relation'], tgt))
    return matches

