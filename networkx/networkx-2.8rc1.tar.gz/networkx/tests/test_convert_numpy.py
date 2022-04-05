import pytest

np = pytest.importorskip("numpy")
npt = pytest.importorskip("numpy.testing")

import networkx as nx
from networkx.generators.classic import barbell_graph, cycle_graph, path_graph
from networkx.utils import graphs_equal


def test_to_numpy_matrix_deprecation():
    pytest.deprecated_call(nx.to_numpy_matrix, nx.Graph())


def test_from_numpy_matrix_deprecation():
    pytest.deprecated_call(nx.from_numpy_matrix, np.eye(2))


def test_to_numpy_recarray_deprecation():
    pytest.deprecated_call(nx.to_numpy_recarray, nx.Graph())


class TestConvertNumpyMatrix:
    # TODO: This entire class can be removed when to/from_numpy_matrix
    # deprecation expires
    def setup_method(self):
        self.G1 = barbell_graph(10, 3)
        self.G2 = cycle_graph(10, create_using=nx.DiGraph)

        self.G3 = self.create_weighted(nx.Graph())
        self.G4 = self.create_weighted(nx.DiGraph())

    def test_exceptions(self):
        G = np.array("a")
        pytest.raises(nx.NetworkXError, nx.to_networkx_graph, G)

    def create_weighted(self, G):
        g = cycle_graph(4)
        G.add_nodes_from(g)
        G.add_weighted_edges_from((u, v, 10 + u) for u, v in g.edges())
        return G

    def assert_equal(self, G1, G2):
        assert sorted(G1.nodes()) == sorted(G2.nodes())
        assert sorted(G1.edges()) == sorted(G2.edges())

    def identity_conversion(self, G, A, create_using):
        assert A.sum() > 0
        GG = nx.from_numpy_matrix(A, create_using=create_using)
        self.assert_equal(G, GG)
        GW = nx.to_networkx_graph(A, create_using=create_using)
        self.assert_equal(G, GW)
        GI = nx.empty_graph(0, create_using).__class__(A)
        self.assert_equal(G, GI)

    def test_shape(self):
        "Conversion from non-square array."
        A = np.array([[1, 2, 3], [4, 5, 6]])
        pytest.raises(nx.NetworkXError, nx.from_numpy_matrix, A)

    def test_identity_graph_matrix(self):
        "Conversion from graph to matrix to graph."
        A = nx.to_numpy_matrix(self.G1)
        self.identity_conversion(self.G1, A, nx.Graph())

    def test_identity_graph_array(self):
        "Conversion from graph to array to graph."
        A = nx.to_numpy_matrix(self.G1)
        A = np.asarray(A)
        self.identity_conversion(self.G1, A, nx.Graph())

    def test_identity_digraph_matrix(self):
        """Conversion from digraph to matrix to digraph."""
        A = nx.to_numpy_matrix(self.G2)
        self.identity_conversion(self.G2, A, nx.DiGraph())

    def test_identity_digraph_array(self):
        """Conversion from digraph to array to digraph."""
        A = nx.to_numpy_matrix(self.G2)
        A = np.asarray(A)
        self.identity_conversion(self.G2, A, nx.DiGraph())

    def test_identity_weighted_graph_matrix(self):
        """Conversion from weighted graph to matrix to weighted graph."""
        A = nx.to_numpy_matrix(self.G3)
        self.identity_conversion(self.G3, A, nx.Graph())

    def test_identity_weighted_graph_array(self):
        """Conversion from weighted graph to array to weighted graph."""
        A = nx.to_numpy_matrix(self.G3)
        A = np.asarray(A)
        self.identity_conversion(self.G3, A, nx.Graph())

    def test_identity_weighted_digraph_matrix(self):
        """Conversion from weighted digraph to matrix to weighted digraph."""
        A = nx.to_numpy_matrix(self.G4)
        self.identity_conversion(self.G4, A, nx.DiGraph())

    def test_identity_weighted_digraph_array(self):
        """Conversion from weighted digraph to array to weighted digraph."""
        A = nx.to_numpy_matrix(self.G4)
        A = np.asarray(A)
        self.identity_conversion(self.G4, A, nx.DiGraph())

    def test_nodelist(self):
        """Conversion from graph to matrix to graph with nodelist."""
        P4 = path_graph(4)
        P3 = path_graph(3)
        nodelist = list(P3)
        A = nx.to_numpy_matrix(P4, nodelist=nodelist)
        GA = nx.Graph(A)
        self.assert_equal(GA, P3)

        assert nx.to_numpy_matrix(P3, nodelist=[]).shape == (0, 0)
        # Test nodelist duplicates.
        long_nodelist = nodelist + [0]
        pytest.raises(nx.NetworkXError, nx.to_numpy_matrix, P3, nodelist=long_nodelist)

        # Test nodelist contains non-nodes
        nonnodelist = [-1, 0, 1, 2]
        pytest.raises(nx.NetworkXError, nx.to_numpy_matrix, P3, nodelist=nonnodelist)

    def test_weight_keyword(self):
        WP4 = nx.Graph()
        WP4.add_edges_from((n, n + 1, dict(weight=0.5, other=0.3)) for n in range(3))
        P4 = path_graph(4)
        A = nx.to_numpy_matrix(P4)
        np.testing.assert_equal(A, nx.to_numpy_matrix(WP4, weight=None))
        np.testing.assert_equal(0.5 * A, nx.to_numpy_matrix(WP4))
        np.testing.assert_equal(0.3 * A, nx.to_numpy_matrix(WP4, weight="other"))

    def test_from_numpy_matrix_type(self):
        pytest.importorskip("scipy")

        A = np.matrix([[1]])
        G = nx.from_numpy_matrix(A)
        assert type(G[0][0]["weight"]) == int

        A = np.matrix([[1]]).astype(float)
        G = nx.from_numpy_matrix(A)
        assert type(G[0][0]["weight"]) == float

        A = np.matrix([[1]]).astype(str)
        G = nx.from_numpy_matrix(A)
        assert type(G[0][0]["weight"]) == str

        A = np.matrix([[1]]).astype(bool)
        G = nx.from_numpy_matrix(A)
        assert type(G[0][0]["weight"]) == bool

        A = np.matrix([[1]]).astype(complex)
        G = nx.from_numpy_matrix(A)
        assert type(G[0][0]["weight"]) == complex

        A = np.matrix([[1]]).astype(object)
        pytest.raises(TypeError, nx.from_numpy_matrix, A)

        G = nx.cycle_graph(3)
        A = nx.adjacency_matrix(G).todense()
        H = nx.from_numpy_matrix(A)
        assert all(type(m) == int and type(n) == int for m, n in H.edges())
        H = nx.from_numpy_array(A)
        assert all(type(m) == int and type(n) == int for m, n in H.edges())

    def test_from_numpy_matrix_dtype(self):
        dt = [("weight", float), ("cost", int)]
        A = np.matrix([[(1.0, 2)]], dtype=dt)
        G = nx.from_numpy_matrix(A)
        assert type(G[0][0]["weight"]) == float
        assert type(G[0][0]["cost"]) == int
        assert G[0][0]["cost"] == 2
        assert G[0][0]["weight"] == 1.0

    def test_to_numpy_recarray(self):
        G = nx.Graph()
        G.add_edge(1, 2, weight=7.0, cost=5)
        A = nx.to_numpy_recarray(G, dtype=[("weight", float), ("cost", int)])
        assert sorted(A.dtype.names) == ["cost", "weight"]
        assert A.weight[0, 1] == 7.0
        assert A.weight[0, 0] == 0.0
        assert A.cost[0, 1] == 5
        assert A.cost[0, 0] == 0

    def test_numpy_multigraph(self):
        G = nx.MultiGraph()
        G.add_edge(1, 2, weight=7)
        G.add_edge(1, 2, weight=70)
        A = nx.to_numpy_matrix(G)
        assert A[1, 0] == 77
        A = nx.to_numpy_matrix(G, multigraph_weight=min)
        assert A[1, 0] == 7
        A = nx.to_numpy_matrix(G, multigraph_weight=max)
        assert A[1, 0] == 70

    def test_from_numpy_matrix_parallel_edges(self):
        """Tests that the :func:`networkx.from_numpy_matrix` function
        interprets integer weights as the number of parallel edges when
        creating a multigraph.

        """
        A = np.matrix([[1, 1], [1, 2]])
        # First, with a simple graph, each integer entry in the adjacency
        # matrix is interpreted as the weight of a single edge in the graph.
        expected = nx.DiGraph()
        edges = [(0, 0), (0, 1), (1, 0)]
        expected.add_weighted_edges_from([(u, v, 1) for (u, v) in edges])
        expected.add_edge(1, 1, weight=2)
        actual = nx.from_numpy_matrix(A, parallel_edges=True, create_using=nx.DiGraph)
        assert graphs_equal(actual, expected)
        actual = nx.from_numpy_matrix(A, parallel_edges=False, create_using=nx.DiGraph)
        assert graphs_equal(actual, expected)
        # Now each integer entry in the adjacency matrix is interpreted as the
        # number of parallel edges in the graph if the appropriate keyword
        # argument is specified.
        edges = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 1)]
        expected = nx.MultiDiGraph()
        expected.add_weighted_edges_from([(u, v, 1) for (u, v) in edges])
        actual = nx.from_numpy_matrix(
            A, parallel_edges=True, create_using=nx.MultiDiGraph
        )
        assert graphs_equal(actual, expected)
        expected = nx.MultiDiGraph()
        expected.add_edges_from(set(edges), weight=1)
        # The sole self-loop (edge 0) on vertex 1 should have weight 2.
        expected[1][1][0]["weight"] = 2
        actual = nx.from_numpy_matrix(
            A, parallel_edges=False, create_using=nx.MultiDiGraph
        )
        assert graphs_equal(actual, expected)

    def test_symmetric(self):
        """Tests that a symmetric matrix has edges added only once to an
        undirected multigraph when using :func:`networkx.from_numpy_matrix`.

        """
        A = np.matrix([[0, 1], [1, 0]])
        G = nx.from_numpy_matrix(A, create_using=nx.MultiGraph)
        expected = nx.MultiGraph()
        expected.add_edge(0, 1, weight=1)
        assert graphs_equal(G, expected)

    def test_dtype_int_graph(self):
        """Test that setting dtype int actually gives an integer matrix.

        For more information, see GitHub pull request #1363.

        """
        G = nx.complete_graph(3)
        A = nx.to_numpy_matrix(G, dtype=int)
        assert A.dtype == int

    def test_dtype_int_multigraph(self):
        """Test that setting dtype int actually gives an integer matrix.

        For more information, see GitHub pull request #1363.

        """
        G = nx.MultiGraph(nx.complete_graph(3))
        A = nx.to_numpy_matrix(G, dtype=int)
        assert A.dtype == int


