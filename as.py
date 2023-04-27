import heapq

def astar(graph, start, end):
    # Create dictionaries for storing the shortest distance and the path
    shortest_distance = {}
    path = {}
    
    # Create a heap for the frontier
    frontier = [(0, start)]
    
    # Initialize the shortest distance of the start node to 0
    shortest_distance[start] = 0
    
    # Start the A* search algorithm
    while frontier:
        # Pop the node with the smallest priority value from the heap
        current_distance, current_node = heapq.heappop(frontier)
        
        # If we have reached the end node, we are done
        if current_node == end:
            # Build the path in reverse order
            reverse_path = []
            while current_node in path:
                reverse_path.append(current_node)
                current_node = path[current_node]
            reverse_path.append(start)
            
            # Reverse the path and return the distance and the path
            return current_distance, list(reversed(reverse_path))
        
        # Visit all the neighbors of the current node
        for neighbor, distance in graph[current_node].items():
            # Calculate the total cost from start to neighbor through the current node
            total_distance = shortest_distance[current_node] + distance
            
            # If the neighbor has not been visited yet or the total cost is smaller than the previous cost
            if neighbor not in shortest_distance or total_distance < shortest_distance[neighbor]:
                # Update the shortest distance of the neighbor
                shortest_distance[neighbor] = total_distance
                
                # Calculate the priority value using the heuristic distance
                priority = total_distance + graph[neighbor]['heuristic']
                
                # Add the neighbor to the frontier with the new priority value
                heapq.heappush(frontier, (priority, neighbor))
                
                # Update the path of the neighbor
                path[neighbor] = current_node
    
    # If we haven't found the end node, there is no path
    return float('inf'), []

# Read the input.txt file and construct the graph
graph = {}
with open('input.txt') as f:
    for line in f:
        parts = line.split()
        node = parts[0]
        graph[node] = {'heuristic': int(parts[1]), 'neighbors': {}}
        for i in range(2, len(parts), 2):
            neighbor = parts[i]
            distance = int(parts[i+1])
            graph[node]['neighbors'][neighbor] = distance

# Ask the user for the start and end nodes
start = input('Start node: ')
end = input('Destination: ')

# Run the A* search algorithm
distance, path = astar(graph, start, end)

# Print the result
if not path:
    print('NO PATH FOUND')
else:
    print('Path:', ' -> '.join(path))
    print('Total distance:', distance, 'km')
