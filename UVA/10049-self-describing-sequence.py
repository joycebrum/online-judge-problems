import sys
from math import sqrt

#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=342
""" """
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f


orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi

#-----------------------
gr = (1 + sqrt(5))/2
const = pow((1 + sqrt(5))/2, 2-(1 + sqrt(5))/2)
e = gr - 1

values = {}

class Element:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, value=0, length=0):
        self.value = value
        self.length = length

    def __repr__(self):
        return '%s' % (self.value)

def f_exp(n):
    return round(const * pow(n, (1 + sqrt(5))/2 - 1))

def function(n):
    if '0' not in values:
        values[
    for i in range
        

if __name__ == '__main__':
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(function(n))
            

#------------------------ não mandar essa parte
""" """       
sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close

#------------------------
