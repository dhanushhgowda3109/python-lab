n = int(input("Enter the number of students: "))
total = 0

for i in range(1, n + 1):
    sname=(input('enter name'))
    usn=input('enter usn')
    s1=input('enter sub1 marks:')
    s2=input('enter sub2 marks')
    s3=input('enter sub3 marks')
total=s1+s2+s3
avg=total/3
print('Total marks:',total)
print('Average marks:',avg)    