# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to an integer
height = float(input("Enter your height in feet: "))  # Convert input to a float

# Perform basic operations
birth_year = 2024 - age
height_in_cm = height * 30.48  # Convert height from feet to centimeters

# Display the results
print("Hello, " + name + "!")
print("You were born in the year", birth_year)
print("Your height in centimeters is:", height_in_cm)
