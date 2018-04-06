G = make_ring_lattice(1000, 10)

d = shortest_path_dijkstra(lattice, 0)
high=0
for k,v in d.items():
    if (v > high):
        high = v
        nodo = k
print ("nodo mais distante igual "+str(nodo)+" e esta a "+str(high)+" km ")
