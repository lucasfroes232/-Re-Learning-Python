class graph:
    # construtor
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, info):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(info)

    def BFS(self, Start_node, target):

        # Lista de nós já visitados, cada ind corresponde a um nó
        closed = []

        # Lista de nós abertos (a serem visitados)
        open_list = []

        # Adiciona nó para start
        open_list.append(Start_node)

        # While open != []
        while open_list:

            # Remove o estado mais a esquerda
            x = open_list.pop(0)

            if x == target:
                print("Caminho encontrado:\n")
                for _ in closed:
                    print(_)

            if x in closed:
                continue

            closed.append(x)

            # Adiciona filhos de X na fila de abertos
            
            if x in self.graph:
            	for i in self.graph[x]:
                	if i not in closed and i not in open_list:
                		#adiciona a esquerda(E o que diferencia do DFS)
                    		open_list.append(i)

if __name__ == '__main__':
    # Create a graph given in
    # the above diagram
    g = graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 7)
    g.addEdge(1, 9)
    g.addEdge(2, 5)
    g.addEdge(2, 6)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(0, 6)
