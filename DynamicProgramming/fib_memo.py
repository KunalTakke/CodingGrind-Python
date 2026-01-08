def fib_memo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1 
    if not(n in memo):
        memo[n] = fib_memo(n-1,memo)+fib_memo(n-2,memo)
    return memo[n]
 
def fib_bottom_up(n):
    table = [0,1]
    for i in range(2,n+1):
        table.append(table[i-1]+table[i-2])
        print(table)
    return table[n-1]

# my_dict = {}
# print(fib_memo(6,my_dict))

print(fib_bottom_up(6))