class TestConvertNumpyArray:
    def setup_method(self):
        self.G1 = barbell_graph(10, 3)
        self.G2 = cycle_graph(10, create_using=nx.DiGraph)
        self.G3 = self.create_weighted(nx.Graph())
        self.G4 = self.create_weighted(nx.DiGraph())

    def create_weighted(self, G):
        g = cycle_graph(4)
        G.add_nodes_from(g)
        G.add_weighted_edges_from((u, v, 10 + u) for u, v in g.edges())
        return G

    def assert_equal(self, G1, G2):
        assert sorted(G1.nodes()) == sorted(G2.nodes())
        assert sorted(G1.edges()) == sorted(G2.edges())

    def identity_conversion(self, G, A, create_using):
        assert A.sum() > 0
        GG = nx.from_numpy_array(A, create_using=create_using)
        self.assert_equal(G, GG)
        GW = nx.to_networkx_graph(A, create_using=create_using)
        self.assert_equal(G, GW)
        GI = nx.empty_graph(0, create_using).__class__(A)
        self.assert_equal(G, GI)

    def test_shape(self):
        "Conversion from non-square array."
        A = np.array([[1, 2, 3], [4, 5, 6]])
        pytest.raises(nx.NetworkXError, nx.from_numpy_array, A)

    def test_identity_graph_array(self):
        "Conversion from graph to array to graph."
        A = nx.to_numpy_array(self.G1)
        self.identity_conversion(self.G1, A, nx.Graph())

    def test_identity_digraph_array(self):
        """Conversion from digraph to array to digraph."""
        A = nx.to_numpy_array(self.G2)
        self.identity_conversion(self.G2, A, nx.DiGraph())

    def test_identity_weighted_graph_array(self):
        """Conversion from weighted graph to array to weighted graph."""
        A = nx.to_numpy_array(self.G3)
        self.identity_conversion(self.G3, A, nx.Graph())

    def test_identity_weighted_digraph_array(self):
        """Conversion from weighted digraph to array to weighted digraph."""
        A = nx.to_numpy_array(self.G4)
        self.identity_conversion(self.G4, A, nx.DiGraph())

    def test_nodelist(self):
        """Conversion from graph to array to graph with nodelist."""
        P4 = path_graph(4)
        P3 = path_graph(3)
        nodelist = list(P3)
        A = nx.to_numpy_array(P4, nodelist=nodelist)
        GA = nx.Graph(A)
        self.assert_equal(GA, P3)

        # Make nodelist ambiguous by containing duplicates.
        nodelist += [nodelist[0]]
        pytest.raises(nx.NetworkXError, nx.to_numpy_array, P3, nodelist=nodelist)

    def test_weight_keyword(self):
        WP4 = nx.Graph()
        WP4.add_edges_from((n, n + 1, dict(weight=0.5, other=0.3)) for n in range(3))
        P4 = path_graph(4)
        A = nx.to_numpy_array(P4)
        np.testing.assert_equal(A, nx.to_numpy_array(WP4, weight=None))
        np.testing.assert_equal(0.5 * A, nx.to_numpy_array(WP4))
        np.testing.assert_equal(0.3 * A, nx.to_numpy_array(WP4, weight="other"))

    def test_from_numpy_array_type(self):
        A = np.array([[1]])
        G = nx.from_numpy_array(A)
        assert type(G[0][0]["weight"]) == int

        A = np.array([[1]]).astype(float)
        G = nx.from_numpy_array(A)
        assert type(G[0][0]["weight"]) == float

        A = np.array([[1]]).astype(str)
        G = nx.from_numpy_array(A)
        assert type(G[0][0]["weight"]) == str

        A = np.array([[1]]).astype(bool)
        G = nx.from_numpy_array(A)
        assert type(G[0][0]["weight"]) == bool

        A = np.array([[1]]).astype(complex)
        G = nx.from_numpy_array(A)
        assert type(G[0][0]["weight"]) == complex

        A = np.array([[1]]).astype(object)
        pytest.raises(TypeError, nx.from_numpy_array, A)

    def test_from_numpy_array_dtype(self):
        dt = [("weight", float), ("cost", int)]
        A = np.array([[(1.0, 2)]], dtype=dt)
        G = nx.from_numpy_array(A)
        assert type(G[0][0]["weight"]) == float
        assert type(G[0][0]["cost"]) == int
        assert G[0][0]["cost"] == 2
        assert G[0][0]["weight"] == 1.0

    def test_from_numpy_array_parallel_edges(self):
        """Tests that the :func:`networkx.from_numpy_array` function
        interprets integer weights as the number of parallel edges when
        creating a multigraph.

        """
        A = np.array([[1, 1], [1, 2]])
        # First, with a simple graph, each integer entry in the adjacency
        # matrix is interpreted as the weight of a single edge in the graph.
        expected = nx.DiGraph()
        edges = [(0, 0), (0, 1), (1, 0)]
        expected.add_weighted_edges_from([(u, v, 1) for (u, v) in edges])
        expected.add_edge(1, 1, weight=2)
        actual = nx.from_numpy_array(A, parallel_edges=True, create_using=nx.DiGraph)
        assert graphs_equal(actual, expected)
        actual = nx.from_numpy_array(A, parallel_edges=False, create_using=nx.DiGraph)
        assert graphs_equal(actual, expected)
        # Now each integer entry in the adjacency matrix is interpreted as the
        # number of parallel edges in the graph if the appropriate keyword
        # argument is specified.
        edges = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 1)]
        expected = nx.MultiDiGraph()
        expected.add_weighted_edges_from([(u, v, 1) for (u, v) in edges])
        actual = nx.from_numpy_array(
            A, parallel_edges=True, create_using=nx.MultiDiGraph
        )
        assert graphs_equal(actual, expected)
        expected = nx.MultiDiGraph()
        expected.add_edges_from(set(edges), weight=1)
        # The sole self-loop (edge 0) on vertex 1 should have weight 2.
        expected[1][1][0]["weight"] = 2
        actual = nx.from_numpy_array(
            A, parallel_edges=False, create_using=nx.MultiDiGraph
        )
        assert graphs_equal(actual, expected)

    def test_symmetric(self):
        """Tests that a symmetric array has edges added only once to an
        undirected multigraph when using :func:`networkx.from_numpy_array`.

        """
        A = np.array([[0, 1], [1, 0]])
        G = nx.from_numpy_array(A, create_using=nx.MultiGraph)
        expected = nx.MultiGraph()
        expected.add_edge(0, 1, weight=1)
        assert graphs_equal(G, expected)

    def test_dtype_int_graph(self):
        """Test that setting dtype int actually gives an integer array.

        For more information, see GitHub pull request #1363.

        """
        G = nx.complete_graph(3)
        A = nx.to_numpy_array(G, dtype=int)
        assert A.dtype == int

    def test_dtype_int_multigraph(self):
        """Test that setting dtype int actually gives an integer array.

        For more information, see GitHub pull request #1363.

        """
        G = nx.MultiGraph(nx.complete_graph(3))
        A = nx.to_numpy_array(G, dtype=int)
        assert A.dtype == int


