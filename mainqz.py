import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from dataqz import quiz_data

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1
    if current_question < len(quiz_data):
        show_question()                                                                              #If all questions have been answered,
    else:
        next_btn.config(state="disabled")
        global score   
        messagebox.showinfo("Quiz completed!" , "No of correct questions: {}/{}".format(score, len(quiz_data)))
        score = int(score / len(quiz_data) * 100)                                                      #display the final score and end the quiz              
        messagebox.showinfo("Quiz Completed!" , f"Percentage Obtained:{score}%")


#app main window
root = tk.Tk()
root.title("Quiz Proctor")
style = Style(theme="darkly")               #flatly,cybrog,pulse,darkly,vapor

#Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(root,command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label = ttk.Label(root,anchor="center",padding=10)
feedback_label.pack(pady=10)

score = 0

# Create the score label
score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10)
score_label.pack(pady=10)

next_btn = ttk.Button(root,text="Next", command=next_question, state="disabled")
next_btn.pack(pady=10)

# starting the app
current_question = 0

show_question()

root.mainloop()