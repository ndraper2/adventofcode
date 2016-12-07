import networkx as nx


def shortest_distance(distances):
    g = nx.Graph()
    for distance in distances:
        words = distance.split(' ')
        g.add_edge(words[0], words[2], {'weight': int(words[-1])})
    print(nx.all_pairs_dijkstra_path_length(g))


if __name__ == '__main__':
    with open('input9-1.txt', 'r') as f:
        distances = f.read().splitlines()
    print(shortest_distance(distances))