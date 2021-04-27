
num = int(input("Enter a nummer: "))
check = True
for i in range(2, num):
    if(num % i == 0):
        print("this is not prime number.")
        check=False
        break  
if (check==True):
    print("this is a prime number")



