
class graph:
	def __init__(self):
		self.graph = {}
	
	def addNode(self,node,info):
		if node not in self.graph:
			self.graph[node] = []
		self.graph[node].append(info)
		
	def DFS(self,start_node,target):
		#Lista de abertos
		open_list = []
		#Lista de fechados
		closed = []
		#Adiciona primeiro no na lista
		open_list.append(start_node)
		
		while open_list:
			x = open_list.pop()
			#Lista de vizinhos
			neighboors = []
			
			#Testa se x é o objetivo
			if x == target:
				print("Achou caminho\n")
				for _ in closed :
					print(_)
			#Testa se x esta no vetor de fechados
			if x in closed:
				continue
			#Gera filhos de x
			if x in self.graph:
					if self.graph[x] == []:
						continue
					for node in self.graph[x]:
						if node not in closed and node not in open_list:
							neighboors.append(node)
							
			for element in reversed(neighboors):
				open_list.append(element)
							
			#Adiciona na lista de fechados
			closed.append(x)				
if __name__ == "__main__":
# the above diagram
    g = graph()
    g.addNode(0, 1)
    g.addNode(0, 2)
    g.addNode(1, 7)
    g.addNode(1, 9)
    g.addNode(2, 5)
    g.addNode(2, 6)

    print("DFS:")
    g.DFS(0, 6)
						
