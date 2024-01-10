class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
            
    
    def add_vertex(self, vertex):
        if vertex in self.adj_list.keys() :
            return False
        
        self.adj_list[vertex] = []
        return True
    
    def add_edge(self, v1, v2):
        if v1 not in self.adj_list.keys() or v2 not in self.adj_list.keys() :
            return False
        
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
      
    
    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
          
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except:
            pass
        return True
    
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            return False
    
        for v in self.adj_list[vertex]:
            self.adj_list[v].remove(vertex)
        
        del self.adj_list[vertex]
        return True