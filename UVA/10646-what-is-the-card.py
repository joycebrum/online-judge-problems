import sys


#------------------------ não mandar essa parte
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1587

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
#------------------------

def get_value(card):
    if card[0] >= '2' and card[0] <= '9':
        return int(card[0])
    else:
        return 10

def apply_the_game(cards):
    cards_in_hand = cards[:25]
    remaining = cards[25:]
    y = 0
    for i in range(0,3):
        card = remaining.pop(0)
        x = get_value(card)
        y = y + x
        discard_value = 10 - x
        remaining = remaining[discard_value:]
    new_pile = cards_in_hand + remaining
    return new_pile, y

if __name__ == '__main__':
    
    n = int(sys.stdin.readline())
    i = 0
    while i < n:
        entry = sys.stdin.readline()
        cards = entry.split(' ')
        cards = cards[::-1]
        new_pile, y = apply_the_game(cards)
        print('Case', str(i+1) + ':', new_pile[-y])
        i = i + 1

#------------------------ não mandar essa parte        
sys.stdout = orig_stdout
f.close()
#------------------------

