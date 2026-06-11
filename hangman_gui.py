import random
import tkinter as tk
from tkinter import messagebox

# Predefined list of words for the game
words = ["python", "flask", "coding", "developer", "program"]

class HangmanGame:
    def __init__(self, root):
        # Initialize main window
        self.root = root
        self.root.title("Hangman Game")

        # ---------------- GAME STATE ----------------
        # Randomly select a word from the list
        self.word = random.choice(words)

        # Create a list of underscores representing hidden letters
        self.guessed_word = ["_"] * len(self.word)

        # Maximum number of wrong guesses allowed
        self.max_wrong = 6

        # Counter for wrong guesses
        self.wrong_guesses = 0

        # ---------------- UI ELEMENTS ----------------
        # Label to display the guessed word (e.g., _ _ _ _)
        self.word_label = tk.Label(root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        # Label to show remaining wrong guesses
        self.info_label = tk.Label(root, text=f"Wrong guesses left: {self.max_wrong}", font=("Arial", 14))
        self.info_label.pack()

        # Frame to hold alphabet buttons
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=20)

        # Create letter buttons (A-Z)
        self.create_letter_buttons()

    def create_letter_buttons(self):
        """
        Create buttons for each alphabet letter and place them in a grid layout.
        """
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(
                self.buttons_frame,
                text=letter,
                width=4,
                height=2,
                command=lambda l=letter: self.guess_letter(l)  # Pass letter to function
            )
            # Arrange buttons in rows and columns
            btn.grid(row=i // 9, column=i % 9, padx=5, pady=5)

    def guess_letter(self, letter):
        """
        Handle logic when a user clicks a letter button.
        """
        correct = False  # Track if guess is correct

        # Check if guessed letter exists in the word
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.guessed_word[i] = letter
                correct = True

        # If incorrect guess, increase wrong guess counter
        if not correct:
            self.wrong_guesses += 1

        # ---------------- UPDATE UI ----------------
        # Update displayed word
        self.word_label.config(text=" ".join(self.guessed_word))

        # Update remaining guesses
        self.info_label.config(
            text=f"Wrong guesses left: {self.max_wrong - self.wrong_guesses}"
        )

        # Disable the clicked button so it can't be reused
        for widget in self.buttons_frame.winfo_children():
            if widget["text"] == letter:
                widget.config(state="disabled")

        # ---------------- CHECK GAME STATUS ----------------
        # Win condition: no underscores left
        if "_" not in self.guessed_word:
            messagebox.showinfo("🎉 You Win!", f"The word was: {self.word}")
            self.reset_game()

        # Lose condition: max wrong guesses reached
        elif self.wrong_guesses >= self.max_wrong:
            messagebox.showerror("💀 You Lose!", f"The word was: {self.word}")
            self.reset_game()

    def reset_game(self):
        """
        Reset the game state and UI for a new round.
        """
        # Select a new word
        self.word = random.choice(words)

        # Reset guessed word display
        self.guessed_word = ["_"] * len(self.word)

        # Reset wrong guess counter
        self.wrong_guesses = 0

        # Update UI labels 
        self.word_label.config(text=" ".join(self.guessed_word))
        self.info_label.config(text=f"Wrong guesses left: {self.max_wrong}")

        # Re-enable all letter buttons
        for widget in self.buttons_frame.winfo_children():
            widget.config(state="normal")


# ---------------- RUN APPLICATION ----------------
# Create main window
root = tk.Tk()

# Initialize game
game = HangmanGame(root)

# Start GUI event loop
root.mainloop()