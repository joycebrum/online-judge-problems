import sys


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=342
"""
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
"""

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi


#------------------------

class Nodo:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, data=-1, before=None, after=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s -> {%s %s}' % (self.data, self.left, self.right)
class List:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.head = Nodo()

    def __repr__(self):
        return "[" + str(self.head) + "]"

    
def compare_words(last, current, order):
    print(last, current)
    i = 0
    while i < len(last) and i < len(current) and last[i] == current[i]:
        i += 1
    if i < len(last) and i < len(current):
        if not last[i] in order or not order[last[i]]:
            order[last[i]] = current[i]
            order[current[i]] = ''

def print_ordered_letters(order):
    current = order['first']
    result = ''
    print(order)
    while current:
        result += current
        current = order[current]
    print('resultado', result)
    
if __name__ == '__main__':
    order = {}
    current = ''
    
    last = input().strip()
    order['first'] = last[0]

    while True:
        current = input().strip()
        if current == '#': break
        compare_words(last, current, order)
        last = current
    print_ordered_letters(order)
        
            

#------------------------ não mandar essa parte
"""        
sys.stdout = orig_stdout
f.close()
"""
sys.stdin = orig_stdin
fi.close

#------------------------
