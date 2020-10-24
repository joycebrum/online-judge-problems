class Node:
    def __init__(self, value=0, root=False, sons=[], fathers=[], has_path=False):
        self.value = value
        self.root = root
        self.sons = sons
        self.fathers = fathers
        self.has_path = has_path

    def __repr__(self):
        return 'value: %s, sons = %s, fathers = %s' % (self.value, self.sons, self.fathers)

def quant_root(nodes):
    roots = 0
    for node in nodes:
        if len(nodes[node].fathers) == 0:
            nodes[node].root = True
            roots += 1
    return roots

def any_node_has_more_than_one_father(nodes):
    for node in nodes:
        if len(nodes[node].fathers) > 1:
            return True
    return False

def find_paths(nodes, node):
    for son in nodes[node].sons:
        if nodes[son].has_path:
            return False #possui ciclo
        nodes[son].has_path = True
    for son in nodes[node].sons:
        find_paths(nodes, son)
    return True
        
def path_from_root(nodes, root):
    if not find_paths(nodes, root):
        return False
    for node in nodes:
        if not nodes[node].root and not nodes[node].has_path:
            return False
    return True
    

def root(nodes):
    for node in nodes:
        if nodes[node].root:
            return node
    return ''

def is_it_a_tree(nodes):
    if not nodes: return True
    if quant_root(nodes) != 1 or any_node_has_more_than_one_father(nodes):  
        return False
    return path_from_root(nodes, root(nodes))

def process_entry(nodes, line):
    i = 0
    while i + 1 < len(line):
        if line[i] + line[i+1] == 0:
            return True
        update_nodes(nodes, str(line[i]), str(line[i+1]))
        i += 2
    return False

def update_nodes(nodes, father, son):
    if father not in nodes:
        nodes[father] = Node(int(father), False, [], [])
    if son not in nodes:
        nodes[son] = Node(int(son), False, [], [])
    nodes[father].sons.append(son)
    nodes[son].fathers.append(father)
    
if __name__ == '__main__':
    nodes = {}
    k = 1
    while True:
        line = input().split()
        if not line: continue
        line = [int(x) for x in line]
        if line[1] < 0 and line[0] < 0:
            break
        
        if process_entry(nodes, line):
            if is_it_a_tree(nodes):
                print('Case', k, 'is a tree.')
            else:
                print('Case', k, 'is not a tree.')
            k += 1
            nodes.clear()
