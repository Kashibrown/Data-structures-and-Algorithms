#An algorithm to find the largest amongst three numbers for single digits
number = input("Enter 3 different number: ")
a = [ i for i in number ]
if a[0] > a[1]:
    if a[0] > a[2]:
        print(f'{a[0]} is the greater number')
    else:
        print(f'{a[2]} is the greater number')
else:
    if a[1] > a[2]:
        print(f'{a[1]} is the greater number ')
    else:
        print(f'{a[2]} is the greater number') 
        
        #OR this if our user wants to enter 2 digits or more 
        
number = input("Enter 3 different number and pls add a comma: ")
num = list(number.split(","))
if num[0] > num[1]:
    if num[0] > num[2]:
        print(f'{num[0]} is the greater number')
    else:
        print(f'{num[2]} is the greater number')
else:
    if num[1] > num[2]:
        print(f'{num[1]} is the greater number')
    else:
        print(f'{num[2]} is the greater number') 



