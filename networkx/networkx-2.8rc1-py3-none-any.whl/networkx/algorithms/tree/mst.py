"""
Algorithms for calculating min/max spanning trees/forests.

"""
from dataclasses import dataclass, field
from enum import Enum
from heapq import heappop, heappush
from operator import itemgetter
from itertools import count
from math import isnan
from queue import PriorityQueue

import networkx as nx
from networkx.utils import UnionFind, not_implemented_for

__all__ = [
    "minimum_spanning_edges",
    "maximum_spanning_edges",
    "minimum_spanning_tree",
    "maximum_spanning_tree",
    "partition_spanning_tree",
    "EdgePartition",
    "SpanningTreeIterator",
]


class EdgePartition(Enum):
    """
    An enum to store the state of an edge partition. The enum is written to the
    edges of a graph before being pasted to `kruskal_mst_edges`. Options are:

    - EdgePartition.OPEN
    - EdgePartition.INCLUDED
    - EdgePartition.EXCLUDED
    """

    OPEN = 0
    INCLUDED = 1
    EXCLUDED = 2


@not_implemented_for("multigraph")
def boruvka_mst_edges(
    G, minimum=True, weight="weight", keys=False, data=True, ignore_nan=False
):
    """Iterate over edges of a Borůvka's algorithm min/max spanning tree.

    Parameters
    ----------
    G : NetworkX Graph
        The edges of `G` must have distinct weights,
        otherwise the edges may not form a tree.

    minimum : bool (default: True)
        Find the minimum (True) or maximum (False) spanning tree.

    weight : string (default: 'weight')
        The name of the edge attribute holding the edge weights.

    keys : bool (default: True)
        This argument is ignored since this function is not
        implemented for multigraphs; it exists only for consistency
        with the other minimum spanning tree functions.

    data : bool (default: True)
        Flag for whether to yield edge attribute dicts.
        If True, yield edges `(u, v, d)`, where `d` is the attribute dict.
        If False, yield edges `(u, v)`.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.

    """
    # Initialize a forest, assuming initially that it is the discrete
    # partition of the nodes of the graph.
    forest = UnionFind(G)

    def best_edge(component):
        """Returns the optimum (minimum or maximum) edge on the edge
        boundary of the given set of nodes.

        A return value of ``None`` indicates an empty boundary.

        """
        sign = 1 if minimum else -1
        minwt = float("inf")
        boundary = None
        for e in nx.edge_boundary(G, component, data=True):
            wt = e[-1].get(weight, 1) * sign
            if isnan(wt):
                if ignore_nan:
                    continue
                msg = f"NaN found as an edge weight. Edge {e}"
                raise ValueError(msg)
            if wt < minwt:
                minwt = wt
                boundary = e
        return boundary

    # Determine the optimum edge in the edge boundary of each component
    # in the forest.
    best_edges = (best_edge(component) for component in forest.to_sets())
    best_edges = [edge for edge in best_edges if edge is not None]
    # If each entry was ``None``, that means the graph was disconnected,
    # so we are done generating the forest.
    while best_edges:
        # Determine the optimum edge in the edge boundary of each
        # component in the forest.
        #
        # This must be a sequence, not an iterator. In this list, the
        # same edge may appear twice, in different orientations (but
        # that's okay, since a union operation will be called on the
        # endpoints the first time it is seen, but not the second time).
        #
        # Any ``None`` indicates that the edge boundary for that
        # component was empty, so that part of the forest has been
        # completed.
        #
        # TODO This can be parallelized, both in the outer loop over
        # each component in the forest and in the computation of the
        # minimum. (Same goes for the identical lines outside the loop.)
        best_edges = (best_edge(component) for component in forest.to_sets())
        best_edges = [edge for edge in best_edges if edge is not None]
        # Join trees in the forest using the best edges, and yield that
        # edge, since it is part of the spanning tree.
        #
        # TODO This loop can be parallelized, to an extent (the union
        # operation must be atomic).
        for u, v, d in best_edges:
            if forest[u] != forest[v]:
                if data:
                    yield u, v, d
                else:
                    yield u, v
                forest.union(u, v)


