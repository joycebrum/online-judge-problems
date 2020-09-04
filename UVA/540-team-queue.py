import sys
from collections import deque 


#------------------------ não mandar essa parte
#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2619
""" """
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi
#------------------------
teams_q = deque()
teams_description = {}
team_in_queue = {}
queue_per_team = {}

team_being_removed = ''
elements_to_remove = 0

def clear_structures():
    global elements_to_remove, team_being_removed
    teams_q.clear()
    teams_description.clear()
    team_in_queue.clear()
    queue_per_team.clear()
    
    elements_to_remove = 0
    team_being_removed = ''

def dequeue():
    global elements_to_remove, team_being_removed
    if elements_to_remove == 0:
        team_being_removed = teams_q.popleft()
        team_in_queue[team_being_removed] = False
        elements_to_remove = len(queue_per_team[team_being_removed])
    element = queue_per_team[team_being_removed].popleft()
    elements_to_remove -= 1
    return element

def enqueue(element, team):
    if not team_in_queue[team]:
        team_in_queue[team] = True
        teams_q.append(team)
    queue_per_team[team].append(element)

if __name__ == '__main__':
    scenario = 0
    while True:
        teams_number = int(sys.stdin.readline())
        if teams_number == 0: break        
        scenario += 1
        print('Scenario #' + str(scenario))
        clear_structures()
        for i in range(0, teams_number):
            team = sys.stdin.readline().split()
            quant = int(team[0])
            team_in_queue[str(i)] = False
            queue_per_team[str(i)] = deque()
            for j in range(1, quant+1):
                teams_description[team[j]] = str(i)
        while True:
            command = sys.stdin.readline().strip()
            if 'STOP' in command:
                print('')
                break
            if 'ENQUEUE' in command:
                element = command.split()[1]
                team = teams_description[element]
                enqueue(element, team)
            if 'DEQUEUE' in command:
                element = dequeue()
                print(element)
            
#------------------------ não mandar essa parte      
""" """
sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close
#------------------------

