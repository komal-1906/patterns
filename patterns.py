print("----------Pattern 1----------")
for i in range (1,10):
    for j in range(1,i+1):
        print(j, end = "  ")
    print()
    

print("----------Pattern 2----------")
for i in range (1,10):
    for j in range(1,i+1):
        print("*", end = "  ")
    print()


print("----------Pattern 3----------")
for i in range (1,10):
    for j in range (1,i+1):
        print(i, end = "  ")
    print()


print("----------Pattern 4----------")
for i in range (1,10):
    for j in range (10, i, -1):
        print(i, end = "  ")
    print()


print("----------Pattern 5----------")
for i in range (1,10):
    for j in range (9,i,-1):
        print("  ", end = "  ")
    for k in range (i):
        print("*", end = "  ")
    print()


print("----------Pattern 6----------")
for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end="  ")
    print()
    
    
print("----------Pattern 7----------")
rows = 9
m = (2*rows)-2
for i in range(0, rows):  
        for j in range(0, m):  
            print(end=" ")
        m -= 1 
        for j in range(0, i+1):  
            print("*",end=" ")              

        print()


print("----------Pattern 8----------")
for i in range(1,10):
    for j in range(1, i+1):
        print(i*j, end = "  ")
    print()
    

print("----------Pattern 9----------")
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = "  ")
    print()
for i in range (5, 0, -1):
    for k in range(0, i-1):
        print("*", end = "  ")
    print()


print("----------Pattern 10----------")
rows = 9
num = rows  
for i in range(rows, 0, -1):    
    for j in range(0, i):  
            print(num, end=" ")       
    print()   


print("----------Pattern 11----------")
rows = 9
for i in range(1, rows+1):  
    num = 1 
    for j in range(rows,0,-1):  
      if j > i:
        print(" ", end=" ") 
      else:
        print(num, end=" ")
        num += 1
    print() 
    

print("----------Pattern 12----------")    
rows = 6
num = 1
stop = 2
for i in range(rows):   
        for j in range(1, stop):  
            print(num, end=" ")     
            num += 1  
        print() 
        stop += 2
        
        
print("----------Pattern 13----------")        
rows = 8
x = 1
for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            x = 1
        else:
            x = x * (i - j)//j
        print(x, end = " ")
    print()
    

