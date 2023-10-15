class Graph:
    def __init__(self, edges):
        self.edges = edges 
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end] #append as list
        # print(self.graph_dict) 
    
    def get_paths(self, start, end):
        #recursion 

if __name__ == '__main__':
    #flight routes, convert to dictionary form 
    routes = [
        ("mumbai", "paris"),
        ("mumbai", "dubai"),
        ("paris", "dubai"),
        ("paris", "new york"),
        ("dubai", "new york"),
        ("new york", "toronto"),
    ]
    
    route_graph = Graph(routes)