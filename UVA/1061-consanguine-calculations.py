import sys


#------------------------ não mandar essa parte
"""
problema https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3502
"""
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi


#------------------------

def remove_if_contains_char(results, char):
    return list(filter(lambda obj: char not in obj, results))
            
def remove_if_not_contains_char(results, char):
    return list(filter(lambda obj: char in obj, results))

def get_possible_kid(pai, mae):
    results = ['O-', 'O+', 'AB-', 'AB+', 'B-', 'B+','A-', 'A+']
    if '-' in pai and '-' in mae:
        results = remove_if_contains_char(results, '+')
    if 'O' in pai and 'O' in mae:
        results = remove_if_not_contains_char(results, 'O')
    if 'A' not in pai and 'A' not in mae:
        results = remove_if_contains_char(results, 'A')
    if 'B' not in pai and 'B' not in mae:
        results = remove_if_contains_char(results, 'B')
    if 'AB' in pai or 'AB' in mae:
        results = remove_if_contains_char(results, 'O')
    if 'O' in pai or 'O' in mae:
        results = remove_if_contains_char(results, 'AB')
    return results
    

def get_possible_father(pai, filho):
    results = ['O-', 'O+', 'AB-', 'AB+', 'B-', 'B+','A-', 'A+']
    if ('AB' in pai and 'O' in filho) or ('O' in pai and 'AB' in filho): return []
    if '+' in filho and '-' in pai:
        results = remove_if_contains_char(results, '-')
    if 'O' in filho:
        results = remove_if_contains_char(results, 'AB')    
    if 'A' in filho and 'A' not in pai:
        results = remove_if_not_contains_char(results, 'A')
    if 'B' in filho and 'B' not in pai:
        results = remove_if_not_contains_char(results, 'B')
    if 'AB' in pai and 'AB' in filho:
        results = remove_if_contains_char(results, 'O')
    return results
        
        
def get_string(blood_types):
    if len(blood_types) == 0: return "IMPOSSIBLE"
    if len(blood_types) == 1: return blood_types[0]
    string = '{'
    for blood_type in blood_types:
        string += blood_type
        if blood_type != blood_types[-1]:
            string += ', '
    return string + '}'
if __name__ == '__main__':
    i = 0
    blood = []
    while True:
        blood = sys.stdin.readline().split()
        if len(blood) < 3:
            continue
        i += 1
        if blood[0] == 'E' and blood[1] == 'N' and blood[2] == 'D': break
        if blood[2] == '?':
            result = get_string(get_possible_kid(blood[0], blood[1]))
            print('Case', str(i) + ':', blood[0], blood[1], result)
        if blood[0] == '?':
            result = get_string(get_possible_father(blood[1], blood[2]))
            print('Case', str(i) + ':', result, blood[1], blood[2])
        if blood[1] == '?':
            result = get_string(get_possible_father(blood[0], blood[2]))
            print('Case', str(i) + ':', blood[0], result, blood[2])

#------------------------ não mandar essa parte
""" """        
sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close



#------------------------
