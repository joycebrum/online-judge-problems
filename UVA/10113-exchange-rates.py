import sys

#------------------------ não mandar essa parte
"""
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
"""
orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi

#------------------------
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


class Pair:
    def __init__(self, first, second):
        self.first = int(first)
        self.second = int(second)

    def reduce_using_mdc(self):
        mdc_v = mdc(self.first, self.second)
        self.first = int(self.first/mdc_v)
        self.second = int(self.second/mdc_v)
        
    def __repr__(self):
        return '(%s, %s)' % (self.first, self.second)

def add_proportion(proport, a, itema, b, itemb):
    mdc_v = mdc(int(a),int(b))
    a = int(a)/mdc_v
    b = int(b)/mdc_v
    if itema not in proport: proport[itema] = {}
    if itemb not in proport: proport[itemb] = {}
    proport[itema][itemb] = Pair(a,b)
    proport[itemb][itema] = Pair(b,a)

def get_new_pair(p1, p2):
    x = p1.first * p2.first / p1.second
    if x - int(x) > 0:
        return Pair(p1.first * p2.first, p2.second * p1.second)
    return Pair(x, p2.second)

def find_proportion(proport, current, item, pair, mark):
    if item in proport[current]: return get_new_pair(pair, proport[current][item])
    for key in proport[current]:
        if key not in mark or not mark[key]:
            mark[key] = True
            if not pair:
                ans = find_proportion(proport, key, item, proport[current][key], mark)
            else:
                new_pair = get_new_pair(pair, proport[current][key])
                ans = find_proportion(proport, key, item, new_pair, mark)
            if ans:
                return ans
    return None

def get_proportion(proport, itema, itemb):
    mark = {}
    if itema in proport and itemb in proport[itema]:
        return proport[itema][itemb]
    if itema not in proport or itemb not in proport: return None

    mark[itema] = True
    pair = find_proportion(proport, itema, itemb, None, mark)
    if pair:
        pair.reduce_using_mdc()
    return pair 

if __name__ == '__main__':
    proport = {}
    while True:
        command = input().strip()
        if command == '.': break
        command = command.split()
        
        if command[0] == '!':
            add_proportion(proport, command[1], command[2], command[4], command[5])
        if command[0] == '?':
            answ = get_proportion(proport, command[1], command[3])
            if not answ:
                print('?', command[1], '= ?', command[3])
            else:
                print(answ.first, command[1], '=', answ.second, command[3])
        
        
    
        
#------------------------ não mandar essa parte
"""
sys.stdout = orig_stdout
f.close()
"""

sys.stdin = orig_stdin
fi.close

#------------------------
