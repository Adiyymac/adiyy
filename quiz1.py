import tkinter as tk
from tkinter import simpledialog, messagebox

# Global variables to track score and current question index
score = 0
current_question = 0

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["Newton", "Einstein", "Galileo", "Tesla"],
        "answer": "Einstein"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Picasso", "Van Gogh", "Da Vinci", "Dali"],
        "answer": "Da Vinci"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "CO2", "H2O", "HO2"],
        "answer": "H2O"
    }
]


# Function to start quiz after login
def start_quiz():
    global score, current_question
    score = 0
    current_question = 0
    display_question()


# Function to display the question and options
def display_question():
    global current_question
    if current_question >= len(questions):
        show_final_score()
        return

    question_data = questions[current_question]
    question_label.config(text=question_data["question"])
    option1_button.config(text=question_data["options"][0], bg="lightgray")
    option2_button.config(text=question_data["options"][1], bg="lightgray")
    option3_button.config(text=question_data["options"][2], bg="lightgray")
    option4_button.config(text=question_data["options"][3], bg="lightgray")
    score_label.config(text=f"Score: {score}")


# Function to check the selected answer
def check_answer(selected_option, button):
    global score, current_question
    correct_answer = questions[current_question]["answer"]

    if selected_option == correct_answer:
        button.config(bg="green")  # Set background to green for correct answer
        score += 5
    else:
        button.config(bg="red")  # Set background to red for incorrect answer

    current_question += 1
    # Wait for 1 second and then display the next question
    quiz_window.after(1000, display_question)





# Function to show the final score
def show_final_score():
    global score
    messagebox.showinfo("Quiz Completed", f"Your final score is: {score}")

    if score >= 20:
        messagebox.showinfo("quiz completed",f"you are winner in this quiz")  # Display the winner message
    else:
        messagebox.showinfo("","you can exit now")

    reset_quiz()


# Function to reset the quiz and go back to login screen
def reset_quiz():
    global score, current_question
    score = 0
    current_question = 0
    name_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    login_screen()


# Function to handle the login screen
def login_screen():
    global score
    login_window.deiconify()  # Show the login window
    quiz_window.withdraw()  # Hide the quiz window


# Function to proceed to the quiz after login
def proceed_to_quiz():
    name = name_entry.get()
    mobile_number = mobile_entry.get()

    if not name or not mobile_number:
        messagebox.showerror("Error", "Please enter both your name and mobile number.")
        return

    # Hide the login window and show the quiz window
    login_window.withdraw()
    quiz_window.deiconify()

    # Set the username on the quiz window
    user_name_label.config(text=f"Welcome {name}!")


# Create the main window for login screen
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("400x300")

# Create the labels and entry fields for the login page
tk.Label(login_window, text="Enter your Name:").pack(pady=10)
name_entry = tk.Entry(login_window, width=30)
name_entry.pack(pady=5)

tk.Label(login_window, text="Enter your Mobile Number:").pack(pady=10)
mobile_entry = tk.Entry(login_window, width=30)
mobile_entry.pack(pady=5)

# Create a button to proceed to the quiz
login_button = tk.Button(login_window, text="Next", command=proceed_to_quiz)
login_button.pack(pady=20)

# Hide the login window initially
login_window.withdraw()

# Create the main window for quiz screen
quiz_window = tk.Toplevel()
quiz_window.title("Quiz Platform")
quiz_window.geometry("500x400")
quiz_window.configure()

# Create a frame to hold the name and score with flex display
info_frame = tk.Frame(quiz_window, bg="black")
info_frame.pack(fill=tk.X, padx=10, pady=10)

# Create a label to display the user's name
user_name_label = tk.Label(info_frame, text="Welcome User!", font=("Arial", 14), fg="white", bg="black")
user_name_label.pack(side=tk.LEFT, padx=10)

# Create a label to display the score
score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 12), fg="white", bg="black")
score_label.pack(side=tk.RIGHT, padx=10)

# Create a label for the question
question_label = tk.Label(quiz_window, text="", font=("Arial", 14), wraplength=400,  fg="black")
question_label.pack(pady=20)

# Create buttons for the answer options
option1_button = tk.Button(quiz_window, text="", width=30,
                           command=lambda: check_answer(questions[current_question]["options"][0], option1_button),
                           bg="lightgray")
option1_button.pack(pady=5)

option2_button = tk.Button(quiz_window, text="", width=30,
                           command=lambda: check_answer(questions[current_question]["options"][1], option2_button),
                           bg="lightgray")
option2_button.pack(pady=5)

option3_button = tk.Button(quiz_window, text="", width=30,
                           command=lambda: check_answer(questions[current_question]["options"][2], option3_button),
                           bg="lightgray")
option3_button.pack(pady=5)

option4_button = tk.Button(quiz_window, text="", width=30,
                           command=lambda: check_answer(questions[current_question]["options"][3], option4_button),
                           bg="lightgray")
option4_button.pack(pady=5)

# Create a button to start the quiz
start_button = tk.Button(quiz_window, text="Start Quiz", command=start_quiz, bg="lightgray")
start_button.pack(pady=20)

# Initially hide the quiz window
quiz_window.withdraw()

# Start the login screen
login_window.deiconify()

# Run the application
login_window.mainloop()
