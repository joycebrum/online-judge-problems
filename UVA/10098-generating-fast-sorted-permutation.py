import sys
from datetime import datetime
#------------------------ não mandar essa parte

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
"""
orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
"""
#------------------------
choosed = []

def deep_recursion(n, perm, string):
    if n >= len(string):
        print(perm)
        return 
    for c in string:
        if not choosed[c]:
            choosed[c] = True
            deep_recursion(n+1, perm + c, string)
            choosed[c] = False

def generate_and_print_permutations(string):
    global choosed
    choosed = {}
    for c in string:
        choosed[c] = False
    deep_recursion(0, '', string)
    
if __name__ == '__main__':
    n = int(input().strip())
    for i in range(0, n):
        #init = datetime.now()
        string = input().strip()
        generate_and_print_permutations(string)
        print('')
        #now = datetime.now()
        #print('time =', (now-init))
        
#------------------------ não mandar essa parte

sys.stdout = orig_stdout
f.close()

"""
sys.stdin = orig_stdin
fi.close
"""
#------------------------
