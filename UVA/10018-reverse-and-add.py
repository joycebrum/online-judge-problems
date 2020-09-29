def is_palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False
def reverse_and_add(number):
    i = 0
    while i < 1000:
        inverse = number[::-1]
        res = int(number) + int(inverse)
        number = str(res)
        i += 1
        if is_palindrome(number):
            break
    return i, number

if __name__ == '__main__':
    tests = int(input())
    for i in range(0, tests):
        number = input()
        iterats, palindrome = reverse_and_add(number)
        print(iterats, palindrome)
