import sys


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=342
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------

def clean(string):
    string = string.upper()
    return string

def is_reverse(char1, char2):
    if char1 == char2 and char1 in ['A', 'H', 'I','M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']:
        return True
    if (char1 == 'E' and char2 == '3') or (char1 == '3' and char2 == 'E'):
        return True
    if (char1 == 'J' and char2 == 'L') or (char1 == 'L' and char2 == 'J'):
        return True
    if (char1 == 'S' and char2 == '2') or (char1 == '2' and char2 == 'S'):
        return True
    if (char1 == 'Z' and char2 == '5') or (char1 == '5' and char2 == 'Z'):
        return True
    if (char1 == 'J' and char2 == 'L') or (char1 == 'L' and char2 == 'J'):
        return True
    return False
def is_mirroed(string):
    reversed_string = string[::-1]
    pos = 0
    for c in reversed_string:
        if is_reverse(c, string[pos]):
            pos += 1
        else:
            return False
    return True
            

def is_palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

if __name__ == '__main__':
    
    while True:
        entry = sys.stdin.readline()
        if not entry:
            break
        entry = entry.replace("\n", '')
        cleaned_entry = clean(entry)
        palindrome = is_palindrome(cleaned_entry)
        mirroed = is_mirroed(cleaned_entry)
        if palindrome and mirroed:
            print(entry, "-- is a mirrored palindrome.\n")
        elif palindrome:
            print(entry, "-- is a regular palindrome.\n")
        elif mirroed:
            print(entry, "-- is a mirrored string.\n")
        else:
            print(entry, "-- is not a palindrome.\n")

#------------------------ não mandar essa parte
        
sys.stdout = orig_stdout
f.close()


sys.stdin = orig_stdin
fi.close
#------------------------
