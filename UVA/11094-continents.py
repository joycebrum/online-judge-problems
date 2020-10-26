import sys

LAND = ""

def identifier(i,j):
    return '(' + str(i) +',' + str(j) + ')'

def find_leader(group, node):
    current = node
    if node not in group: return None
    while group[current] != current:
        current = group[current]
    return current

def max_quant_group(group, quants, kingdom):
    max_q = 0
    kingdom_l = find_leader(group, kingdom)
    for key in quants:
        if find_leader(group, key) != kingdom_l and quants[key] > max_q:
            max_q = quants[key]
    return max_q

def insert(a1, a2, group, quant):
    l2 = find_leader(group, a2)
    if a1 in group:
        l1 = find_leader(group, a1)
        if l1 != l2:
            group[l1] = l2
            quant[l2] += quant[l1]
            #del quant[l1]
    else:
        group[a1] = l2
        quant[l2] += 1

def set_relations(i, j, table, group, quant, n, m):
    node = identifier(i,j)
    #add to continent if it is closed to previous land
    if i - 1 >= 0 and table[i-1][j] == LAND:
        insert(node, identifier(i-1, j), group, quant) 
    if j - 1 >= 0 and table[i][j-1] == LAND:
        insert(node, identifier(i, j-1), group, quant)
    if m > 1 and j == m-1 and table[i][0] == LAND:
        insert(node, identifier(i, 0), group, quant)
    #create new continent
    if node not in group:
        group[node] = node
        quant[node] = 1

        

def set_groups(table, l, c, n, m):
    group = {}
    quant = {}
    current = identifier(l,c)
    for i in range(0, n):
        for j in range(0, m):
            if table[i][j] == LAND:
                set_relations(i,j, table, group, quant, n, m)
    return group, quant
    
def get_maximum_continent(table, l, c, n, m):
    group, quant = set_groups(table, l, c, n, m)
    #print(group)
    return max_quant_group(group, quant, identifier(l,c))

if __name__ == '__main__':
    table = []
    while True:
        try:
            entry = sys.stdin.readline().strip()
            if not entry: break
            n, m = [int(x) for x in entry.split()]
            
            for i in range(0, n):
                line = sys.stdin.readline().strip()
                table.append(line)            
            l, c = [int(x) for x in sys.stdin.readline().split()]
            sys.stdin.readline() #empty line
            LAND = table[l][c]
            maximum = get_maximum_continent(table, l, c, n, m)
            print(maximum)
            table.clear()
        except EOFError:
            break

