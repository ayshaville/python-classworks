# 1: Explain the for statement and give 3 example using the for statement
# 2: Create 3 different set of codes using the def and lambda function each (make each one with string,
#  integers/floats, list respectively)
# 3: Finish up the assignment 1, 2, 3, 4
# for statement

# A for statement is a control flow statement that is used to repeatedly execute a group of statements 
# as long as the condition is satisfied. Such a type of statement is also known as an iterative statement.

# example 1

food= ["fries", "rice", "potatoe", "pasta"]
for x in food:
    print(x)


# example 2

for num in range(1, 6):
    print(num)

# in the example above, the 'for loop' iterates over a range of numbers from 1 to 5. the varriable 'num'
# takes on the value of each iteration, and it is printed out.

# example 3

message= "hello, aysha"
for x in message:
    print(x)

# in the example i gave here also, the 'for loop' iterates over each letter in the string 'message'.
# the variable 'x' takes on the value of each letter in each iteration, and its printed out.


# funtion
# A function is a block of code which only runs when it is called.

# defining a function using def (using int)

def add_numbers(num1, num2):
    sum= num1+num2
    return sum
result= add_numbers(10,7)
print('sum', result)

# (using string)

def comment():
    print("this building is very tall")
comment()


# defining a funtion using lambda (int)

y= lambda a, b, c: a+b+c
print(y(8,1,5))


# (using list)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
filtered_result= filter (lambda n: n < 8, numbers)
print(list(filtered_result))
