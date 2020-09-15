import sys
from collections import deque 
#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=342
"""orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
"""
orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------

def is_executed(task, executed):
    return task in executed and executed[task]
def has_dependence(task, dependence):
    return task in dependence and dependence[task]

def execute_dependence(current, dependence, execution_order, executed):
    if not has_dependence(current, dependence):
        if not is_executed(current, executed):
            executed[current] = True
            execution_order.append(current)
        return
    while len(dependence[current]) > 0:
        task = dependence[current].popleft()
        if not is_executed(task, executed):
            execute_dependence(task, dependence, execution_order, executed)
    execution_order.append(current)
    executed[current] = True
        
    
if __name__ == '__main__':
    while True:
        entry = input().strip().split()
        n = int(entry[0])
        m = int(entry[1])
        dependence = {}
        if n == 0 and m == 0: break
        for i in range(0, m):
            tasks = input().strip().split()
            if tasks[1] not in dependence:
                dependence[tasks[1]] = deque()
            dependence[tasks[1]].append(tasks[0])
        executed = {}
        execution_order = []
        for i in range(0, n):
            if is_executed(str(i+1), executed):
                continue
            if has_dependence(str(i+1), dependence):
                execute_dependence(str(i+1), dependence, execution_order, executed)
            else:
                execution_order.append(str(i+1))
                executed[str(i+1)] = True
        print(' '.join(execution_order))
#------------------------ não mandar essa parte
"""       
sys.stdout = orig_stdout
f.close()
"""

sys.stdin = orig_stdin
fi.close
#------------------------
