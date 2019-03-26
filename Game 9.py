f=[]
import random
z=random.randint(10,40)
for i in range (1,z+1,1):
    f.append(i)
x=len(f)
y=x

while y>0 :
    print(f)
    c=int(input("player-1: How many tokens will you take (1 or 2) ?"))
    if (c == 1):
        a=int(input("Enter your number " ))
        f.remove(a)
        f.insert(a,"")
        y=y-1
        
    elif (c == 2):
        b=int(input("Enter your first num(only the first one ) "))
        f.remove(b)
        f.insert(b-1,"")
        d=b+1
        f.remove(d)
        f.insert(d-1,"")
        y=y-2
    else :
        print("You have lost your turn ! ,You can only choose 1 or 2 so try again in your turn ")
        print(f)    
    if (y==0)and (c==1):
        print("player2 is the winner")
    elif (y==0)and (c==2):
        print ("It's Draw !")
        

    print(f)
    e=int(input("player-2: how many tokens will you take (1 or 2) ?"))
    if (e == 1):
        g=int(input("Enter your num "))
        f.remove(g)
        f.insert(g-1,"")
        y=y-1
        
      
    elif (e == 2):
        h=int(input("Enter the first num (only the first one ) "))
        f.remove(h)
        f.insert(h-1,"")
        j=h+1
        f.remove(j)
        f.insert(j-1,"")
        y=y-2
    else :
        print("You have lost your turn ! ,You can only choose 1 or 2 so try again in your turn  ")    
    
    if (y==0)and (e==1):
        print("player2 is the winner")
    elif (y==0)and (e==2):
        print ("It's Draw !")
        
    
