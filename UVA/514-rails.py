import sys
from collections import deque

#------------------------ não mandar essa parte
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------

def can_permutate(blocks, order):
    station = deque()
    j = 0
    if len(order) < blocks: return False
    for i in range(0, blocks):
        station.append(i+1)
        while len(station)> 0 and int(order[j]) == station[-1]:
            station.pop()
            j += 1
    if len(station)> 0: return False
    return True

if __name__ == '__main__':
    while True:
        blocks = int(sys.stdin.readline().strip())
        if blocks == 0: break
        while True:
            order = sys.stdin.readline().strip().split()
            if order[0] == '0':
                print('')
                break
            can = can_permutate(blocks, order)
            if can: print('Yes')
            else: print('No')

#------------------------ não mandar essa parte
        
sys.stdout = orig_stdout
f.close()


sys.stdin = orig_stdin
fi.close
#------------------------
