import tkinter as tk
from tkinter import messagebox
import random

choices = ["Sang", "Kaghaz", "Gheichi"]

def play(user_choice):
    ai_choice = random.choice(choices)

    result_text = f"Your choice: {user_choice}\nAI choice: {ai_choice}\n"

    if user_choice == ai_choice:
        result_text += "\nEqual"
    elif (
        (user_choice == "Sang" and ai_choice == "Gheichi") or
        (user_choice == "Kaghaz" and ai_choice == "Sang") or
        (user_choice == "Gheichi" and ai_choice == "Kaghaz")
    ):
        result_text += "\nYou Win!"
    else:
        result_text += "\nYou Lost!"

    result_label.config(text=result_text)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(
    btn_frame,
    text="🪨 Sang",
    width=12,
    command=lambda: play("Sang")
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame,
    text="📄 Kaghaz",
    width=12,
    command=lambda: play("Kaghaz")
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame,
    text="✂️ Gheichi",
    width=12,
    command=lambda: play("Gheichi")
).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()