

l1 = [1,2,3,4,5,6,7,8,9,10]

def fact(num):
    temp = 1
    while(num !=0):
         temp = temp  * num
         num = num - 1
    return temp
    

for num in l1:
    f = fact(num)
    print(f"Factorial of {num} = {f}")  
    
  