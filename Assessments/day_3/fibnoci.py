#user defined function to find fibnocci series

def fibno(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibno(x-1) + fibno(x-2)
    
#calling function
n=int(input("enter the range to get fibnocci series"))

for i in range(n):
    print(fibno(i),end=", ")