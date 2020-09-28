import sys


#------------------------ não mandar essa parte
""""""
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi

#------------------------           

def get_carry_operations(first, second):
    first = first[::-1]
    second = second[::-1]
    carries = 0
    last_carry = 0
    i = 0
    
    while True:
        if i < len(first) and i < len(second):
            if int(first[i]) + int(second[i]) + last_carry > 9:
                last_carry = 1
                carries += 1
            else:
                last_carry = 0
        elif i < len(first) and last_carry > 0:
            if int(first[i]) + last_carry > 9:
                last_carry = 1
                carries += 1
            else:
                last_carry = 0
        elif i < len(second) and last_carry > 0:
            if int(second[i]) + last_carry > 9:
                last_carry = 1
                carries += 1
            else:
                last_carry = 0
        else: break
        i+=1
    return carries

if __name__ == '__main__':
    while True:
        numbers = input().strip().split()
        if int(numbers[0]) == 0 and int(numbers[1]) == 0: break
        carries = get_carry_operations(numbers[0], numbers[1])
        if carries == 0:
            print('No carry operation.')
        elif carries == 1:
            print('1 carry operation.')
        else:
            print(carries, 'carry operations.')

#------------------------ não mandar essa parte
""""""
sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close

#------------------------
