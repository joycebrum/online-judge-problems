def turn_right(face):
    if face == 'N': return 'E'
    if face == 'E': return 'S'
    if face == 'S': return 'W'
    if face == 'W': return 'N'

def turn_left(face):
    if face == 'N': return 'W'
    if face == 'E': return 'N'
    if face == 'S': return 'E'
    if face == 'W': return 'S'

def can_move_to(maze, i, j, n, m):
    if i >= n or j >= m: return False
    return maze[i][j] != '*'

def move(maze, l, c, f, n, m):
    if f == 'N':
        if can_move_to(maze, l-1, c, n, m): l -= 1
    elif f == 'E':
        if can_move_to(maze, l, c+1, n, m): c += 1
    elif f == 'S':
        if can_move_to(maze, l+1, c, n, m): l += 1
    elif f == 'W':
        if can_move_to(maze, l, c-1, n, m): c -= 1
    return l, c
    
if __name__ == '__main__':
    tests = int(input())
    for t in range(0, tests):
        if t > 0:
            print('')
        input() #blank_line
        maze = []
        n, m = [int(x) for x in input().split()]
        for i in range(0, n):
            maze.append(input())
        l, c = [int(x) - 1 for x in input().split()]
        f = 'N'
        while True:
            line = input()
            for x in line:
                if x == 'R':
                    f = turn_right(f)
                elif x == 'L':
                    f = turn_left(f)
                elif x == 'F':
                    l, c = move(maze, l, c, f, n, m)
                elif x == 'Q':
                    break
            if 'Q' in line:
                print(l + 1, c + 1, f)
                break
