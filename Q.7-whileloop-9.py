#7. Write a python script to print first N even natural numbers in reverse order

n=int(input("Enter the number"))
i=1
while i<=n:
    print((n+1)*2-2*i)
    i+=1