def kruskal_mst_edges(
    G, minimum, weight="weight", keys=True, data=True, ignore_nan=False, partition=None
):
    """
    Iterate over edge of a Kruskal's algorithm min/max spanning tree.

    Parameters
    ----------
    G : NetworkX Graph
        The graph holding the tree of interest.

    minimum : bool (default: True)
        Find the minimum (True) or maximum (False) spanning tree.

    weight : string (default: 'weight')
        The name of the edge attribute holding the edge weights.

    keys : bool (default: True)
        If `G` is a multigraph, `keys` controls whether edge keys ar yielded.
        Otherwise `keys` is ignored.

    data : bool (default: True)
        Flag for whether to yield edge attribute dicts.
        If True, yield edges `(u, v, d)`, where `d` is the attribute dict.
        If False, yield edges `(u, v)`.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.

    partition : string (default: None)
        The name of the edge attribute holding the partition data, if it exists.
        Partition data is written to the edges using the `EdgePartition` enum.
        If a partition exists, all included edges and none of the excluded edges
        will appear in the final tree. Open edges may or may not be used.

    Yields
    ------
    edge tuple
        The edges as discovered by Kruskal's method. Each edge can
        take the following forms: `(u, v)`, `(u, v, d)` or `(u, v, k, d)`
        depending on the `key` and `data` parameters
    """
    subtrees = UnionFind()
    if G.is_multigraph():
        edges = G.edges(keys=True, data=True)
    else:
        edges = G.edges(data=True)

    """
    Sort the edges of the graph with respect to the partition data. 
    Edges are returned in the following order:

    * Included edges
    * Open edges from smallest to largest weight
    * Excluded edges
    """
    included_edges = []
    open_edges = []
    for e in edges:
        d = e[-1]
        wt = d.get(weight, 1)
        if isnan(wt):
            if ignore_nan:
                continue
            raise ValueError(f"NaN found as an edge weight. Edge {e}")

        edge = (wt,) + e
        if d.get(partition) == EdgePartition.INCLUDED:
            included_edges.append(edge)
        elif d.get(partition) == EdgePartition.EXCLUDED:
            continue
        else:
            open_edges.append(edge)

    if minimum:
        sorted_open_edges = sorted(open_edges, key=itemgetter(0))
    else:
        sorted_open_edges = sorted(open_edges, key=itemgetter(0), reverse=True)

    # Condense the lists into one
    included_edges.extend(sorted_open_edges)
    sorted_edges = included_edges
    del open_edges, sorted_open_edges, included_edges

    # Multigraphs need to handle edge keys in addition to edge data.
    if G.is_multigraph():
        for wt, u, v, k, d in sorted_edges:
            if subtrees[u] != subtrees[v]:
                if keys:
                    if data:
                        yield u, v, k, d
                    else:
                        yield u, v, k
                else:
                    if data:
                        yield u, v, d
                    else:
                        yield u, v
                subtrees.union(u, v)
    else:
        for wt, u, v, d in sorted_edges:
            if subtrees[u] != subtrees[v]:
                if data:
                    yield u, v, d
                else:
                    yield u, v
                subtrees.union(u, v)


def prim_mst_edges(G, minimum, weight="weight", keys=True, data=True, ignore_nan=False):
    """Iterate over edges of Prim's algorithm min/max spanning tree.

    Parameters
    ----------
    G : NetworkX Graph
        The graph holding the tree of interest.

    minimum : bool (default: True)
        Find the minimum (True) or maximum (False) spanning tree.

    weight : string (default: 'weight')
        The name of the edge attribute holding the edge weights.

    keys : bool (default: True)
        If `G` is a multigraph, `keys` controls whether edge keys ar yielded.
        Otherwise `keys` is ignored.

    data : bool (default: True)
        Flag for whether to yield edge attribute dicts.
        If True, yield edges `(u, v, d)`, where `d` is the attribute dict.
        If False, yield edges `(u, v)`.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.

    """
    is_multigraph = G.is_multigraph()
    push = heappush
    pop = heappop

    nodes = set(G)
    c = count()

    sign = 1 if minimum else -1

    while nodes:
        u = nodes.pop()
        frontier = []
        visited = {u}
        if is_multigraph:
            for v, keydict in G.adj[u].items():
                for k, d in keydict.items():
                    wt = d.get(weight, 1) * sign
                    if isnan(wt):
                        if ignore_nan:
                            continue
                        msg = f"NaN found as an edge weight. Edge {(u, v, k, d)}"
                        raise ValueError(msg)
                    push(frontier, (wt, next(c), u, v, k, d))
        else:
            for v, d in G.adj[u].items():
                wt = d.get(weight, 1) * sign
                if isnan(wt):
                    if ignore_nan:
                        continue
                    msg = f"NaN found as an edge weight. Edge {(u, v, d)}"
                    raise ValueError(msg)
                push(frontier, (wt, next(c), u, v, d))
        while nodes and frontier:
            if is_multigraph:
                W, _, u, v, k, d = pop(frontier)
            else:
                W, _, u, v, d = pop(frontier)
            if v in visited or v not in nodes:
                continue
            # Multigraphs need to handle edge keys in addition to edge data.
            if is_multigraph and keys:
                if data:
                    yield u, v, k, d
                else:
                    yield u, v, k
            else:
                if data:
                    yield u, v, d
                else:
                    yield u, v
            # update frontier
            visited.add(v)
            nodes.discard(v)
            if is_multigraph:
                for w, keydict in G.adj[v].items():
                    if w in visited:
                        continue
                    for k2, d2 in keydict.items():
                        new_weight = d2.get(weight, 1) * sign
                        push(frontier, (new_weight, next(c), v, w, k2, d2))
            else:
                for w, d2 in G.adj[v].items():
                    if w in visited:
                        continue
                    new_weight = d2.get(weight, 1) * sign
                    push(frontier, (new_weight, next(c), v, w, d2))