@pytest.fixture
def recarray_test_graph():
    G = nx.Graph()
    G.add_edge(1, 2, weight=7.0, cost=5)
    return G


def test_to_numpy_recarray(recarray_test_graph):
    A = nx.to_numpy_recarray(
        recarray_test_graph, dtype=[("weight", float), ("cost", int)]
    )
    assert sorted(A.dtype.names) == ["cost", "weight"]
    assert A.weight[0, 1] == 7.0
    assert A.weight[0, 0] == 0.0
    assert A.cost[0, 1] == 5
    assert A.cost[0, 0] == 0
    with pytest.raises(AttributeError, match="has no attribute"):
        A.color[0, 1]


def test_to_numpy_recarray_default_dtype(recarray_test_graph):
    A = nx.to_numpy_recarray(recarray_test_graph)
    assert A.dtype.names == ("weight",)
    assert A.weight[0, 0] == 0
    assert A.weight[0, 1] == 7
    with pytest.raises(AttributeError, match="has no attribute"):
        A.cost[0, 1]


def test_to_numpy_recarray_directed(recarray_test_graph):
    G = recarray_test_graph.to_directed()
    G.remove_edge(2, 1)
    A = nx.to_numpy_recarray(G, dtype=[("weight", float), ("cost", int)])
    np.testing.assert_array_equal(A.weight, np.array([[0, 7.0], [0, 0]]))
    np.testing.assert_array_equal(A.cost, np.array([[0, 5], [0, 0]]))


