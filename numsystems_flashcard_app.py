import tkinter as tk
from tkinter import ttk
import random

def convert_to_decimal(num, base):
    return int(num, base)

def generate_number(base):
    if base == 2:
        return bin(random.randint(1, 255))[2:]  # Generate random binary number
    elif base == 16:
        return hex(random.randint(1, 255))[2:].upper()  # Generate random hexadecimal number

def show_solution(num, base):
    result = convert_to_decimal(num, base)
    steps = f"({num}){base} = ({result})10\n\n"
    steps += "Step by step solution\n\n"
    steps += f"Step 1: Write down the number:\n\n({num}){base}\n\n"
    steps += f"Step 2: Show each digit place as an increasing power of {base}:\n\n" + ' + '.join(f'{digit}*{base}^{idx}' for idx, digit in enumerate(reversed(num))) + "\n\n"
    steps += "Step 3: Convert each digit values to decimal values then perform the math:\n\n" + ' + '.join(f'{int(digit, base)}*{base**idx}' for idx, digit in enumerate(reversed(num))) + f" = ({result})10\n\n"
    return steps

def check_answer():
    user_answer = answer_entry.get()
    correct_answer = convert_to_decimal(current_number.get(), bases[current_base.get()])
    if int(user_answer) == correct_answer:
        solution_text = "Correct! Well done.\n\n"
    else:
        solution_text = "Incorrect. Try again!\n\n"
    solution_text += show_solution(current_number.get(), bases[current_base.get()])
    solution_label.config(text=solution_text)

def new_number():
    num = generate_number(bases[current_base.get()])
    current_number.set(num)
    solution_label.config(text="")

# Set up the main window
root = tk.Tk()
root.title("Number System Flashcard App")

# Dropdown menu for selecting the base
current_base = tk.StringVar(value="Hexadecimal")
bases = {"Binary": 2, "Hexadecimal": 16}
base_menu = ttk.Combobox(root, textvariable=current_base, values=list(bases.keys()))
base_menu.grid(column=0, row=0, padx=10, pady=10)

# Button to generate a new number
new_number_button = ttk.Button(root, text="New Number", command=new_number)
new_number_button.grid(column=1, row=0, padx=10, pady=10)

# Label to show the current number
current_number = tk.StringVar()
number_label = ttk.Label(root, textvariable=current_number)
number_label.grid(column=0, row=1, padx=10, pady=10)

# Entry for the user's answer
answer_entry = ttk.Entry(root)
answer_entry.grid(column=0, row=2, padx=10, pady=10)

# Button to check the answer
check_button = ttk.Button(root, text="Check Answer", command=check_answer)
check_button.grid(column=1, row=2, padx=10, pady=10)

# Label to show the solution
solution_label = ttk.Label(root, text="", wraplength=400)
solution_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Start the application
new_number()  # Generate the first number
root.mainloop()
