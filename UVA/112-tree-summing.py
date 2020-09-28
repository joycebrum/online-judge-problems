import sys
from collections import deque 


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=56
""" 
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f"""

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------

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
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

def get_number(tree, pos):
    number = ''
    for i in range(pos, len(tree)):
        if tree[i] == '(' or tree[i] == ')':
            return int(number), i
        number += tree[i]
    return int(number), len(tree)-1
    

def process_entry(tree, pos, father)
    if tree[pos:pos+2] == '()':
        pos += 2
    else:
        number, pos = get_number(tree, pos + 1)
        father.left = NodoLista(number)
    if tree[pos:pos+2] == '()':
        pos += 2
    else:
        number, pos = get_number(tree, pos + 1)
        father.left = NodoLista(number)
    return pos

if __name__ == '__main__':
    lista = ListaEncadeada()
    summings = []
    while True:
        line = sys.stdin.readline().strip()
        if not line: break

        line = line.replace(' ', '')
        index = line.index('(')
        sum_v = line[0:index]
        tree = line[index:]

        root, pos = NodoLista(get_number(tree, 1))
        lista.head = root
        process_entry(tree, pos, root)
        
#------------------------ não mandar essa parte
""" 
sys.stdout = orig_stdout
f.close()
"""

sys.stdin = orig_stdin
fi.close
#------------------------
