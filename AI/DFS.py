diction = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["NULL", "NULL"],
    "E": ["NULL", "H"],
    "F": ["NULL", "NULL"],
    "G": ["NULL", "NULL"],
    "H": ["NULL", "NULL"],
}



def DFS(Tree, S, G, Path=[]):
    crt = S
    Queue = []
    pre="NULL"
    while crt != G:
        node = diction[crt]
        left = node[0]
        right = node[1]
        if right != "NULL":
            Queue.insert(0, right)
        if left != "NULL":
            Queue.insert(0,left)
        if (len(Queue) != 0):
            Path.append(crt)
            crt = Queue.pop(0)
        if crt == G:
            Path.append(crt)
            return Path

print(DFS(diction, "A", "G"))
