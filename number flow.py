# display multiplication of table for given number

n = int(input("enter a number"))

count = 0

while count <= 10 :
  
  print(n, 'X', count, '=', n * count )

  count = count + 1


#for using for loop 

number = int(input("enter a number"))

for i in range(1,11):
    product = number * i

    print(f"{number} * {i} = {product}")


#counting the number of digits in number

n =  int(input("enter a number"))

count = 0
while n > 0:
    n = n // 10
    count+=1

print(f"number of digits are {count}") 

#sum of digits in a number

n = int(input("enter a number"))

sum=0
while n > 0:
    r = n % 10
   # n = n // 10
    sum = sum + r

print(f"sum of digits of a number {sum}")


# reverse a number

n = int(input('enter a number'))

rev = 0

while n > 0:

    r = n % 10
    n = n //10
    rev = rev * 10 + r

print(f"reverse of a number {rev}")

print(n)


# sum of positive and negative number

no_of_nos = int(input("enter numbers of number"))

psum = 0
nsum = 0
count = 0

while count < no_of_nos:
    n = int(input('enter a number'))

    if (n > 0) :
        
        psum += n

    else:

        nsum += n

    count = count + 1

print(f"positive sum {psum}")

print(f"negative sum {nsum}")
