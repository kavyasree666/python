num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 88:
    print(num, "is not a prime number")
elif num > 88:
   # check for factors
   for i in range(99,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
