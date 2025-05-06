
"""
Problem:
Given a weighted graph of cities connected by roads (edges with weights),
determine the shortest path between a specified start and destination city
using Dijkstra's Algorithm.

Approach:
- Use a priority queue (min-heap) to explore the shortest distance node first.
- Maintain a dictionary to track shortest known distances to each node.
- Track the parent of each node to reconstruct the shortest path once destination is reached.
"""
# import to use heap queue algo. also known as priority queue.
import heapq

def dijkstra(graph, start, end):
    # Priority queue: (distance, city)
    queue = [(0, start)]
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {city: None for city in graph}

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        if current_city == end:
            break

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    return path, distances[end]

if __name__ == "__main__":
    cities = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'C': 3, 'D': 9},
        'C': {'A': 10, 'B': 3, 'D': 1},
        'D': {'B': 9, 'C': 1}
    }

    start_city = 'A'
    destination_city = 'D'
    shortest_path, total_distance = dijkstra(cities, start_city, destination_city)

    print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(shortest_path)}")
    print(f"Total distance: {total_distance}")
