# Return the sum of the event numbers in a list

def sumOfNumbers(numbers): # [1,2,4,5,6,7]
    sum = 0
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            sum += numbers[i]
    print(sum)

sumOfNumbers([1,2,3,4,5,6,7,2])
