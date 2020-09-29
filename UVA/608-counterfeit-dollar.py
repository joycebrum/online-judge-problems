not_defined = "NA"
coin_range = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

def check_sides_and_results(coins, coin, result, coins_mem):
    if coin in result[0] and coins_mem[coin]['side'] == 'R':
        if result[2] in coins_mem[coin]['result']:
            coins.remove(coin)
    elif coin in result[1] and coins_mem[coin]['side'] == 'L':
        if result[2] in coins_mem[coin]['result']:
            coins.remove(coin)

def is_opositive(result1, result2):
    if ('up' in result1 and 'down' in result2) or ('down' in result1 and 'up' in result2):
        return True
    return False

def remove_all_except(coins, coin):
    for obj in coins:
        if obj != coin:
            coins.remove(obj)

def is_any_coin_in_the_side(coins, scale1, scale2): #side 0 para esq e 1 pra dir
    for c1 in scale1[0]:
        if len(coins) == 1: break
        if c1 in coins and c1 in scale2[1] and not is_opositive(scale1[2], scale2[2]): #mudou de lado mas manteve o resultado
            coins.remove(c1)
        if c1 in coins and is_opositive(scale1[2], scale2[2]): #se o resultado inverteu
            if c1 in scale2[0]: #se nao mudou de lado e o resultado inverteu, é verdadeira
                coins.remove(c1)
    for c1 in scale1[1]:
        if len(coins) == 1: break
        if c1 in coins and c1 in scale2[0] and not is_opositive(scale1[2], scale2[2]): #mudou de lado mas manteve o resultado
            coins.remove(c1)
        if c1 in coins and is_opositive(scale1[2], scale2[2]): #se o resultado inverteu
            if c1 in scale2[1]: #se nao mudou de lado e o resultado inverteu, é verdadeira
                coins.remove(c1)

def analyse(coins, results, coins_mem):
    for coin in coin_range:
        for result in results:
            if coin not in coins:
                break
            if 'even' in result[2] and (coin in result[0] or coin in result[1]):
                coins.remove(coin)
            elif 'even' not in result[2]:
                if coin not in result[0] and coin not in result[1]:
                    coins.remove(coin)
                else:
                    check_sides_and_results(coins, coin, result, coins_mem)
            if coins_mem[coin]['side'] == 'N':
                if coin in result[0]:
                    coins_mem[coin]['side'] = 'L'
                    coins_mem[coin]['result'] = result[2]
                if coin in result[1]:
                    coins_mem[coin]['side'] = 'R'
                    coins_mem[coin]['result'] = result[2]
    if len(coins) > 1:
        for result in results:
            if 'even' not in result[2]:
                for result2 in results:
                    if 'even' not in result2[2]:
                        is_any_coin_in_the_side(coins, result, result2)
        
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(0,n):
        coins = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        coins_mem = {'A': {'side': 'N', 'result': 'N'}, 'B': {'side': 'N', 'result': 'N'}, 'C': {'side': 'N', 'result': 'N'}, 'D': {'side': 'N', 'result': 'N'}, 'E': {'side': 'N', 'result': 'N'}, 'F': {'side': 'N', 'result': 'N'}, 'G': {'side': 'N', 'result': 'N'}, 'H': {'side': 'N', 'result': 'N'}, 'I': {'side': 'N', 'result': 'N'}, 'J': {'side': 'N', 'result': 'N'}, 'K': {'side': 'N', 'result': 'N'}, 'L': {'side': 'N', 'result': 'N'}}

        first = sys.stdin.readline().split()
        second = sys.stdin.readline().split()
        third = sys.stdin.readline().split()

        analyse(coins, [first, second, third], coins_mem)

        if len(coins) == 1:
            if ('up' in coins_mem[coins[0]]['result'] and coins_mem[coins[0]]['side'] == 'R') or ('down' in coins_mem[coins[0]]['result'] and coins_mem[coins[0]]['side'] == 'L'):
                print(coins[0], "is the counterfeit coin and it is", 'light' + '.')
            elif ('up' in coins_mem[coins[0]]['result'] and coins_mem[coins[0]]['side'] == 'L') or ('down' in coins_mem[coins[0]]['result'] and coins_mem[coins[0]]['side'] == 'R'):
                print(coins[0], "is the counterfeit coin and it is", 'heavy' + '.')
        else:
            print('Não foi possível descobrir.')


