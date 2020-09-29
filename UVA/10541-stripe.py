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
