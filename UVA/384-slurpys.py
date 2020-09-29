def is_slump(string, pos):
    if pos >= len(string): return False, -1
    if string[pos] != 'D' and string[pos] != 'E':
        return False, -1

    pos += 1
    f_count = 0
    while pos < len(string) and string[pos]== 'F':
        f_count += 1
        pos += 1
    if f_count == 0:
        return False, -1

    if pos >= len(string): return False, -1
    if string[pos] == 'G':
        return True, pos+1
    return is_slump(string, pos)

def is_slimp(string, pos):
    if pos >= len(string): return False, -1
    if string[pos] != 'A' or pos+1 >= len(string): return False, -1

    pos += 1
    if string[pos] == 'H': return True, pos+1

    if string[pos] == 'B':
        pos += 1
        slimp, pos = is_slimp(string, pos)
        if slimp and pos < len(string) and string[pos] == 'C':
            return True, pos+1
    else:
        slump, pos = is_slump(string, pos)
        if slump and pos < len(string) and string[pos] == 'C':
            return True, pos+1
    return False, -1
        
    

def is_slurpy(string):
    slimp, pos = is_slimp(string, 0)
    if not slimp: return False

    slump, pos = is_slump(string, pos)
    if not slump: return False

    if pos >= len(string): return True
    return False

if __name__ == '__main__':
    test_cases = int(input())
    print('SLURPYS OUTPUT')
    for i in range(0, test_cases):
        string = input()
        string = string.strip().upper()
        if is_slurpy(string):
            print('YES')
        else:
            print('NO')
    print('END OF OUTPUT')