def test_to_numpy_recarray_default_dtype_no_weight():
    G = nx.Graph()
    G.add_edge(0, 1, color="red")
    with pytest.raises(KeyError):
        A = nx.to_numpy_recarray(G)
    A = nx.to_numpy_recarray(G, dtype=[("color", "U8")])
    assert A.color[0, 1] == "red"


@pytest.fixture
def recarray_nodelist_test_graph():
    G = nx.Graph()
    G.add_edges_from(
        [(0, 1, {"weight": 1.0}), (0, 2, {"weight": 2.0}), (1, 2, {"weight": 0.5})]
    )
    return G


def test_to_numpy_recarray_nodelist(recarray_nodelist_test_graph):
    A = nx.to_numpy_recarray(recarray_nodelist_test_graph, nodelist=[0, 1])
    np.testing.assert_array_equal(A.weight, np.array([[0, 1], [1, 0]]))


@pytest.mark.parametrize(
    ("nodelist", "errmsg"),
    (([2, 3], "in nodelist is not in G"), ([1, 1], "nodelist contains duplicates")),
)
def test_to_numpy_recarray_bad_nodelist(recarray_nodelist_test_graph, nodelist, errmsg):
    with pytest.raises(nx.NetworkXError, match=errmsg):
        A = nx.to_numpy_recarray(recarray_nodelist_test_graph, nodelist=nodelist)


