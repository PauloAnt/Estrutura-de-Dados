def dfsPilha(num):
    graph = {0: (1, 2), 1: (3,), 2 : (4,), 3:(5,), 4: (6,), 5: (7, 8), 6: (), 7: (), 8: ()}
    visited = [False] * len(graph)
    pilha = []
    ordem = []
    pilha.append(num)
    while pilha:
        ultimo = pilha[-1]
        ordem.append(ultimo)
        adj = graph[ultimo]
        visited[ultimo] = True
        pilha.pop()
        for i in range(len(adj)):
            if (visited[adj[i]] == False):
                pilha.append(adj[i])
    return ordem

def bfsFila(num):
    graph = {0: (1, 2), 1: (3,), 2 : (5,), 3:(4, 6), 4: (), 5: (7,), 6: (), 7: ()}
    visited = [False] * len(graph)
    fila = []
    ordem = []
    fila.append(num)
    while fila:
        first = fila[0]
        ordem.append(first)
        adj = graph[first]
        visited[first] = True
        fila.pop(0)
        for i in range(len(adj)):
            if (visited[adj[i]] == False):
                fila.append(adj[i])
    return ordem

print(dfsPilha(0))
print(bfsFila(0))


        

