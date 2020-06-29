a=int(input("enter the rows for matrix 1: "))

b=int(input("enter the columns for matrix 1: "))

a1=int(input("enter the rows for matrix 2: "))

b1=int(input("enter the columns for matrix 2: "))

if(a==a1 and b==b1): #checking the possibility of matrix addition
    mat=0
    x1=[]
    y1=[]
    ans=[]
    
    for i in range(a*b):#getting values for matrix 1
        mat=int(input("enter the  value {0} in matrix 1: ".format(i+1)))
        x1.append(mat)
    w=0
    print("\n")
    print("Matrix --->1")
    for i in range(a):# printing the matrix 1
        for j in range (b):
            print(x1[w],end="\t")
            w=w+1
        print("")
    
    for i in range(a1*b1):# getting values for matrix 2
        mat=int(input("enter the  value {0} in matrix 2: ".format(i+1)))
        y1.append(mat)
    w=0
    print("\n")
    print("Matrix --->2")
    for i in range(a):# printing the matrix 2
        for j in range (b):
            print(y1[w],end="\t")
            w=w+1
        print("")
        
        
    for i in range(a1*b1):#additing matrix
        mat=x1[i]+y1[i]
        ans.append(mat)
    w=0
    print("\n")
    print("Addition of two matrices")
    for i in range(a):# displaying the result
        for j in range (b):
            print(ans[w],end="\t")
            w=w+1
        print("")

else:
    print("Invalid matrix credentials")