# Program to display the Fibonacci sequence up to n-th term

number = int(input("What number do you want to get a fibonacci sequence for? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number is valid
if number <= 0:
   print("Please enter a positive integer")
elif number == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < number:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1