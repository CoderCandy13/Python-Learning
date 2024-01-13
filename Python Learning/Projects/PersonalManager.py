import math
import random

def get_user_information():
    print("Welcome to the Personal Information Manager!")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in feet: "))
    is_student = input("Are you a student? (yes/no): ").lower() == 'yes'

    user_info = {
        "Name": name,
        "Age": age,
        "Height (feet)": height,
        "Is Student": is_student
    }

    return user_info

def temperature_checker(temperature):
    if temperature < 0:
        return "It's freezing!"
    elif 0 <= temperature <= 20:
        return "It's a bit chilly."
    else:
        return "It's warm."

def age_calculator(age):
    current_year = 2024
    birth_year = current_year - age
    return f"You were born in the year {birth_year}."

def height_converter(height):
    height_in_cm = height * 30.48
    return f"Your height in centimeters is: {height_in_cm:.2f} cm."

def greet_user(name):
    return f"Hello, {name}!"

def save_to_file(user_info):
    with open("user_info.txt", "w") as file:
        for key, value in user_info.items():
            file.write(f"{key}: {value}\n")

def read_from_file():
    with open("user_info.txt", "r") as file:
        content = file.read()
        return content

def main():
    user_info = get_user_information()

    # Additional features
    temperature = float(input("Enter the current temperature in Celsius: "))
    print(temperature_checker(temperature))
    
    print(age_calculator(user_info["Age"]))
    print(height_converter(user_info["Height (feet)"]))
    
    print(greet_user(user_info["Name"]))

    # Save user information to a file
    save_to_file(user_info)
    print("User information has been saved to 'user_info.txt'.")

    # Read and display user information from the file
    file_content = read_from_file()
    print("\nUser Information from File:")
    print(file_content)

if __name__ == "__main__":
    main()
