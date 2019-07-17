# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:20:58 2019

@author: cookchr2
"""

import networkx as nx
from networkx.algorithms import community
import pandas as pd

data = pd.read_stata(r'R:\JoePriceResearch\RA_work_folders\Christopher_Cook\temp\network\undirected_all_cen.dta')[['name1','name2']]
G = nx.convert_matrix.from_pandas_edgelist (data,'name1','name2')

communities = community.greedy_modularity_communities(G)

