
sub1 = int(input("Enter sub1 marks="))
sub2 = int(input("Enter sub2 marks="))
sub3 = int(input("Enter sub3 marks="))

def avg_marks(sub1,sub2,sub3):
    avg = (sub1 + sub2 + sub3) / 3
    return avg

avg  = avg_marks(sub1,sub2,sub3)

if avg >= 90:
    print("Grade of student = A")
elif avg >= 80 and avg < 89 :
    print("Grade of student = B")
elif avg >= 70 and avg < 79 :       
    print("Grade of student = C")
elif avg >= 60 and avg < 69 :       
    print("Grade of student = D")    
else:
     print("Student failed in exam")    