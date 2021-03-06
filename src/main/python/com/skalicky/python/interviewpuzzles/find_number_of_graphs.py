# Task:
#
# Given a list of undirected edges which represents a graph, find out the number of connected components.
#
# def num_connected_components(edges):
# 	# Fill this in.
#
# print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# # 2
#
#
# In the above example, vertices 1, 2, 3, 4 are all connected, and 5, 6 are connected, and thus there are 2 connected
# components in the graph above.
from typing import Dict, List, Tuple


def find_number_of_graphs(edges: List[Tuple[int, int]]) -> int:
    graphs_by_vertices: Dict[int, int] = {}
    list_of_vertices_by_graphs: Dict[int, List[int]] = {}
    graph_id_generator: int = 1
    for edge in edges:
        vertex_1: int = edge[0]
        vertex_2: int = edge[1]
        if vertex_1 in graphs_by_vertices and vertex_2 in graphs_by_vertices:
            old_graph_1: int = graphs_by_vertices[vertex_1]
            old_graph_2: int = graphs_by_vertices[vertex_2]
            if old_graph_1 != old_graph_2:
                old_graph_1_size: int = len(list_of_vertices_by_graphs[old_graph_1])
                old_graph_2_size: int = len(list_of_vertices_by_graphs[old_graph_2])
                source_graph: int = old_graph_2 if old_graph_1_size > old_graph_2_size else old_graph_1
                destination_graph: int = old_graph_1 if old_graph_1_size > old_graph_2_size else old_graph_2

                for source_graph_vertex in list_of_vertices_by_graphs.pop(source_graph):
                    list_of_vertices_by_graphs[destination_graph].append(source_graph_vertex)
                    graphs_by_vertices[source_graph_vertex] = destination_graph

        elif vertex_1 in graphs_by_vertices:
            graphs_by_vertices[vertex_2] = graphs_by_vertices[vertex_1]
            list_of_vertices_by_graphs[graphs_by_vertices[vertex_1]].append(vertex_2)
        elif vertex_2 in graphs_by_vertices:
            graphs_by_vertices[vertex_1] = graphs_by_vertices[vertex_2]
            list_of_vertices_by_graphs[graphs_by_vertices[vertex_1]].append(vertex_1)
        else:
            graphs_by_vertices[vertex_1] = graph_id_generator
            graphs_by_vertices[vertex_2] = graph_id_generator
            list_of_vertices_by_graphs[graph_id_generator] = [vertex_1, vertex_2]
            graph_id_generator += 1
    return len(list_of_vertices_by_graphs.keys())
