a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

max1 = 0

def max(a,b,c):
    
    if a > b:
        if a > c:
            print("a is a greatest number")
            return a
        else:
            print("c is a largest number")
            return c
    else:
        if b > c:
            print("b is a largest number")
            return b
        else:
            print("c is a largest number")            
            return c
            
              

# max(a,b,c)
print(f"lagest among 3 numbers = {max(a,b,c)}")  