#!/usr/bin/env python
# coding=utf-8

def find_lowest_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
         cost = costs[node]
         if cost < lowest_cost and node  not in processed:
             lowest_cost = cost
             lowest_cost_node = node
    return lowest_cost_node