ALGORITHMS = {
    "boruvka": boruvka_mst_edges,
    "borůvka": boruvka_mst_edges,
    "kruskal": kruskal_mst_edges,
    "prim": prim_mst_edges,
}


@not_implemented_for("directed")
def minimum_spanning_edges(
    G, algorithm="kruskal", weight="weight", keys=True, data=True, ignore_nan=False
):
    """Generate edges in a minimum spanning forest of an undirected
    weighted graph.

    A minimum spanning tree is a subgraph of the graph (a tree)
    with the minimum sum of edge weights.  A spanning forest is a
    union of the spanning trees for each connected component of the graph.

    Parameters
    ----------
    G : undirected Graph
       An undirected graph. If `G` is connected, then the algorithm finds a
       spanning tree. Otherwise, a spanning forest is found.

    algorithm : string
       The algorithm to use when finding a minimum spanning tree. Valid
       choices are 'kruskal', 'prim', or 'boruvka'. The default is 'kruskal'.

    weight : string
       Edge data key to use for weight (default 'weight').

    keys : bool
       Whether to yield edge key in multigraphs in addition to the edge.
       If `G` is not a multigraph, this is ignored.

    data : bool, optional
       If True yield the edge data along with the edge.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.

    Returns
    -------
    edges : iterator
       An iterator over edges in a maximum spanning tree of `G`.
       Edges connecting nodes `u` and `v` are represented as tuples:
       `(u, v, k, d)` or `(u, v, k)` or `(u, v, d)` or `(u, v)`

       If `G` is a multigraph, `keys` indicates whether the edge key `k` will
       be reported in the third position in the edge tuple. `data` indicates
       whether the edge datadict `d` will appear at the end of the edge tuple.

       If `G` is not a multigraph, the tuples are `(u, v, d)` if `data` is True
       or `(u, v)` if `data` is False.

    Examples
    --------
    >>> from networkx.algorithms import tree

    Find minimum spanning edges by Kruskal's algorithm

    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight=2)
    >>> mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
    >>> edgelist = list(mst)
    >>> sorted(sorted(e) for e in edgelist)
    [[0, 1], [1, 2], [2, 3]]

    Find minimum spanning edges by Prim's algorithm

    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight=2)
    >>> mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
    >>> edgelist = list(mst)
    >>> sorted(sorted(e) for e in edgelist)
    [[0, 1], [1, 2], [2, 3]]

    Notes
    -----
    For Borůvka's algorithm, each edge must have a weight attribute, and
    each edge weight must be distinct.

    For the other algorithms, if the graph edges do not have a weight
    attribute a default weight of 1 will be used.

    Modified code from David Eppstein, April 2006
    http://www.ics.uci.edu/~eppstein/PADS/

    """
    try:
        algo = ALGORITHMS[algorithm]
    except KeyError as err:
        msg = f"{algorithm} is not a valid choice for an algorithm."
        raise ValueError(msg) from err

    return algo(
        G, minimum=True, weight=weight, keys=keys, data=data, ignore_nan=ignore_nan
    )


