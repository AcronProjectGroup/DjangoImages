

listOfNumbers = [90, 89, 70, 128]

def MinMaxSumLength(*args):
    global listOfNumbers
    listOfNumbers.sort(reverse=True)
    if len(args) > 0:
        MinNums = min(args)
        MaxNums = max(args)    
        SumNums = sum(args)
        LenNums = len(args)
        return MinNums, MaxNums, SumNums, LenNums

print(MinMaxSumLength(1,2,3,4,5,6))
MinMaxSumLength()
print(listOfNumbers)