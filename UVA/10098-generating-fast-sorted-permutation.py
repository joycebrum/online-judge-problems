def get_min_greater_than(array, letter):
    value = max(array)
    for c in array:
        if c > letter and c < value:
            value = c
    return value

def get_next_permutation(letters):
    i = len(letters) - 1
    removed = []
    while i >= 0:
        if not removed:
            removed.append(letters.pop())
            i -= 1
            continue

        if max(removed) > letters[i]:
            letter = letters.pop()
            next_l = get_min_greater_than(removed, letter)
            
            removed.remove(next_l)
            letters.append(next_l)
            removed.append(letter)
            
            rest = sorted(removed)
            return letters + rest
        removed.append(letters.pop())
        i -= 1
    return None

def generate_and_print_permutations(letters):
    print("".join(letters))
    while True:
        letters = get_next_permutation(letters)
        if  not letters:
            break
        print("".join(letters))
        
    
if __name__ == '__main__':
    n = int(input().strip())
    for i in range(0, n):
        string = sorted(input().strip())
        generate_and_print_permutations(string)
        print('')
        
