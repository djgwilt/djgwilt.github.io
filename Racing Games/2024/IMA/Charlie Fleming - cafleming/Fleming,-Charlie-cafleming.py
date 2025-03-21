# Feedback for Fleming,-Charlie-cafleming
# Challenge c02.py
# Student Fleming,-Charlie-cafleming 
# Auto [5]

########################################
# ALL THE CODE YOU NEED IS HERE. THE INSTRUCTIONS FOLLOW

# All the lines of code that you need are below, 
# but with no indentation and not in the correct 
# order. You will need to replace the ?? with code.
# Use Alt + Arrow keys to re-order the lines, moving them
# into the 'Main Program' space below.


##########################################
# Main Program
##########################################
# ==> Allow the user to enter a numerator and a denominator 
#     as two separate whole numbers, in that order. 

print("Enter a numerator and denominator on two separate lines in that order")

num = int(input("enter numerator: "))
den = int(input("enter denominator: "))

# ==> If the denominator is zero, print 'Infinity' 
if den == 0:
  print("Infinity")
    
# ==> Otherwise, if the numerator and denominator are 
#     the same, then print the word 'One' 

elif num == den:
  print("One")

# ==> For all other cases, print the numerator divided 
#     by the denominator, rounded to two decimal places. 

else:
  frac = num / den
  print("{:.2f}".format(frac))

########################################
# Challenge c03.py
# Student Fleming,-Charlie-cafleming 
# Hand-marked below
########################################
# ==> Create the variable called 'data' as an empty list [1]
data = []

# Choose the correct next line to allow the user to enter a whole number. 
# ==> Uncomment one line only. [1]
amount = int(input("How many words will you enter?"))
#amount = float(input("How many words will you enter?"))

# ==> Fill in the ?? to create a loop that will run 'amount' number of times [1]
for count in range(0,amount,1):

# ==> Inside the loop, ask the user to 'enter a word' and add the number of 
#     letters in the word to the end of the list called 'data' [3]
  word = input("Enter a word:")
  num_letters = len(word)
  data.append(num_letters)


# The longest word can be found with the python code 'max(data)'. 
longest = max(data)

# ==> Change the ?? in the format-string below so that after the loop, 
#     the length of the longest word is printed [1]
print("The longest word has length {}".format(longest))

########################################
