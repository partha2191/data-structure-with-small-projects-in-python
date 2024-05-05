# How to interchange first and last elements in a list in python

numberList = [1,2,3,4]

# Traditional Method

# def list(n):
#     temp = numberList[0]
#     n[0] = numberList[len(numberList)-1]
#     numberList[len(numberList)-1] = temp
#     print(numberList)
# list(numberList)

# Only works in python
numberList[0],numberList[len(numberList)-1] = numberList[len(numberList)-1], numberList[0]
print(numberList)