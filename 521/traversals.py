def bfs(g, s):
    print("BFS: ", end="")
    visited = set()
    queue = [s]
    front = 0

    visited.add(s)

    while front < len(queue):
        node = queue[front]
        front += 1

        print(node, end=" ")

        for n in g[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

def dfs(g, s):
    print("DFS: ", end="")
    visited = set()
    stack = [s]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            print(node, end=" ")

            for n in reversed(g[node]):
                if n not in visited:
                    stack.append(n)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
print()
dfs(graph, 'A')