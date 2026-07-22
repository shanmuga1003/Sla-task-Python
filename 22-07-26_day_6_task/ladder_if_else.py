#ladder if-else
mark = int(input("Enter your mark to find our grade : "))
if mark <=100 and mark >=91:
    print("S grade")
elif mark <=90 and mark >=81:
    print("A grade")
elif mark <=80 and mark >=71:
    print("B grade")
elif mark <=70 and mark >=61:
    print("C grade")
elif mark <=60 and mark >=51:
    print("D grade")
elif mark <=50 and mark >=40:
    print("E grade")
else:
    print("Fail")
