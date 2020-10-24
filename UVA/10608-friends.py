def find_leader(group, node):
    current = node
    while group[current] != current:
        current = group[current]
    return current

def max_quant_group(quants):
    max_q = 1
    for key in quants:
        if quants[key] > max_q:
            max_q = quants[key]
    return max_q

def insert(group, a1, a2, group_quant):
    if a1 in group or a2 in group:
        if a1 in group and a2 in group:
            leader1, leader2 = find_leader(group, a1), find_leader(group, a2)
            if leader1 == leader2: return
            group_quant[leader1] += group_quant[leader2]
            group[leader2] = leader1
        elif a1 in group:
            leader1 = find_leader(group, a1)
            group[a2] = leader1
            group_quant[leader1] += 1
        elif a2 in group:
            leader2 = find_leader(group, a2)
            group[a1] = leader2
            group_quant[leader2] += 1
    else:
        group[a1] = a1
        group[a2] = a1
        group_quant[a1] = 2

if __name__ == '__main__':
    t = int(input())
    group = {}
    group_quant = {}
    for i in range(0, t):
        n, m = [int(x) for x in input().split()]
        for j in range(0, m):
            a1, a2 = input().split()
            insert(group, a1, a2, group_quant)
        max_q = max_quant_group(group_quant)
        group.clear()
        group_quant.clear()
        print(max_q)

