import sys


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=342
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------

def common_permutation(first, second):
    permutation = ''
    j = 0
    n = len(second)
    for i in range(0, len(first)):
        while j < n and second[j] < first[i]:
            j+= 1
        if j >= n: break
        if first[i] == second[j]:
            permutation += first[i]
            j += 1
    return permutation

if __name__ == '__main__':
    
    while True:
        try:
            first = input().strip()
            second = input().strip()
            first = sorted(first)
            second = sorted(second)
            print(common_permutation(first, second))
        except:
            break
    print('')
        

#------------------------ não mandar essa parte
       
sys.stdout = orig_stdout
f.close()


sys.stdin = orig_stdin
fi.close
#------------------------
