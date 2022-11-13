def genreate_cost(graph):
    infinity = float('inf')
    costs = {}
    for k in graph.keys():
        if k in graph['start'].keys():
            costs[k] = graph['start'][k]
        elif k != 'start':
            costs[k] = infinity
    return costs


def generate_parent(graph):
    parents = {}
    for k in graph.keys():
        if k in graph['start'].keys():
            parents[k] = 'start'
        elif k != 'start':
            parents[k] = ''
    return parents


def find_lowest_cost_note(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for k in costs:
        if costs[k] < lowest_cost and k not in processed:
            lowest_cost = costs[k]
            lowest_cost_node = k
    return lowest_cost_node


def find_shortest_path_and_cost(graph):

    costs = genreate_cost(graph)
    parents = generate_parent(graph)

    processed = []
    node = find_lowest_cost_note(costs, processed)
    while node:
        for neig in graph[node]:
            new_cost = costs[node] + graph[node][neig]
            if new_cost < costs[neig]:
                costs[neig] = new_cost
                parents[neig] = node
        processed.append(node)
        node = find_lowest_cost_note(costs, processed)


    path = ['finish']
    k = parents['finish']
    while k != 'start':
        path.append(k)
        k = parents[k]
    path.append('start')
    path = ' -> '.join(path[::-1])

    total_cost = costs['finish']
    return(path, total_cost)