@not_implemented_for("directed")
def maximum_spanning_edges(
    G, algorithm="kruskal", weight="weight", keys=True, data=True, ignore_nan=False
):
    """Generate edges in a maximum spanning forest of an undirected
    weighted graph.

    A maximum spanning tree is a subgraph of the graph (a tree)
    with the maximum possible sum of edge weights.  A spanning forest is a
    union of the spanning trees for each connected component of the graph.

    Parameters
    ----------
    G : undirected Graph
       An undirected graph. If `G` is connected, then the algorithm finds a
       spanning tree. Otherwise, a spanning forest is found.

    algorithm : string
       The algorithm to use when finding a maximum spanning tree. Valid
       choices are 'kruskal', 'prim', or 'boruvka'. The default is 'kruskal'.

    weight : string
       Edge data key to use for weight (default 'weight').

    keys : bool
       Whether to yield edge key in multigraphs in addition to the edge.
       If `G` is not a multigraph, this is ignored.

    data : bool, optional
       If True yield the edge data along with the edge.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.

    Returns
    -------
    edges : iterator
       An iterator over edges in a maximum spanning tree of `G`.
       Edges connecting nodes `u` and `v` are represented as tuples:
       `(u, v, k, d)` or `(u, v, k)` or `(u, v, d)` or `(u, v)`

       If `G` is a multigraph, `keys` indicates whether the edge key `k` will
       be reported in the third position in the edge tuple. `data` indicates
       whether the edge datadict `d` will appear at the end of the edge tuple.

       If `G` is not a multigraph, the tuples are `(u, v, d)` if `data` is True
       or `(u, v)` if `data` is False.

    Examples
    --------
    >>> from networkx.algorithms import tree

    Find maximum spanning edges by Kruskal's algorithm

    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight=2)
    >>> mst = tree.maximum_spanning_edges(G, algorithm="kruskal", data=False)
    >>> edgelist = list(mst)
    >>> sorted(sorted(e) for e in edgelist)
    [[0, 1], [0, 3], [1, 2]]

    Find maximum spanning edges by Prim's algorithm

    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight=2)  # assign weight 2 to edge 0-3
    >>> mst = tree.maximum_spanning_edges(G, algorithm="prim", data=False)
    >>> edgelist = list(mst)
    >>> sorted(sorted(e) for e in edgelist)
    [[0, 1], [0, 3], [2, 3]]

    Notes
    -----
    For Borůvka's algorithm, each edge must have a weight attribute, and
    each edge weight must be distinct.

    For the other algorithms, if the graph edges do not have a weight
    attribute a default weight of 1 will be used.

    Modified code from David Eppstein, April 2006
    http://www.ics.uci.edu/~eppstein/PADS/
    """
    try:
        algo = ALGORITHMS[algorithm]
    except KeyError as err:
        msg = f"{algorithm} is not a valid choice for an algorithm."
        raise ValueError(msg) from err

    return algo(
        G, minimum=False, weight=weight, keys=keys, data=data, ignore_nan=ignore_nan
    )


def minimum_spanning_tree(G, weight="weight", algorithm="kruskal", ignore_nan=False):
    """Returns a minimum spanning tree or forest on an undirected graph `G`.

    Parameters
    ----------
    G : undirected graph
        An undirected graph. If `G` is connected, then the algorithm finds a
        spanning tree. Otherwise, a spanning forest is found.

    weight : str
       Data key to use for edge weights.

    algorithm : string
       The algorithm to use when finding a minimum spanning tree. Valid
       choices are 'kruskal', 'prim', or 'boruvka'. The default is
       'kruskal'.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.

    Returns
    -------
    G : NetworkX Graph
       A minimum spanning tree or forest.

    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight=2)
    >>> T = nx.minimum_spanning_tree(G)
    >>> sorted(T.edges(data=True))
    [(0, 1, {}), (1, 2, {}), (2, 3, {})]


    Notes
    -----
    For Borůvka's algorithm, each edge must have a weight attribute, and
    each edge weight must be distinct.

    For the other algorithms, if the graph edges do not have a weight
    attribute a default weight of 1 will be used.

    There may be more than one tree with the same minimum or maximum weight.
    See :mod:`networkx.tree.recognition` for more detailed definitions.

    Isolated nodes with self-loops are in the tree as edgeless isolated nodes.

    """
    edges = minimum_spanning_edges(
        G, algorithm, weight, keys=True, data=True, ignore_nan=ignore_nan
    )
    T = G.__class__()  # Same graph class as G
    T.graph.update(G.graph)
    T.add_nodes_from(G.nodes.items())
    T.add_edges_from(edges)
    return T


