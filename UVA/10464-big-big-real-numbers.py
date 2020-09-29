def add(number1, number2):
    decimal_part, carry = add_decimal(number1[1], number2[1])
    int_part, carry = add_int(number1[0], number2[0], carry)
    if carry:
        int_part = str(1) + int_part
        
    int_part, decimal_part = remove_zeroes(int_part, decimal_part)
    return int_part, decimal_part

def add_int(n1, n2, carry):
    if not n1 and not n2:
        return '0', 0
    if not n1 and not carry: return n2, 0
    if not n2 and not carry: return n1, 0
    n1, n2 = n1[::-1], n2[::-1]
    len_n1, len_n2 = len(n1), len(n2)
    res = ''
    for i in range(0, max(len_n1, len_n2)):
        a1, a2 = 0, 0
        if i < len_n1:
            a1 = int(n1[i])
        if i < len_n2:
            a2 = int(n2[i])
        res += str(a1 + a2 + carry)[-1]
        if a1 + a2 + carry > 9:
            carry = 1
        else:
            carry = 0
    return res[::-1], carry

def add_decimal(n1, n2):
    if not n1 and not n2: return '0', 0
    if not n1: return n2, 0
    if not n2: return n1, 0
    rest = ''
    if len(n1)> len(n2):
        rest = n1[len(n2):]
        n1 = n1[0:len(n2)]
    elif len(n2) > len(n1):
        rest = n2[len(n1):]
        n2 = n2[0:len(n1)]
    res, carry = add_int(n1,n2, 0)
    res += rest
    return res, carry    

def get_order_to_sub(number1, number2):
    i1, i2, d1, d2 = number1[0], number2[0], number1[1], number2[1]
    if len(i1) > len(i2): return number1, number2, ''
    elif len(i2) > len(i1): return number2, number1, '-'
    elif i1 > i2: return number1, number2, ''
    elif i2 > i1: return number2, number1, '-'
    n = min(len(d1), len(d2))
    if d1[0:n] > d2[0:n]: return number1, number2, ''
    if d2[0:n] > d1[0:n]: return number2, number1, '-'
    if len(d1) > len(d2): return number1, number2, ''
    else: return number2, number1, '-'

def sub(number1, number2):
    maior, menor, negative = get_order_to_sub(number1, number2)
    #print(maior, '-', menor)
    decimal_part, borrow = sub_decimal(maior[1], menor[1])
    #print('parte inteira', maior[0], '-', menor[0])
    int_part, borrow = sub_int(maior[0], menor[0], borrow)
    
    int_part, decimal_part = remove_zeroes(int_part, decimal_part)
    int_part = set_sign(negative, int_part, decimal_part)
    return int_part, decimal_part

def sub_int(n1, n2, borrow):
    if not n1 and not n2: return '0', borrow
    if not n1 and not borrow: return n2, 0
    if not n2 and not borrow: return n1, 0
    n1, n2 = n1[::-1], n2[::-1]
    len_n1, len_n2 = len(n1), len(n2)
    res = ''
    for i in range(0, max(len_n1, len_n2)):
        a1, a2 = 0, 0
        if i < len_n1:
            a1 = int(n1[i])
        if i < len_n2:
            a2 = int(n2[i])
        #print(a1, a2, borrow)
        if borrow:
            a1 -= 1
            borrow = 0
        if a1 < a2:
            a1 += 10
            borrow = 1
        res += str(a1 - a2)
        #print(res, '\n')
    return res[::-1], borrow

def check_decimal_rest_or_fill_with_zeroes(n1, n2):
    rest = ''
    if len(n1)> len(n2):
        rest = n1[len(n2):]
        n1 = n1[0:len(n2)]
    elif len(n2) > len(n1):
        n1 = n1 + '0'*(len(n2) - len(n1))
    return n1, n2, rest

def sub_decimal(n1, n2):
    if not n1 and not n2: return '0', 0
    if not n2: return n1, 0
    n1, n2, rest = check_decimal_rest_or_fill_with_zeroes(n1, n2)
    #print('parte decimal', n1, '-', n2, '------- rest:', rest)
    res, borrow = sub_int(n1,n2, 0)
    res += rest
    return res, borrow

def clean_entry(number):
    int_part = number[0]
    if len(number) == 1:
        number.append('')
    decimal_part = number[1]
    if int_part.startswith('-'):
        number[0], number[1] = remove_zeroes(number[0][1:], number[1])
        number[0] = '-' + number[0]
    else: number[0], number[1] = remove_zeroes(number[0], number[1])
    return number

def remove_zeroes(integer, decimal):
    i = 0
    while i < len(integer) and integer[i] == '0': i += 1
    if i >= len(integer): integer = '0'
    else:
        integer = integer[i:]

    i = len(decimal)-1
    while i >= 0 and decimal[i] == '0': i -= 1
    if i < 0: decimal = '0'
    else:
        decimal = decimal[:i+1]
    return integer, decimal

def set_sign(negative, integer, decimal):
    if integer != '0' or decimal != '0':
        integer = negative + integer
    return integer

if __name__ == '__main__':
    tests = int(input().strip())
    int_part, decimal_part = '', ''
    for i in range(0, tests):
        line = input().strip().split()
        number1, number2 = clean_entry(line[0].split('.')), clean_entry(line[1].split('.'))
        if number1[0].startswith('-') or number2[0].startswith('-'):
            if number1[0].startswith('-') and number2[0].startswith('-'):
                number1[0] = number1[0][1:]
                number2[0] = number2[0][1:]
                int_part, decimal_part = add(number1, number2)
                int_part = set_sign('-', int_part, decimal_part)
            elif number1[0].startswith('-'):
                number1[0] = number1[0][1:]
                int_part, decimal_part = sub(number2, number1)
            else:
                number2[0] = number2[0][1:]
                int_part, decimal_part = sub(number1, number2)
        else:
            int_part, decimal_part = add(number1, number2)
        print(int_part + '.' + decimal_part)
