import sys


#------------------------ não mandar essa parte
#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2619
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------
last_index = [-1]*1000000000

def reset_last_index():
    for i in range(0, len(last_index)):
        last_index[i] = -1


def max_unique_subsequence(snowflakes):
    reset_last_index()
    answer = 0
    i = 0
    for j in range(0, len(snowflakes)):
        index = int(snowflakes[j])
        i = max(i, last_index[index] + 1)
        answer = max(answer, j - i + 1)
        last_index[index]=j
    return answer

if __name__ == '__main__':
    test_case_number = int(sys.stdin.readline())
    for i in range(0, test_case_number):
        snowflakes_number = int(sys.stdin.readline())
        snowflakes = []
        for j in range(0, snowflakes_number):
            snowflakes.append(sys.stdin.readline().strip())
        maximum = max_unique_subsequence(snowflakes)
        print(maximum)
        

#------------------------ não mandar essa parte      
sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close
#------------------------