def partition_spanning_tree(
    G, minimum=True, weight="weight", partition="partition", ignore_nan=False
):
    """
    Find a spanning tree while respecting a partition of edges.

    Edges can be flagged as either `INLCUDED` which are required to be in the
    returned tree, `EXCLUDED`, which cannot be in the returned tree and `OPEN`.

    This is used in the SpanningTreeIterator to create new partitions following
    the algorithm of Sörensen and Janssens [1]_.

    Parameters
    ----------
    G : undirected graph
        An undirected graph.

    minimum : bool (default: True)
        Determines whether the returned tree is the minimum spanning tree of
        the partition of the maximum one.

    weight : str
        Data key to use for edge weights.

    partition : str
        The key for the edge attribute containing the partition
        data on the graph. Edges can be included, excluded or open using the
        `EdgePartition` enum.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.


    Returns
    -------
    G : NetworkX Graph
        A minimum spanning tree using all of the included edges in the graph and
        none of the excluded edges.

    References
    ----------
    .. [1] G.K. Janssens, K. Sörensen, An algorithm to generate all spanning
           trees in order of increasing cost, Pesquisa Operacional, 2005-08,
           Vol. 25 (2), p. 219-229,
           https://www.scielo.br/j/pope/a/XHswBwRwJyrfL88dmMwYNWp/?lang=en
    """
    edges = kruskal_mst_edges(
        G,
        minimum,
        weight,
        keys=True,
        data=True,
        ignore_nan=ignore_nan,
        partition=partition,
    )
    T = G.__class__()  # Same graph class as G
    T.graph.update(G.graph)
    T.add_nodes_from(G.nodes.items())
    T.add_edges_from(edges)
    return T


def maximum_spanning_tree(G, weight="weight", algorithm="kruskal", ignore_nan=False):
    """Returns a maximum spanning tree or forest on an undirected graph `G`.

    Parameters
    ----------
    G : undirected graph
        An undirected graph. If `G` is connected, then the algorithm finds a
        spanning tree. Otherwise, a spanning forest is found.

    weight : str
       Data key to use for edge weights.

    algorithm : string
       The algorithm to use when finding a maximum spanning tree. Valid
       choices are 'kruskal', 'prim', or 'boruvka'. The default is
       'kruskal'.

    ignore_nan : bool (default: False)
        If a NaN is found as an edge weight normally an exception is raised.
        If `ignore_nan is True` then that edge is ignored instead.


    Returns
    -------
    G : NetworkX Graph
       A maximum spanning tree or forest.


    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight=2)
    >>> T = nx.maximum_spanning_tree(G)
    >>> sorted(T.edges(data=True))
    [(0, 1, {}), (0, 3, {'weight': 2}), (1, 2, {})]


    Notes
    -----
    For Borůvka's algorithm, each edge must have a weight attribute, and
    each edge weight must be distinct.

    For the other algorithms, if the graph edges do not have a weight
    attribute a default weight of 1 will be used.

    There may be more than one tree with the same minimum or maximum weight.
    See :mod:`networkx.tree.recognition` for more detailed definitions.

    Isolated nodes with self-loops are in the tree as edgeless isolated nodes.

    """
    edges = maximum_spanning_edges(
        G, algorithm, weight, keys=True, data=True, ignore_nan=ignore_nan
    )
    edges = list(edges)
    T = G.__class__()  # Same graph class as G
    T.graph.update(G.graph)
    T.add_nodes_from(G.nodes.items())
    T.add_edges_from(edges)
    return T


