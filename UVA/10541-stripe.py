import sys


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=342
"""
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
"""

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi


#-----------------------
fat_v = {}

def fat(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    return fat

def get_black_spaces(code):
    res = 0
    for c in code:
        res += int(c)
    return res

if __name__ == '__main__':
    tests = int(input().strip())

    for i in range(0, tests):
        entry = input().strip().split()
        n = int(entry[0])
        k = int(entry[1])
        if k == 0:
            print(1)
            continue
        code = entry[2:]
        black_spaces = get_black_spaces(code)
        extras = n - black_spaces - k + 1
        if extras < 0:
            print(0)
            continue
        elif extras == 0:
            print(1)
            continue
        numerador = fat(k+1)
        denominador = fat(k + 1 - extras)
        print(int(numerador/denominador))
    
        
            

#------------------------ não mandar essa parte
"""        
sys.stdout = orig_stdout
f.close()
"""
sys.stdin = orig_stdin
fi.close

#------------------------
