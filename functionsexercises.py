# # def add_calc(number1, number2):
# #     answer = number1 + number2
# #     return answer

# # added_number = add_calc(5,5)
# # print(added_number + 20)


#1.  #create a program that works out a grade based on marks with the use of functions.
# #asl students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs
# #output their name and final ICT grade as a percentage.


# def ICTGrade(h, a, e):
#     ICTPercentage = (h*a*e)*100
#     return ICTPercentage

# student_name = input("What is your name? ")
# homework_score = int(input("Enter homework score /25 "))/25
# assessment_score = int(input("Enter assessment score /50 "))/50
# exam_score = int(input("Enter exam score /100 "))/100

# var1 = ICTGrade(homework_score, assessment_score, exam_score)
# print(student_name + "'s ICT Final Percentage is: ", var1)

# if var1 > 90:
#     print(student_name + " passed --A--")
# elif var1 > 80:
#     print(student_name + " passed --B--")
# elif var1 > 75:
#     print(student_name + " passed --C--")
# elif var1 > 70:
#     print(student_name + " passed --D--")
# elif var1 > 59:
#     print(student_name + " passed --E--")
# else:
#     print(student_name + " Failed --F--")


#2. Write a Python function to find the Max of three numbers

# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))



#3 
##Write a Python function to sum all the numbers in a list
#sample List : (8, 2, 3, 0, 7)

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))



#4 
#Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)

# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((8, 2, 3, -1, 7)))



#5
# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"

# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))



#6
#Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument.

# def fact(n):

#     f = 1

#     for i in range(1, n+1) :
#         f = f*i
#     return f

# x = 5

# result = fact(x)

# print(result)

#or to make you insert a number : 

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))


#7 
#Write a Python function to check whether a number falls in a given range

# def test_range(n):
#     if n in range(2,8):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(3)