class SpanningTreeIterator:
    """
    Iterate over all spanning trees of a graph in either increasing or
    decreasing cost.

    Notes
    -----
    This iterator uses the partition scheme from [1]_ (included edges,
    excluded edges and open edges) as well as a modified Kruskal's Algorithm
    to generate minimum spanning trees which respect the partition of edges.
    For spanning trees with the same weight, ties are broken arbitrarily.

    References
    ----------
    .. [1] G.K. Janssens, K. Sörensen, An algorithm to generate all spanning
           trees in order of increasing cost, Pesquisa Operacional, 2005-08,
           Vol. 25 (2), p. 219-229,
           https://www.scielo.br/j/pope/a/XHswBwRwJyrfL88dmMwYNWp/?lang=en
    """

    @dataclass(order=True)
    class Partition:
        """
        This dataclass represents a partition and stores a dict with the edge
        data and the weight of the minimum spanning tree of the partition dict.
        """

        mst_weight: float
        partition_dict: dict = field(compare=False)

        def __copy__(self):
            return SpanningTreeIterator.Partition(
                self.mst_weight, self.partition_dict.copy()
            )

    def __init__(self, G, weight="weight", minimum=True, ignore_nan=False):
        """
        Initialize the iterator

        Parameters
        ----------
        G : nx.Graph
            The directed graph which we need to iterate trees over

        weight : String, default = "weight"
            The edge attribute used to store the weight of the edge

        minimum : bool, default = True
            Return the trees in increasing order while true and decreasing order
            while false.

        ignore_nan : bool, default = False
            If a NaN is found as an edge weight normally an exception is raised.
            If `ignore_nan is True` then that edge is ignored instead.
        """
        self.G = G.copy()
        self.weight = weight
        self.minimum = minimum
        self.ignore_nan = ignore_nan
        # Randomly create a key for an edge attribute to hold the partition data
        self.partition_key = (
            "SpanningTreeIterators super secret partition attribute name"
        )

    def __iter__(self):
        """
        Returns
        -------
        SpanningTreeIterator
            The iterator object for this graph
        """
        self.partition_queue = PriorityQueue()
        self._clear_partition(self.G)
        mst_weight = partition_spanning_tree(
            self.G, self.minimum, self.weight, self.partition_key, self.ignore_nan
        ).size(weight=self.weight)

        self.partition_queue.put(
            self.Partition(mst_weight if self.minimum else -mst_weight, dict())
        )

        return self

    def __next__(self):
        """
        Returns
        -------
        (multi)Graph
            The spanning tree of next greatest weight, which ties broken
            arbitrarily.
        """
        if self.partition_queue.empty():
            del self.G, self.partition_queue
            raise StopIteration

        partition = self.partition_queue.get()
        self._write_partition(partition)
        next_tree = partition_spanning_tree(
            self.G, self.minimum, self.weight, self.partition_key, self.ignore_nan
        )
        self._partition(partition, next_tree)

        self._clear_partition(next_tree)
        return next_tree

    def _partition(self, partition, partition_tree):
        """
        Create new partitions based of the minimum spanning tree of the
        current minimum partition.

        Parameters
        ----------
        partition : Partition
            The Partition instance used to generate the current minimum spanning
            tree.
        partition_tree : nx.Graph
            The minimum spanning tree of the input partition.
        """
        # create two new partitions with the data from the input partition dict
        p1 = self.Partition(0, partition.partition_dict.copy())
        p2 = self.Partition(0, partition.partition_dict.copy())
        for e in partition_tree.edges:
            # determine if the edge was open or included
            if e not in partition.partition_dict:
                # This is an open edge
                p1.partition_dict[e] = EdgePartition.EXCLUDED
                p2.partition_dict[e] = EdgePartition.INCLUDED

                self._write_partition(p1)
                p1_mst = partition_spanning_tree(
                    self.G,
                    self.minimum,
                    self.weight,
                    self.partition_key,
                    self.ignore_nan,
                )
                p1_mst_weight = p1_mst.size(weight=self.weight)
                if nx.is_connected(p1_mst):
                    p1.mst_weight = p1_mst_weight if self.minimum else -p1_mst_weight
                    self.partition_queue.put(p1.__copy__())
                p1.partition_dict = p2.partition_dict.copy()

    def _write_partition(self, partition):
        """
        Writes the desired partition into the graph to calculate the minimum
        spanning tree.

        Parameters
        ----------
        partition : Partition
            A Partition dataclass describing a partition on the edges of the
            graph.
        """
        for u, v, d in self.G.edges(data=True):
            if (u, v) in partition.partition_dict:
                d[self.partition_key] = partition.partition_dict[(u, v)]
            else:
                d[self.partition_key] = EdgePartition.OPEN

    def _clear_partition(self, G):
        """
        Removes partition data from the graph
        """
        for u, v, d in G.edges(data=True):
            if self.partition_key in d:
                del d[self.partition_key]
