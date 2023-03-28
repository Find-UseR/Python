Graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["NULL", "H"],
}


def BFS(Tree, s, g, Path=[]):
    ct = s
    Queue = []
    while ct != g:
        node = Graph[ct]
        left = node[0]
        right = node[1]
        if left != "NULL":
            Queue.append(left)
        if right != "NULL":
            Queue.append(right)
        if (len(Queue) != 0):
            Path.append(ct)
            ct = Queue.pop(0)
        if ct == g:
            Path.append(ct)
            return Path


print(BFS(Graph, "A", "E"))