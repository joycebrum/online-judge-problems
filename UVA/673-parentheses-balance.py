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

if __name__ == '__main__':
    
    n = int(sys.stdin.readline())
    i = 0
    while i < n:
        entry = sys.stdin.readline()
        print(balance(entry))
        i = i + 1

