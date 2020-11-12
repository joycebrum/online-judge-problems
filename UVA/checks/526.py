import sys

#------------------------ não mandar essa parte
orig_stdin = sys.stdin
fi = open('../out.txt', 'r')
sys.stdin = fi

#------------------------

def replace_at(s, i, c):
    return s[:i] + c + s[i+1:]

def insert_at(s, i, c):
    return s[:i] + c + s[i:]

def remove_at(s, i):
    return s[:i] + s[i+1:]

def apply_commands(str1, str2, commands):
    #print(str1)
    for command in commands:
        if command[0] == "Delete":
            str1 = remove_at(str1, int(command[1])-1)
        elif command[0] == "Insert":
            i, c = command[1].split(',')
            str1 = insert_at(str1, int(i)-1, c)
        else:
            i, c = command[1].split(',')
            str1 = replace_at(str1, int(i)-1, c)
        #print(command, str1)
    return str1
            

if __name__ == '__main__':
    first = True
    while True:
        try:
            if not first: input()
            first = False
            
            commands = []
            str1 = input()
            str2 = input()
            #print(str1, str2)
            
            n = int(input())
            for i in range(0, n):
                command = input().split()
                commands.append(command[1:])
            transformed = apply_commands(str1, str2, commands)
            #print(transformed)
            #print(str2)
            #print(transformed == str2)
            if transformed != str2:
                print('Erro na entrada', str1, str2)
        except EOFError:
            break
        
#------------------------ não mandar essa parte

sys.stdin = orig_stdin
fi.close

#------------------------
