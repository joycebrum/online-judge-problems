import sys

def find_leader(components, v):
    current = v
    while components[current] != current:
        current = components[current]
    return current

def connect(components, c1, c2, valency):
    valency[c1] += 1
    valency[c2] += 1
    l1, l2 = find_leader(components, c1), find_leader(components, c2)
    if l1 != l2:
        components[l2] = l1

def is_connected(components, valency, v):
    groups = 0
    for i in range(0, v):
        if components[i] == i and valency[i] > 0:
            groups += 1
            if groups > 1:
                return False
    return True

def has_just_pair_valencies(valency, v):
    for i in range(0, v):
        if valency[i] % 2 != 0:
            return False
    return True

def have_eulidian_path(components, valency, has_edge, v):
    return has_just_pair_valencies(valency, v) and is_connected(components, valency, v)

if __name__ == '__main__':
    while True:
        try:
            line = sys.stdin.readline().split()
            if not line: break
            
            v,a = [int (x) for x in line]
            components = [ i for i in range(0,v) ]
            has_edge = [ True for i in range(0, v) ]
            valency = [ 0 for i in range(0, v) ]
            for i in range(0, a):
                c1, c2 = [int (x) for x in sys.stdin.readline().split()]
                connect(components, c1, c2, valency)
                has_edge[c1] = True
                has_edge[c2] = True
            if a == 0:
                print("Not Possible")
            elif have_eulidian_path(components, valency, has_edge, v):
                print("Possible")
            else:
                print("Not Possible")
        except EOFError:
            break
