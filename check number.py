# n = int(input('enter a number'))

# if n % 2 == 0:

#     print("even number")

# else:

#     print("odd number")    


# # check if no is prime or not

# n = int(input("enter a number"))

# count = 0

# for i in range(1, n+1):

#     if n % i == 0 :
#         count += 1

# if count == 2 :
#     print('prime')

# else:

#     print('not prime')


# check if a number is pallindrome or not

n = int(input("enter a number"))

m=n

rev=0

while n > 0 :
    r = n % 10 
    n = n // 10
    rev = rev * 10 + r 

if m ==  rev :
    print("pallindrome")    

else:

    print("not pallindrome")
    

