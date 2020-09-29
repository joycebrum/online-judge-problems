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
