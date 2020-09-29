from math import sqrt

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
