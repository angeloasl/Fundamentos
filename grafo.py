# Fundamentos

from __future__ import print_function, division

%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt

import networkx as nx
import numpy as np

# colors from our friends at http://colorbrewer2.org
COLORS = ['#43a2ca','#31a354','#de2d26','#fb8072','#8856a7','#fdb462',
          '#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5','#ffed6f']

pos = dict(LinhaAzul=(-120, 45),
          LinhaVerde=(-70, 60),
          LinhaVermelha=(-90, 40),
          LinhaAmarela=(-70, 20),
          LinhaRoxa=(-120,20))
pos['LinhaAzul']

G = nx.Graph()
G.add_nodes_from(pos)
G.nodes()

numero_conexoes = {('LinhaAzul', 'LinhaVerde'): 2,
               ('LinhaAzul', 'LinhaAmarela'): 1,
               ('LinhaAzul', 'LinhaVermelha'): 1,
               ('LinhaAzul', 'LinhaRoxa'): 1,
               ('LinhaVerde', 'LinhaVermelha'): 1,
               ('LinhaVerde', 'LinhaAmarela'): 1,
               ('LinhaVermelha', 'LinhaAmarela'): 1,
               ('LinhaRoxa', 'LinhaAmarela'): 1}

G.add_edges_from(numero_conexoes)
G.edges()

nx.draw(G, pos, 
        node_color=COLORS[0], 
        node_shape='s', 
        node_size=2500, 
        with_labels=True)

nx.draw_networkx_edge_labels(G, pos, 
                             edge_labels=numero_conexoes)

plt.axis('equal')
plt.savefig('chap02-2.pdf')




#Attempt 2

from __future__ import print_function, division

%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt

import networkx as nx
import numpy as np

# colors from our friends at http://colorbrewer2.org
COLORS = ['#43a2ca','#31a354','#de2d26','#fb8072','#8856a7','#fdb462',
          '#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5','#ffed6f']

pos = dict(LinhaAzul=(-120, 45),
          LinhaVerde=(-70, 60),
          LinhaVermelha=(-85, 40),
          LinhaAmarela=(-70, 20),
          LinhaRoxa=(-120,20))
pos['LinhaAzul']

G = nx.Graph()
G.add_nodes_from(pos)
G.nodes()

numero_conexoes = {('LinhaAzul', 'LinhaVerde'): 2,
               ('LinhaAzul', 'LinhaAmarela'): 1,
               ('LinhaAzul', 'LinhaVermelha'): 1,
               ('LinhaAzul', 'LinhaRoxa'): 1,
               ('LinhaVerde', 'LinhaVermelha'): 1,
               ('LinhaVerde', 'LinhaAmarela'): 1,
               ('LinhaVermelha', 'LinhaAmarela'): 1,
               ('LinhaRoxa', 'LinhaAmarela'): 1}

G.add_edges_from(numero_conexoes)
G.edges()

nx.draw(G, pos, 
        node_color=COLORS[0], 
        node_size=7000, 
        with_labels=True)

nx.draw_networkx_edge_labels(G, pos, 
                             edge_labels=numero_conexoes)

plt.axis('equal')
plt.savefig('chap02-2.pdf')



