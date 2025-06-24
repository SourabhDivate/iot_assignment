
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

def avg(a,b,c):
    ans = (a + b + c) // 3
    return ans

ans = avg(a,b,c)
print(f"Avg = {ans}")