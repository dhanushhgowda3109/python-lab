n=int(input("enter the number of student:"))




for i in range(1,n+1):
    sname=input("enter student name:")
    usn=input("enter student usn:")
    sub1=int(input("enter student marks:"))
    sub2=int(input("enter marks:"))
    sub3=int(input("enter marks:"))
    total=sub1+sub2+sub3
    avg=total/3
    print("--------student details-------")
    print("stuent name:",sname)
    print("USN:",usn)
    print("sub1 marks:",sub1)
    print("sub2 marks:",sub2)
    print("sub3 marks:",sub3)
    print("TOTAL:",total)
    print("AVERAGE:",avg)
