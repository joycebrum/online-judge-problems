def list_to_str(list): 
    s = [str(i) for i in list] 
      
    res = " ".join(s) 
      
    return(res) 

def flip(index, pile):
    top = pile[0:index+1][::-1]
    return top + pile[index+1:len(pile)]

def sort_pile(pile):
    max_i = 0
    quant = len(pile)
    position = []
    right_pos = 0
    while quant - right_pos > 0:
        sub_pile = pile[0:quant - right_pos]
        max_i = pile.index(max(sub_pile))
        if max_i >= quant - right_pos - 1:
            right_pos += 1
            continue
        if max_i == 0:
            pile = flip(quant - right_pos - 1, pile)
            position.append(right_pos + 1)
        else:
            pile = flip(max_i, pile)
            position.append(quant - max_i)

            pile = flip(quant - right_pos - 1, pile)
            position.append(right_pos + 1)
        right_pos += 1
    position.append(0)
    return pile, position
        
if __name__ == '__main__':
    
    while True:
        init_pile = sys.stdin.readline().strip()
        if not init_pile: break
        pile = [int(i) for i in init_pile.split()]
        print(init_pile)
        res, position = sort_pile(pile)
        print(list_to_str(position))
