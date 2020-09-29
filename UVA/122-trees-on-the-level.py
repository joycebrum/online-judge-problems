from collections import deque 

pot = [pow(2, i) for i in range(0,11)]
class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, data=-1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s -> {%s %s}' % (self.data, self.left, self.right)
class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.head = NodoLista()

    def __repr__(self):
        return "[" + str(self.head) + "]"
    
def get_level_tree(lista):
    nexts = deque()
    if lista.head.data >= 0: nexts.append(lista.head)
    res = []
    while True:
        if not nexts: break
        actual = nexts.popleft()
        if actual.data >= 0:
            res.append(str(actual.data))
        if actual.left and actual.left.data >= 0:
            nexts.append(actual.left)
        if actual.right and actual.right.data >= 0:
            nexts.append(actual.right)
    return res

def add_node(lista, node):
    if not node[1]:
        lista.head.data = int(node[0])
        return
    actual = lista.head
    for side in node[1]:
        if side == 'L':
            if not actual.left:
                actual.left = NodoLista()
            actual = actual.left
        if side == 'R':
            if not actual.right:
                actual.right = NodoLista()
            actual = actual.right
    actual.data = int(node[0])

if __name__ == '__main__':
    lista = ListaEncadeada() 
    nElements = 0
    while True:
        line = sys.stdin.readline().strip()
        if not line: break
        for node_str in line.split():
            node = node_str.strip('()').split(',')
            if len(node) == 1 and not node[0]:
                res = get_level_tree(lista)
                if len(res) != nElements:
                    print('not complete')
                else:
                    print(" ".join(res))
                del lista
                lista = ListaEncadeada()
                nElements = 0
                break
            nElements += 1
            add_node(lista, node)
