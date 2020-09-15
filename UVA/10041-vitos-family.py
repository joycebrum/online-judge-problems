import sys
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


if __name__ == '__main__':
    test_case_number = int(input().strip())
    for i in range(0, test_case_number):
        sums = {}
        test_case = input().strip().split()
        n = int(test_case[0])
        minimum = 2147483647
        for i in range(1, n+1):
            atual = int(test_case[i])
            sums[str(atual)] = 0
            for j in range(1, n+1):
                sums[str(atual)] += abs(atual - int(test_case[j]))
            if sums[str(atual)] < minimum:
                minimum = sums[str(atual)]
        print(minimum)
            
#------------------------ não mandar essa parte
"""       
sys.stdout = orig_stdout
f.close()
"""

sys.stdin = orig_stdin
fi.close
#------------------------