@pytest.fixture
def multigraph_test_graph():
    G = nx.MultiGraph()
    G.add_edge(1, 2, weight=7)
    G.add_edge(1, 2, weight=70)
    return G


@pytest.mark.parametrize(("operator", "expected"), ((sum, 77), (min, 7), (max, 70)))
def test_numpy_multigraph(multigraph_test_graph, operator, expected):
    A = nx.to_numpy_array(multigraph_test_graph, multigraph_weight=operator)
    assert A[1, 0] == expected


def test_to_numpy_array_multigraph_nodelist(multigraph_test_graph):
    G = multigraph_test_graph
    G.add_edge(0, 1, weight=3)
    A = nx.to_numpy_array(G, nodelist=[1, 2])
    assert A.shape == (2, 2)
    assert A[1, 0] == 77


@pytest.mark.parametrize(
    "G, expected",
    [
        (nx.Graph(), np.array([[0, 1 + 2j], [1 + 2j, 0]], dtype=complex)),
        (nx.DiGraph(), np.array([[0, 1 + 2j], [0, 0]], dtype=complex)),
    ],
)
def test_to_numpy_array_complex_weights(G, expected):
    G.add_edge(0, 1, weight=1 + 2j)
    A = nx.to_numpy_array(G, dtype=complex)
    npt.assert_array_equal(A, expected)


