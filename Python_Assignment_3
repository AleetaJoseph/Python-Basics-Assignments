#1. Set Up the Game: 
# Generate a random number between 1 and 10
 
# import random
# secret_number = random.randint(1, 10)

#Prompt the User: 
# ★ Ask the user to guess the number. 
# ★ Set a variable attempts to 3, which represents the maximum number of guesses allowed.

#attempts = 3

#3. Implement the Guessing Logic: 
# ★ Use a while loop to allow the user to keep guessing until they get the 
# correct number or run out of attempts. 
# ★ Provide feedback to the user for each guess: 
# ➢ If the guess is out of the valid range (1 to 10), inform the user. 
# ➢ If the guess is greater than the secret number. 
# ➢ If the guess is lower than the secret number. 
# ➢ If the guess is correct, congratulate the user and end the game.

# while attempts > 0:
#     guess = int( input("Enter a number from 1 to 10: "))

#     if guess < 1 or guess > 10:
#          print("Your guess is out of valid range(1 to 10)")
#          continue

#     if guess == secret_number:
#         print("Congratulations! You guessed the correct number.")
#         break

#     elif guess > secret_number:
#         print("Too high. Try again.")
#     else:
#         print("Too low. Try again.")

#     attempts -= 1

# else:
#     print("Better luck next time!")


#For Loop:  
#Multiplication Table Generator
#Problem Statement: Create a Python program that generates and prints a 
# multiplication table (from 1 to 10) for a given number using a for loop and the range function. 
# Step wise Instructions: 
# 1. Prompt user for Input. Ask the user to enter a number for which they want to generate a multiplication table. 
# 2. Generate the Multiplication Table: Use a for loop to iterate through the numbers 
# 1 to 10. In each iteration, calculate the product of the user's number and the current number from the loop. 
# 3. Display the Multiplication Table:  Print each line of the multiplication table in the format: "number x i = result".

# number = int(input("Enter the number for which you want the multiplication table: "))

# for i in range(1, 11):
#     result = number * i
#     print(number, "X",i,"=",result)


#Function: 
# BMI Calculator 
# Problem Statement: Create a Python program that calculates the Body Mass Index (BMI). 
# Hint: BMI = weight (kg) / [height (m)]²  
# Instructions: 
# 1. Define a function calculate_bmi(weight, height) that returns the BMI. 
# 2. Prompt the user for their weight (in kg) and height (in meters). 
# 3. Use the function to calculate and display the BMI  
# Sample Output: 
# Enter your weight in kg: 58 
# Enter your height in meters: 1.62 
# Your BMI is: 22.10

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your BMI is:", bmi)
