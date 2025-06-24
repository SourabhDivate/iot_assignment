num = int(input("Enter a 4 digit number:"))

def face_value(num):
  
    a = num

    print("Face value:")

    a = num // 1000
    b = (num //100) %10
    c = (num //10) %10
    d = num % 10
    print(a,b,c,d)


    print("Place value:")
    print(f"num = {a*1000} + {b * 100} + {c * 10} + {d}")
    
    reverse = d *1000 + c * 100 + b * 10 + a
    print(f"reverse = {reverse}")
    
    
face_value(num)    