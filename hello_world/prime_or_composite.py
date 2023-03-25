#This is my first attempt to write a program


num = int(input("Enter a number: "))

if num in range(0,1+1):
    print(f"{num} is neither prime nor composite number")

else:
    c = 0
    for x in range (1,num + 1): 
        if num % x == 0:
            c += 1
        else:
            pass
    if c == 2 :
        print(f"{num} is a prime number.")

    else:
        print(f"{num} is a composite number.")
