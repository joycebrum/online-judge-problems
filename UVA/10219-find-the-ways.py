import sys
from datetime import datetime


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=56
"""
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
"""
#------------------------

pot = [pow(10, x) for x in range(20)]
if __name__ == '__main__':
    while True:
        test = sys.stdin.readline().strip().split()
        if not test or len(test) < 2: break
        n = int(test[0])
        k = int(test[1])

        decimals = 1
        ways = 1
        init = datetime.now()
        
        for i in range(0, k):
            """ways = ways * ((n - i)/(k-i));
            places = len(str(int(ways)))
            if places > 2:
                ways = ways / pot[places-1]
            decimals += places"""
            a = 5
        print("Time", datetime.now() - init)
        print(decimals)
#------------------------ não mandar essa parte
"""
sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close
"""
#------------------------
