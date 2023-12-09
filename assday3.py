

# if else statement
  
# The if-else statement is used to execute both the true part and the false part of a given condition.
# If the condition is true, the if block code is executed and if the condition is false, the else block
# code is executed.

# example

# a= 50
# b= 80
# if a> b:
#    print("a is greater than b")
# else:
#    print("a is less than b")


# while loop

#   A while loop is a control flow statement which allows code to be executed repeatedly, depending on whether 
# a condition is satisfied or not.As long as some condition is true, 'while' repeats everything inside the
# loop block. It stops executing the block if and only if the condition fails.

# example

x= 1
while x < 5:
   print(x)
   x += 1
#  for loop

#    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set,
# or a string).

# example for list

fruits= ["banana", "apple", "orange"]
for x in fruits:
   print(x)

# example for tuple

colors= ("red", "blue", "pink")
for c in colors:
   print(c)



# while count
#    a "while count" can be achieved using a while loop. a while loop as explained above allows you to repeat
# a block of of code until a certain condition is no longer True

# example

count= 0 
while count <5:
   print("is less than 5")
   count += 0


# in this example, the code inside the while loop will run as long as the count is less than 5.


# nested dictionary
#       A nested dictionary is a dictionary inside a dictionary. It's a collection of dictionaries
#  into one single dictionary.

# example

phones= {"infinix": ["model hot7", "storage 32GB", "RAM 16GB"], 
          "samnsung": ["model galaxy s9+", "storage 64GB", "RAM 32GB"],
         "Nokia": ["model note 7",  "storage 124GB", "RAM 64GB"]}

print(phones)


