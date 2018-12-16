import sys

class Worker:
    def __init__(self):
        self.char = ''
        self.finishTime = -1

    def assign(self, time, newChar):
        if not self.done(time):
            return False

        self.char = newChar
        self.finishTime = time + 60 + (1 + ord(newChar) - ord('A'))
        return True

    def done(self, time):
        return time >= self.finishTime

    def just_finished(self, time):
        return time == self.finishTime

def all_workers_free(workers, time):
    for w in workers:
        if not w.done(time):
            return False
    return True

def all_workers_busy(workers, time):
    for w in workers:
        if w.done(time):
            return False
    return True

def get_finished_at_this_time(workers, time):
    finishedAtThisTime = []
    for w in workers:
        if w.just_finished(time):
            finishedAtThisTime.append(w.char)
    return sorted(finishedAtThisTime)

class Graph:
    def __init__(self):
        self.child = {}
        self.parent = {}

    def add_edge(self, src, dest):
        if src not in self.child:
            self.child[src] = []
        if src not in self.parent:
            self.parent[src] = []

        if dest not in self.child:
            self.child[dest] = []
        if dest not in self.parent:
            self.parent[dest] = []

        self.child[src].append(dest)
        self.parent[dest].append(src)

    def remove_node(self, node):
        for c in self.child[node]:
            self.parent[c].remove(node)

        del self.child[node]
        del self.parent[node]

    def get_all_node_with_indegree_zero(self):
        result = []
        for k in self.parent:
            if self.get_indegree(k) == 0:
                result.append(k)
        return sorted(result)

    def get_indegree(self, node):
        return len(self.parent[node])

    def get_outdegree(self, node):
        return len(self.child[node])

def main():
    graphNotTaken = Graph()
    graphNotComplete = Graph()

    for line in sys.stdin:
        lineread = line.split(' ')
        src = lineread[1]
        dest = lineread[7]
        graphNotTaken.add_edge(src, dest)
        graphNotComplete.add_edge(src, dest)

    time = 0
    workers = [Worker(), Worker(), Worker(), Worker(), Worker()]
    current_nodes = graphNotTaken.get_all_node_with_indegree_zero()

    while len(current_nodes) > 0:        
        for n in current_nodes:
            if all_workers_busy(workers, time):
                break

            if graphNotComplete.get_indegree(n) != 0:
                continue

            for w in workers:
                if w.assign(time, n):
                    break

            graphNotTaken.remove_node(n)

        time += 1        
        finished_nodes = get_finished_at_this_time(workers, time)
        # print(''.join(finished_nodes), end='')

        for n in finished_nodes:
            graphNotComplete.remove_node(n)
        current_nodes = graphNotTaken.get_all_node_with_indegree_zero()

    while not all_workers_free(workers, time):
        time += 1
        finished_nodes = get_finished_at_this_time(workers, time)
        # print(''.join(finished_nodes), end='')

    print(time)

main()
