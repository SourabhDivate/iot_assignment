
num = int(input("Enter a number:"))

def fact(num):
    temp = 1
    while(num !=0):
         temp = temp  * num
         num = num - 1
    return temp

f = fact(num)
print(f"Factorial of {num} = {f}")     