def test_to_numpy_array_arbitrary_weights():
    G = nx.DiGraph()
    w = 922337203685477580102  # Out of range for int64
    G.add_edge(0, 1, weight=922337203685477580102)  # val not representable by int64
    A = nx.to_numpy_array(G, dtype=object)
    expected = np.array([[0, w], [0, 0]], dtype=object)
    npt.assert_array_equal(A, expected)

    # Undirected
    A = nx.to_numpy_array(G.to_undirected(), dtype=object)
    expected = np.array([[0, w], [w, 0]], dtype=object)
    npt.assert_array_equal(A, expected)


@pytest.mark.parametrize(
    "func, expected",
    ((min, -1), (max, 10), (sum, 11), (np.mean, 11 / 3), (np.median, 2)),
)
def test_to_numpy_array_multiweight_reduction(func, expected):
    """Test various functions for reducing multiedge weights."""
    G = nx.MultiDiGraph()
    weights = [-1, 2, 10.0]
    for w in weights:
        G.add_edge(0, 1, weight=w)
    A = nx.to_numpy_array(G, multigraph_weight=func, dtype=float)
    assert np.allclose(A, [[0, expected], [0, 0]])

    # Undirected case
    A = nx.to_numpy_array(G.to_undirected(), multigraph_weight=func, dtype=float)
    assert np.allclose(A, [[0, expected], [expected, 0]])


@pytest.mark.parametrize(
    ("G, expected"),
    [
        (nx.Graph(), [[(0, 0), (10, 5)], [(10, 5), (0, 0)]]),
        (nx.DiGraph(), [[(0, 0), (10, 5)], [(0, 0), (0, 0)]]),
    ],
)
def test_to_numpy_array_structured_dtype_attrs_from_fields(G, expected):
    """When `dtype` is structured (i.e. has names) and `weight` is None, use
    the named fields of the dtype to look up edge attributes."""
    G.add_edge(0, 1, weight=10, cost=5.0)
    dtype = np.dtype([("weight", int), ("cost", int)])
    A = nx.to_numpy_array(G, dtype=dtype, weight=None)
    expected = np.asarray(expected, dtype=dtype)
    npt.assert_array_equal(A, expected)


