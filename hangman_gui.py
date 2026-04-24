import random
import tkinter as tk
from tkinter import messagebox

# Word list
words = ["python", "flask", "coding", "developer", "program"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        # Game setup
        self.word = random.choice(words)
        self.guessed_word = ["_"] * len(self.word)
        self.max_wrong = 6
        self.wrong_guesses = 0

        # UI Elements
        self.word_label = tk.Label(root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.info_label = tk.Label(root, text=f"Wrong guesses left: {self.max_wrong}", font=("Arial", 14))
        self.info_label.pack()

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=20)

        self.create_letter_buttons()

    def create_letter_buttons(self):
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, height=2,
                            command=lambda l=letter: self.guess_letter(l))
            btn.grid(row=i // 9, column=i % 9, padx=5, pady=5)

    def guess_letter(self, letter):
        correct = False

        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.guessed_word[i] = letter
                correct = True

        if not correct:
            self.wrong_guesses += 1

        # Update UI
        self.word_label.config(text=" ".join(self.guessed_word))
        self.info_label.config(text=f"Wrong guesses left: {self.max_wrong - self.wrong_guesses}")

        # Disable button after click
        for widget in self.buttons_frame.winfo_children():
            if widget["text"] == letter:
                widget.config(state="disabled")

        # Check win/lose
        if "_" not in self.guessed_word:
            messagebox.showinfo("🎉 You Win!", f"The word was: {self.word}")
            self.reset_game()

        elif self.wrong_guesses >= self.max_wrong:
            messagebox.showerror("💀 You Lose!", f"The word was: {self.word}")
            self.reset_game()

    def reset_game(self):
        self.word = random.choice(words)
        self.guessed_word = ["_"] * len(self.word)
        self.wrong_guesses = 0

        self.word_label.config(text=" ".join(self.guessed_word))
        self.info_label.config(text=f"Wrong guesses left: {self.max_wrong}")

        for widget in self.buttons_frame.winfo_children():
            widget.config(state="normal")


# Run app
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()