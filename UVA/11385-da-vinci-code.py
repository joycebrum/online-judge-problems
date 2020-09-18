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


#------------------------
fib_index = {}
fib = [-1]*128

fib[0] = 1
fib[1] = 2
fib_index['1'] = 1
fib_index['2'] = 2

def get_fib(n):
    global fib
    if fib[n-1] < 0:
        fib[n-1] = get_fib(n-1) + get_fib(n-2)
        fib_index[str(fib[n-1])] = n
    return fib[n-1]
get_fib(128)


def clean_msg(msg):
    result = ''
    for c in msg:
        if c < 'A' or c > 'Z': continue
        result += c
    return result

def decode(msg, fib_numbers):
    global actual_fib_index
    result = [' ']*128
    pos = 0
    cleaned = clean_msg(msg)
    last_pos = 0
    
    for f in fib_numbers:
        res_pos = fib_index[f]
        if res_pos > last_pos:
            last_pos = res_pos
        result[res_pos-1] = cleaned[pos]
        pos += 1
    return ''.join(result[0:last_pos])
if __name__ == '__main__':
    test_cases = int(input().strip())

    for i in range(0, test_cases):
        n = int(input().strip())
        fib_numbers = input().strip().split()
        msg = input().strip()
        print(decode(msg, fib_numbers))

#------------------------ não mandar essa parte
"""    
sys.stdout = orig_stdout
f.close()
"""
sys.stdin = orig_stdin
fi.close

#------------------------
