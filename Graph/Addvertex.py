class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        sort_graph = []
        for key in self.adj_list:
            sort_graph.append(key)
        sort_graph.sort()
        for vertex in sort_graph:
            print("vertex: ", vertex, " Edges: ", self.adj_list[vertex])


    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []
    B : []
"""