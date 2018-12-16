# NOTE: DFS implementation is WRONG. It will fail test1_8.in, and input.txt

import sys

def dfs(graph, current, visited, traverse_stack):
    if visited[current]:
        return
    
    all_child = sorted(graph[current], reverse=True)
    for c in all_child:
        dfs(graph, c, visited, traverse_stack)

    traverse_stack.append(current)
    visited[current] = True

def main():
    graph = {}
    visited = {}

    for line in sys.stdin:
        lineread = line.split(' ')
        src = lineread[1]
        dest = lineread[7]
        if src not in graph:
            graph[src] = []
            visited[src] = False
        if dest not in graph:
            graph[dest] = []
            visited[dest] = False
        graph[src].append(dest)

    # print(graph)

    all_keys = sorted(list(graph.keys()), reverse=True)
    traverse_stack = []
    for k in all_keys:
        dfs(graph, k, visited, traverse_stack)

    while len(traverse_stack) > 0:
        print(traverse_stack.pop(), end='')
    print()

main()
