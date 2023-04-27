import heapq

def read_graph(file_name):
    # read the graph from the given file
    graph = {}
    with open(file_name, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            node = tokens[0]
            graph[node] = []
            graph[node].append(float(tokens[1]))
            for i in range(2, len(tokens)-1, 2):
                graph[node].append((tokens[i], float(tokens[i+1])))
    return graph

def a_star(graph, start, end):
    # perform A* search algorithm to find the most optimal path
    visited = set()
    heap = [(0, start, [])]
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path, cost
            for neighbor, neighbor_cost in graph[node][1:]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost+neighbor_cost+graph[neighbor][0], neighbor, path))
    return "NO PATH FOUND"

# read the graph from the input.txt file
graph = read_graph("input.txt")

# take user input for start and end nodes
start = input("Start node: ")
end = input("Destination: ")

# perform A* search and print the result
result = a_star(graph, start, end)
if type(result) == str:
    print(result)
else:
    path, cost = result
    print("Path:", " -> ".join(path))
    print("Total distance:", cost, "km")
