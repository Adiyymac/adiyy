import tkinter as tk

from tkinter import simpledialog

# Create the main window
root = tk.Tk()
root.title("User Input Form")  # Optional: Add a title to the window

# Create a label to display the output
output_label = tk.Label(root, text="Your result will appear here.")
output_label.pack(pady=20)  # Adds space between widgets


# Function to display the output
def display_output(name, mobile_number):
    # Display the input values in the label
    output_label.config(text=f"Hi {name}! Your mobile number is {mobile_number}.")

    # Example logic
    age = 25
    if age > 18:
        output_label.config(text=f"{output_label.cget('text')} You are eligible to vote.")
    else:
        output_label.config(text=f"{output_label.cget('text')} You are not eligible to vote.")

    # Use a list
    fruits = ["Apple", "Orange", "Banana"]
    output_label.config(text=f"{output_label.cget('text')} First fruit in list: {fruits[0]}")

    # Use a dictionary
    person = {"name": "Adiya", "age": 25}
    output_label.config(text=f"{output_label.cget('text')} Name from dictionary: {person['name']}")


# Prompt for name and mobile number
name = simpledialog.askstring("Input", "Enter your name:")
mobile_number = simpledialog.askstring("Input", "Enter your mobile number:")

# Call the function to display the results
display_output(name, mobile_number)

# Keep the window open
root.mainloop()
