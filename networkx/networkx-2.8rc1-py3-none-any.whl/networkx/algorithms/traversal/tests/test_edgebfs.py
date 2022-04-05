import pytest

import networkx as nx
from networkx.algorithms.traversal.edgedfs import FORWARD, REVERSE


class TestEdgeBFS:
    @classmethod
    def setup_class(cls):
        cls.nodes = [0, 1, 2, 3]
        cls.edges = [(0, 1), (1, 0), (1, 0), (2, 0), (2, 1), (3, 1)]

    def test_empty(self):
        G = nx.Graph()
        edges = list(nx.edge_bfs(G))
        assert edges == []

    def test_graph_single_source(self):
        G = nx.Graph(self.edges)
        G.add_edge(4, 5)
        x = list(nx.edge_bfs(G, [0]))
        x_ = [(0, 1), (0, 2), (1, 2), (1, 3)]
        assert x == x_

    def test_graph(self):
        G = nx.Graph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes))
        x_ = [(0, 1), (0, 2), (1, 2), (1, 3)]
        assert x == x_

    def test_digraph(self):
        G = nx.DiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes))
        x_ = [(0, 1), (1, 0), (2, 0), (2, 1), (3, 1)]
        assert x == x_

    def test_digraph_orientation_invalid(self):
        G = nx.DiGraph(self.edges)
        edge_iterator = nx.edge_bfs(G, self.nodes, orientation="hello")
        pytest.raises(nx.NetworkXError, list, edge_iterator)

    def test_digraph_orientation_none(self):
        G = nx.DiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes, orientation=None))
        x_ = [(0, 1), (1, 0), (2, 0), (2, 1), (3, 1)]
        assert x == x_

    def test_digraph_orientation_original(self):
        G = nx.DiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes, orientation="original"))
        x_ = [
            (0, 1, FORWARD),
            (1, 0, FORWARD),
            (2, 0, FORWARD),
            (2, 1, FORWARD),
            (3, 1, FORWARD),
        ]
        assert x == x_

    def test_digraph2(self):
        G = nx.DiGraph()
        nx.add_path(G, range(4))
        x = list(nx.edge_bfs(G, [0]))
        x_ = [(0, 1), (1, 2), (2, 3)]
        assert x == x_

    def test_digraph_rev(self):
        G = nx.DiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes, orientation="reverse"))
        x_ = [
            (1, 0, REVERSE),
            (2, 0, REVERSE),
            (0, 1, REVERSE),
            (2, 1, REVERSE),
            (3, 1, REVERSE),
        ]
        assert x == x_

    def test_digraph_rev2(self):
        G = nx.DiGraph()
        nx.add_path(G, range(4))
        x = list(nx.edge_bfs(G, [3], orientation="reverse"))
        x_ = [(2, 3, REVERSE), (1, 2, REVERSE), (0, 1, REVERSE)]
        assert x == x_

    def test_multigraph(self):
        G = nx.MultiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes))
        x_ = [(0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (1, 2, 0), (1, 3, 0)]
        # This is an example of where hash randomization can break.
        # There are 3! * 2 alternative outputs, such as:
        #    [(0, 1, 1), (1, 0, 0), (0, 1, 2), (1, 3, 0), (1, 2, 0)]
        # But note, the edges (1,2,0) and (1,3,0) always follow the (0,1,k)
        # edges. So the algorithm only guarantees a partial order. A total
        # order is guaranteed only if the graph data structures are ordered.
        assert x == x_

    def test_multidigraph(self):
        G = nx.MultiDiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes))
        x_ = [(0, 1, 0), (1, 0, 0), (1, 0, 1), (2, 0, 0), (2, 1, 0), (3, 1, 0)]
        assert x == x_

    def test_multidigraph_rev(self):
        G = nx.MultiDiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes, orientation="reverse"))
        x_ = [
            (1, 0, 0, REVERSE),
            (1, 0, 1, REVERSE),
            (2, 0, 0, REVERSE),
            (0, 1, 0, REVERSE),
            (2, 1, 0, REVERSE),
            (3, 1, 0, REVERSE),
        ]
        assert x == x_

    def test_digraph_ignore(self):
        G = nx.DiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes, orientation="ignore"))
        x_ = [
            (0, 1, FORWARD),
            (1, 0, REVERSE),
            (2, 0, REVERSE),
            (2, 1, REVERSE),
            (3, 1, REVERSE),
        ]
        assert x == x_

    def test_digraph_ignore2(self):
        G = nx.DiGraph()
        nx.add_path(G, range(4))
        x = list(nx.edge_bfs(G, [0], orientation="ignore"))
        x_ = [(0, 1, FORWARD), (1, 2, FORWARD), (2, 3, FORWARD)]
        assert x == x_

    def test_multidigraph_ignore(self):
        G = nx.MultiDiGraph(self.edges)
        x = list(nx.edge_bfs(G, self.nodes, orientation="ignore"))
        x_ = [
            (0, 1, 0, FORWARD),
            (1, 0, 0, REVERSE),
            (1, 0, 1, REVERSE),
            (2, 0, 0, REVERSE),
            (2, 1, 0, REVERSE),
            (3, 1, 0, REVERSE),
        ]
        assert x == x_
