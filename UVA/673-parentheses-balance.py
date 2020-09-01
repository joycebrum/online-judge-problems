import sys

def balance(string):
    string = string.replace(" ", '')
    previousLen = len(string)
    if previousLen == 0:
        return "Yes"
    if '(' not in string and ')' not in string and '[' not in string and ']' not in string:
        return "Yes"
    while '(' in string or ')' in string or '[' in string or ']' in string:
        string = string.replace("()", '')
        string = string.replace("[]", '')
        if previousLen == len(string):
            return "No"
        previousLen = len(string)
    return "Yes"

#------------------------ não mandar essa parte
#https://onlinejudge.org/external/6/673.pdf
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
#------------------------

if __name__ == '__main__':
    
    n = int(sys.stdin.readline())
    i = 0
    while i < n:
        entry = sys.stdin.readline()
        print(balance(entry))
        i = i + 1

#------------------------ não mandar essa parte        
sys.stdout = orig_stdout
f.close()
#------------------------
