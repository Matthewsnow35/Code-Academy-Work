# This activity involved following along to build a magic 8-ball model. This activity involved declaring variables, assigning variables to a string, learned about the .randint() function and used it to generate a random number, used control flow with the use of if, elif and else statements. Finally I utilized the print() statement to print the results.

import random

name = "Matthew"
question = "What color am I thinking about?"
answer = ""

random_number = random.randint(1, 9)
# prints a random number
print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else: 
  answer = "Error"

print(name + " asks: " + question)

print("Magic 8-ball's answer: " + answer)

# Activity Directions:

# 1.) In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
# 2.) Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
# 3.) We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
# 4.) In order for the answer to be different each time we run the program, we will utilize randomly generated values. Note: This will be something new! But don’t worry, we will try to explain this topic thoroughly and also supply the code. In Python, we can use the .randint() function from the random module to generate a random number from a range.But first, let’s import this module so we can use its functions. Add this line of code to the top of magic8.py:
# 5.) Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call: random.randint(1, 9) which will generate a random number between 1 (inclusive) and 9 (inclusive). Next, add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.Once you’re sure this is working as we expected, feel free to comment out this print() statement.
# 6.) Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program! For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely”
# 7.) Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9. Recall that the 9 possible answers of the Magic 8-Ball are: 1 Yes - definitely 2 It is decidedly so 3 Without a doubt 4 Reply hazy, try again 5 Ask again later 6 Better not tell you now 7 My sources say no 8 Outlook not so good 9 Very doubtful
# 8.) Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.
# 9.) Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format: [Name] asks: [Question] For example, when we run the program, the output should look something like:
# 10.)  Add a second print() statement that will output the Magic 8-Ball’s answer in the following format: Magic 8-Ball's answer: [answer]For example, when running the program it should look something like:
# 11.) Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes. Run your program several times to see that it’s working as expected.
