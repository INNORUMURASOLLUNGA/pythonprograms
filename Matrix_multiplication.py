a=int(input("Enter the no of rows for Matrix 1: "))

b=int(input("Enter the no of columns for Matrix 1: "))

a1=int(input("Enter the no of rows for Matrix 2: "))

b1=int(input("Enter the no of columns for Matrix 2: "))

#condition for checking the matrix multiplication
if (b==a1):
    mat1=[]
    mat2=[]
    ans=[]
    
    #intilization of the resultant matrix to be zero matrix
    for i in range(a):
        tem=[]
        for j in range(b1):
            v=0
            tem.append(v)
        ans.append(tem)
    
    m=0
    n=0
    
    #getting the values for matrix 1
    
    print("\n")
    print("-------------------Enter the values for Matrix 1-------------------------")
    
    for i in range(a):
        tem=[]
        for j in range(b):
            
            m=int(input("Enter the value {0} for matrix 1:".format(n+1)))
            tem.append(m)
            n=n+1 
        mat1.append(tem)

    
    #printing the values of matrix 1
    
    for r in mat1: 
        print(r)
     
     
    #getting the values for matrix 2  
    
    print("\n\n")
    print("--------------------Enter the values for Matrix 2-------------------------")
        
        
    n=0    
    for i in range(a1):
        tem=[]
        for j in range(b1):
            
            m=int(input("Enter the value {0} for matrix 2:".format(n+1)))
            tem.append(m)
            n=n+1 
        mat2.append(tem)


    #printing the values of matrix 2
    
    print("Matrix-------->2")
    for r in mat2: 
        print(r)
        
        
        
    #doing the multiplication of matrix   
    print("---------------------------Result Matrix-------------------------")
    for i in range(len(mat1)): 
  
        for j in range(len(mat2[0])): 
                
            for k in range(len(mat2)): 
                ans[i][j] += mat1[i][k] * mat2[k][j] 
                    
    #printing the result matrix
    for r in ans: 
        print(r)                
                    
else:
    print("\n")
    print("UNABLE TO DO MATRIX MULTIPLICATION")
            