def meu_dijkstra(G, source):
    seen = set()
    nextlevel= {source}
    nivel=0
    distancias={}
    while nextlevel:
        thislevel = nextlevel
        nextlevel = set()
        for v in thislevel:
            distancias[v] = nivel
            if v not in seen:
                seen.add(v)
                nextlevel.update(G[v])
        nivel+=1
return distancias
