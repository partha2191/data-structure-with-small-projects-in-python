# def fibonnaci(num):
#     num1 = 0
#     num2 = 1
#     num3 = num1
#     if num < 0:
#         print('null')
#     elif num == 0:
#         print(num)
#     elif num > 0:
#         for i in range (num): 
#             print(num3, end=" ")
#             num1, num2 = num2, num3
#             num3 = num1 + num2``

# fibonnaci(int(input("Enter the number to see the series: ")));

def RecFibonnnaci(n):
    if n > 1:
        return (RecFibonnnaci(n-1) + RecFibonnnaci(n-2))
    else:
        return n
    

result = int(input("Enter the number to see the series: "))

for i in range(result):
    print(RecFibonnnaci(i))
