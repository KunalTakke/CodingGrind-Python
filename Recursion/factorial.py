

def factorial(n):
    if n==0 or n==1:
        return 1
    prev_res = n*factorial(n-1)
    return prev_res
print(factorial(5))
