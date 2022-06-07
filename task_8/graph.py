class Vertex:

    def __init__(self, val):
        self.Value = val

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        ind = self._find_index()

        if ind is not None:
            new_vertex = Vertex(v)
            self.vertex[ind] = new_vertex
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        self.vertex[v] = None

        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def _find_index(self):
        try:
            return self.vertex.index(None)
        except ValueError:
            return