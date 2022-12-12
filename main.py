from typing import List


def topologicalSort(adjList, numOfVertices) -> List[int]:
    visited = [False for _ in range(numOfVertices)]
    order = []
    def helper(v):
        visited[v] = True
        for vertex, _ in adjList.get(v):
            if not visited[vertex]:
                helper(vertex)
        order.insert(0,v)

    for vertex in range(numOfVertices-1):
        if not visited[vertex]:
            helper(vertex)
          
    return order

def longestPath(start: int, end: int, adjList, numOfVertices: int, edges) -> int:
    distances = [-1 for _ in range(numOfVertices)]    
    distances[start] = 0

    for node in topologicalSort(adjList, numOfVertices):
      if distances[node] == -1:
        continue
      for neighbor, weight in adjList.get(node):
          distances[neighbor] = max(distances[neighbor], distances[node] + weight)
    return distances[end]

def main():
    numOfVertices, numOfEdges = [int(_) for _ in input().split()]
    i, j = [int(_) for _ in input().split()]
    edges = []
    
    for _ in range(numOfEdges):
        node, target, weight = [int(_) for _ in input().split()]
        edges.append((node, target, weight))
    
    adjList = { c:[] for c in range(numOfVertices) } #dictionary
    for src, dest, weight in edges:
        adjList[src].append((dest, weight))
    
    print(longestPath(i, j, adjList, numOfVertices, edges) )

if __name__ == "__main__":
    main()
