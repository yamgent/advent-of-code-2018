import sys

# algorithm used is Kahn's algorithm, because it will traverse through alphabetically
# from smallest to biggest (we do not have the same control with DFS, see the DFS
# implementation that fails test1_8.in)

def main():
    graphChild = {}
    graphParent = {}

    for line in sys.stdin:
        lineread = line.split(' ')

        src = lineread[1]
        dest = lineread[7]

        if src not in graphChild:
            graphChild[src] = []
        if src not in graphParent:
            graphParent[src] = []

        if dest not in graphChild:
            graphChild[dest] = []
        if dest not in graphParent:
            graphParent[dest] = []

        graphChild[src].append(dest)
        graphParent[dest].append(src)

    # print(graph)

    current_nodes = []
    for k, v in graphParent.items():
        if len(v) == 0:
            current_nodes.append(k)
    current_nodes = sorted(current_nodes, reverse=True)

    while len(current_nodes) > 0:
        first = current_nodes.pop()
        print(first, end='')

        for c in graphChild[first]:
            graphParent[c].remove(first)
            if len(graphParent[c]) == 0:
                current_nodes.append(c)

        current_nodes = sorted(current_nodes, reverse=True)
    print()

main()
