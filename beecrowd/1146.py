x = int(input())

while x !=0:


    for i in range(1, x+1):

        print(i, end='')

        if i == x:
            print()
        
        else:
            print(' ', end='')
    
    x = int(input())
            
