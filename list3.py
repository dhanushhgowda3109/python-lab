mixed_list=["red",10,20,"blue",20,]
mixed_1=[]
mixed_2=[]
for item in mixed_list:
    if isinstance(item,(int,float)):
       print(mixed_1.append(item))
    else:
        print(mixed_2.append(item))