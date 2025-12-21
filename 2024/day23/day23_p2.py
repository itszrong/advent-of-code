from __future__ import annotations
from collections import defaultdict
from typing import Dict, Set, Hashable, List, Iterable, Optional

def main():
    with open("day23/data.txt", "r") as f:
        contents = f.read()


    graph = defaultdict(set)
    for line in contents.splitlines():
        s1, s2 = line.split('-')
        graph[s1].add(s2)
        graph[s2].add(s1)


    Node = Hashable
    Graph = Dict[Node, Set[Node]]


    def bron_kerbosch_maximal_cliques(G: Graph) -> List[Set[Node]]:
        """
        Return all maximal cliques in an undirected simple graph G.

        G must be an adjacency dict: node -> set of neighbors.
        Assumes: no self-loops; symmetric adjacency (u in G[v] <=> v in G[u]).
        """
        cliques: List[Set[Node]] = []

        # Copy to avoid accidental mutation surprises
        P: Set[Node] = set(G.keys())
        R: Set[Node] = set()
        X: Set[Node] = set()

        def bk(R: Set[Node], P: Set[Node], X: Set[Node]) -> None:
            if not P and not X:
                cliques.append(set(R))
                return

            # Pivot: choose u from P ∪ X maximizing neighbors in P (common heuristic)
            U = P | X
            if U:
                u = max(U, key=lambda n: len(G[n] & P))
                candidates = P - G[u]
            else:
                candidates = set(P)

            for v in list(candidates):
                Nv = G[v]
                bk(R | {v}, P & Nv, X & Nv)
                P.remove(v)
                X.add(v)

        bk(R, P, X)
        return cliques


    def maximum_clique(G: Graph) -> Set[Node]:
        """Return one maximum clique (largest maximal clique)."""
        cliques = bron_kerbosch_maximal_cliques(G)
        return max(cliques, key=len, default=set())

    res = list(maximum_clique(graph))
    res.sort()
    print("Maximum clique:", res)
    print(','.join(res))


if __name__ == "__main__":
    main()
