class Command:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, command='', pos=-1, value=''):
        self.command = command
        self.pos = pos
        self.value = value

    def __repr__(self):
        if len(self.value) > 0:
            return '%s %s,%s' % (self.command, self.pos, self.value)
        else:
            return '%s %s' % (self.command, self.pos)

def get_commands(commands, x, y):
    path = []
    while True:
        if x < 0 or y < 0: break
        command = commands[x][y]
        if not command:
            x -= 1
            y -= 1
            continue
        if command.command == "Delete":
            x = x-1
        elif command.command == "Insert":
            y = y-1
        else:
            x = x-1
            y = y-1
        path.append(command)
    return path[::-1]
            

def levenshtein(str1, str2):
    tab = []
    commands =[]

    for x in range(0, len(str1)+1):
        tab.append([-1]*(len(str2)+1))
        commands.append( [None] * (len(str2)+1) )
        tab[x][0] = x
        if x > 0:
            commands[x][0] = Command("Delete", x, '')
        
    for y in range(0, len(str2)+1):
        tab[0][y] = y
        if y > 0:
            commands[0][y] = Command("Insert", 1, str2[y-1])

    for x in range(1, len(str1)+1):
        for y in range(1, len(str2)+1):
            if str1[x-1] == str2[y-1]: cost = 0
            else: cost = 1 #Custo da substituição deve ser 1, deleção e inserção

            tab[x][y] = min(tab[x-1][y] + 1, tab[x][y-1] + 1, tab[x-1][y-1] + cost)

            if tab[x][y] == tab[x-1][y] + 1:
                commands[x][y] = Command("Delete", x, '')
            elif tab[x][y] == tab[x][y-1] + 1:
                commands[x][y] = Command("Insert", x+1, str2[y-1])
            else:
                if cost == 0:
                    commands[x][y] = None
                else:
                    commands[x][y] = Command("Replace", x, str2[y-1])
    path = get_commands(commands, len(str1), len(str2))
    return tab[len(str1)][len(str2)], path

def print_commands(commands):
    count = 0
    pos_diff = 0
    for command in commands:
        count += 1
        command.pos += pos_diff
        print(count, command)
        if command.command == "Delete":
            pos_diff -= 1
        if command.command == "Insert":
            pos_diff += 1
        

if __name__ == '__main__':
    count = 0
    while True:
        try:
            str1 = input().strip()
            str2 = input().strip()
            count += 1
            if count > 1:
                print('')
            #print(str1)
            #print(str2)
            distance, commands = levenshtein(str1, str2)
            print(distance)
            print_commands(commands)
        except EOFError:
            break
