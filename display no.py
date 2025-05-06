#difference between two number
# no1 = int(input("enter first number"))

# no2= int(input("enter second number"))

# if no1 > no2 :
#     print(no1 - no2)

# else:

#     print(no2 - no1)    


# #check if  a person is male or female

# gender = input("enter gender of a person")

# if gender == 'm' or gender == 'M':

#     print("male")

# elif gender == 'f' or gender == 'F':

#     print("female")    

# else:

#     print("you type wrong letter,please check again")    


#   
# check if a given letter is vowel or consonant

# l= input("enter a letter").lower()

# if l=='a' or  l=='i'  or  l=='o'  or   l =='u'   or  l =='e':

#     print('vowel')

# else:

#     print('consonant')    


#leap year or not

# year=int(input("enter year"))

# if year % 100 ==0 :
#     if year % 400 ==0 :
#         print("leap year")

#     else:

#         print("not leap year")    

# elif year % 4 ==0 : 
#     print("leap year") 

# else:

#     print("not leap year")          


#find calendar


# import calendar

# yy=int(input("enter year"))

# mm=int(input('enter month'))

# print(calendar.month(yy,mm))


# find current date and time

import datetime

now= datetime.datetime.now()

print(f"current date and time {now}")