def get_quant(char, linhas):
    count = 0
    for l in linhas:
        count += l.count(char)
    return count

def win(player, linhas):
    for l in linhas:
        if l.count(player) == 3:
            return True
    for i in range(0,3):
        if linhas[0][i] == player and linhas[0][i] == linhas[1][i] and linhas[1][i] == linhas[2][i]:
            return True
    if linhas[1][1] == player:
        if linhas[0][0] == linhas[1][1] and linhas[1][1] == linhas[2][2]:
            return True
        if linhas[0][2] == linhas[1][1] and linhas[1][1] == linhas[2][0]:
            return True
    return False
    
    
def valid_board(linhas):
    xq = get_quant('X', linhas)
    oq = get_quant('O', linhas)
    if xq - oq < 0 or xq - oq > 1:
        return False
    if win('O', linhas) and xq != oq:
        return False
    if win('X', linhas) and xq == oq:
        return False
    return True

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(0, n):
        l1 = input().strip()
        while not l1:
            l1 = input().strip()
        l2 = input().strip()
        l3 = input().strip()
        if valid_board([l1,l2,l3]):
            print('yes')
        else:
            print('no')
