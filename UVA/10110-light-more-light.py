from math import sqrt

def is_on(n):
    root = round(sqrt(n))
    if root * root == n:
        return "yes"
    return "no"

if __name__ == '__main__':
    while True:
        n = int(input().strip())
        if n == 0: break
        print(is_on(n))
