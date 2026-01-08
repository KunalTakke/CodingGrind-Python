# Best Time to Buy and Sell Stock
def bruteForce(prices):
    # prices = [7,1,5,3,6,4]
    # return 0 if no profit, return profit = (buy-sell)

    # edge case: all days same 
    # return 0 

    # edge case: days strictly decreasing  [5,4,3,2,1]
    # return 0 

    maximum_price = max(prices)
    minimum_price  = min(prices)
    # print(f" maximum is {prices.index(maximum_price)}")
    # print(f" minimum is {prices.index(minimum_price)}")

    if maximum_price == minimum_price:
        return 0
    else:
        if prices.index(maximum_price) > prices.index(minimum_price):
            # print(prices.index(maximum_price))
            # print(prices.index(minimum_price))
            return maximum_price - minimum_price
        else:
            return 0



    pass 

def optimized(prices):
    pass 


if __name__ == "__main__":
    tests = []
    test1 = {
        'input':{
            'price':[7,1,5,3,6,4]
        },
        'output': 5
        }
    
    test2 = {
        'input':{
            'price':[7,6,4,3,1]
        },
        'output': 0
        }
    
    tests.append(test1)
    tests.append(test2)

    counter = 1
    for t in tests:
        ans = bruteForce(t['input']['price'])
        if t['output'] == ans:
            print(f"Testcase {counter} Passed")
        else:
            print(f"Testcase {counter} Failed")
            print(f"Your output: {ans} , expected output {t['output']}")
        counter+=1