def test_to_numpy_array_structured_dtype_single_attr_default():
    G = nx.path_graph(3)
    dtype = np.dtype([("weight", float)])  # A single named field
    A = nx.to_numpy_array(G, dtype=dtype, weight=None)
    expected = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
    npt.assert_array_equal(A["weight"], expected)


@pytest.mark.parametrize(
    ("field_name", "expected_attr_val"),
    [
        ("weight", 1),
        ("cost", 3),
    ],
)
def test_to_numpy_array_structured_dtype_single_attr(field_name, expected_attr_val):
    G = nx.Graph()
    G.add_edge(0, 1, cost=3)
    dtype = np.dtype([(field_name, float)])
    A = nx.to_numpy_array(G, dtype=dtype, weight=None)
    expected = np.array([[0, expected_attr_val], [expected_attr_val, 0]], dtype=float)
    npt.assert_array_equal(A[field_name], expected)


@pytest.mark.parametrize("graph_type", (nx.Graph, nx.DiGraph))
@pytest.mark.parametrize(
    "edge",
    [
        (0, 1),  # No edge attributes
        (0, 1, {"weight": 10}),  # One edge attr
        (0, 1, {"weight": 5, "flow": -4}),  # Multiple but not all edge attrs
        (0, 1, {"weight": 2.0, "cost": 10, "flow": -45}),  # All attrs
    ],
)
def test_to_numpy_array_structured_dtype_multiple_fields(graph_type, edge):
    G = graph_type([edge])
    dtype = np.dtype([("weight", float), ("cost", float), ("flow", float)])
    A = nx.to_numpy_array(G, dtype=dtype, weight=None)
    for attr in dtype.names:
        expected = nx.to_numpy_array(G, dtype=float, weight=attr)
        npt.assert_array_equal(A[attr], expected)


@pytest.mark.parametrize("G", (nx.Graph(), nx.DiGraph()))
def test_to_numpy_array_structured_dtype_scalar_nonedge(G):
    G.add_edge(0, 1, weight=10)
    dtype = np.dtype([("weight", float), ("cost", float)])
    A = nx.to_numpy_array(G, dtype=dtype, weight=None, nonedge=np.nan)
    for attr in dtype.names:
        expected = nx.to_numpy_array(G, dtype=float, weight=attr, nonedge=np.nan)
        npt.assert_array_equal(A[attr], expected)


@pytest.mark.parametrize("G", (nx.Graph(), nx.DiGraph()))
def test_to_numpy_array_structured_dtype_nonedge_ary(G):
    """Similar to the scalar case, except has a different non-edge value for
    each named field."""
    G.add_edge(0, 1, weight=10)
    dtype = np.dtype([("weight", float), ("cost", float)])
    nonedges = np.array([(0, np.inf)], dtype=dtype)
    A = nx.to_numpy_array(G, dtype=dtype, weight=None, nonedge=nonedges)
    for attr in dtype.names:
        nonedge = nonedges[attr]
        expected = nx.to_numpy_array(G, dtype=float, weight=attr, nonedge=nonedge)
        npt.assert_array_equal(A[attr], expected)


def test_to_numpy_array_structured_dtype_with_weight_raises():
    """Using both a structured dtype (with named fields) and specifying a `weight`
    parameter is ambiguous."""
    G = nx.path_graph(3)
    dtype = np.dtype([("weight", int), ("cost", int)])
    exception_msg = "Specifying `weight` not supported for structured dtypes"
    with pytest.raises(ValueError, match=exception_msg):
        nx.to_numpy_array(G, dtype=dtype)  # Default is weight="weight"
    with pytest.raises(ValueError, match=exception_msg):
        nx.to_numpy_array(G, dtype=dtype, weight="cost")


@pytest.mark.parametrize("graph_type", (nx.MultiGraph, nx.MultiDiGraph))
def test_to_numpy_array_structured_multigraph_raises(graph_type):
    G = nx.path_graph(3, create_using=graph_type)
    dtype = np.dtype([("weight", int), ("cost", int)])
    with pytest.raises(nx.NetworkXError, match="Structured arrays are not supported"):
        nx.to_numpy_array(G, dtype=dtype, weight=None)
