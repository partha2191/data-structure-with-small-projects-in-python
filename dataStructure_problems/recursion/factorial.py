# def factorial (num):
#     num4 = 1
#     if num == 0:
#         print(num)
#     if num >= 2:
#         num3 = num # 4
#         num4 = num4 * num
#         while num3 > 1:
#             num3 = num3 - 1 # 3 2 1
#             num2 = num3
#             num4 = num4 * num2
#         print(num4)

# factorial(int(input("Enter the number: ")))

def RecFactorial (n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * RecFactorial(n-1))
    

Result = RecFactorial(int(input("Enter the number: ")))
print(Result)