import sys

#------------------------ não mandar essa parte

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi

#------------------------

if __name__ == '__main__':=
    n = int(input().strip())
        
#------------------------ não mandar essa parte

sys.stdout = orig_stdout
f.close()


sys.stdin = orig_stdin
fi.close

#------------------------
