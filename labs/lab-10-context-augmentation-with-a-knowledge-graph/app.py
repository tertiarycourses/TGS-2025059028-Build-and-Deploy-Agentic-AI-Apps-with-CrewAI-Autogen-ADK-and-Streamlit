"""
Lab 10 — Context Augmentation with a Knowledge Graph

Vector similarity alone cannot answer multi-hop questions that require joining
facts. This script models the invoice data as entities and relationships, then
answers a question plain RAG gets wrong.

    python app.py
"""
import csv
import os

import networkx as nx

DATA = os.path.join(os.path.dirname(__file__), "data", "invoice_graph.csv")


def build_graph(path: str) -> nx.DiGraph:
    """Load the entity/relationship CSV into a directed graph."""
    G = nx.DiGraph()
    with open(path) as f:
        for row in csv.DictReader(f):
            G.add_edge(row["Source"], row["Target"], rel=row["Relationship"])
    return G


def customers_who_bought_the_same(G: nx.DiGraph, customer: str) -> set:
    """The multi-hop query: customer -> invoices -> products -> invoices -> customers."""
    products = [p for inv in G.successors(customer) for p in G.successors(inv)]
    others = {c
              for p in products
              for inv in G.predecessors(p)
              for c in G.predecessors(inv)}
    return others - {customer}


def main():
    G = build_graph(DATA)
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges\n")

    target = "Aaron Hawkins"
    products = [p for inv in G.successors(target) for p in G.successors(inv)]
    print(f"{target} bought: {sorted(set(products))}")

    others = customers_who_bought_the_same(G, target)
    print(f"Other customers who bought the same product(s): {sorted(others)}")

    print("\nAsk your Lab 8 RAG app the same question.")
    print("Flat vector retrieval cannot reliably make this connection —")
    print("that gap is the whole argument for GraphRAG.")


if __name__ == "__main__":
    main()
