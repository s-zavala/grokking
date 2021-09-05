#!/usr/bin/env python3
"""
Dijkstra's Algorithm -- find the shortest path on a weighted graph
"""
import pprint


printer = pprint.PrettyPrinter(indent=5)

def find_lowest_cost_node(costs):
    lowest = float("inf")
    lowest_node = None
    # Loop over nodes by cost.
    for node in costs:
        cost = costs[node]
        # Find lowest cost node that was not already processed.
        if (cost < lowest) and (node not in processed):
            lowest = cost
            lowest_node = node
    return lowest_node

graph = {
    "start":{"a":6, "b":2},
    "A": {"fin":1},
    "B": {"A":1, "fin":5},
    "fin": {}
}
costs = {
    "A":6,
    "B":2,
    "fin": float("inf")
}
parents = {}
processed = []

node = find_lowest_cost_node(costs)
# Loop over all nodes.
while node:
    cost = costs[node]
    neighbors = graph[node]
    # Loop over neighbors.
    for n in neighbors.keys():
        # Find the cost of path from current node to neighbor.
        new_cost = cost + neighbors[n]
        # Test if new path is less expensive.
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

printer.pprint(costs)