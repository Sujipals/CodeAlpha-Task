# Hangman GUI

A classic Hangman word-guessing game with a graphical user interface built using Python's **Tkinter** library.

## 🎮 Overview

This project is an interactive implementation of the traditional Hangman game. Players guess letters to reveal a hidden word before running out of incorrect guesses. The game features a clean GUI with clickable letter buttons and instant feedback.

## ✨ Features

- **Interactive GUI**: Built with Tkinter for a user-friendly experience
- **Alphabet Buttons**: Click any letter A-Z to make your guess
- **Real-time Feedback**: Instant visual updates showing:
  - Revealed letters in the word
  - Remaining wrong guesses
- **Word List**: Pre-defined collection of words covering programming-related topics
- **Auto-Reset**: Game automatically resets after winning or losing
- **Disabled Buttons**: Already-guessed letters are disabled to prevent re-selection
- **Win/Lose Dialogs**: Clear notifications with the solution revealed

## 📋 Game Rules

1. A random word is selected from the word list
2. The word is initially hidden as underscores (e.g., `_ _ _ _ _`)
3. Click letter buttons to guess
4. Each correct guess reveals all instances of that letter
5. Each incorrect guess reduces your remaining attempts
6. **Win**: Reveal all letters before running out of guesses
7. **Lose**: Run out of guesses (max 6 wrong guesses allowed)

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Sujipals/CodeAlpha-Task.git
cd CodeAlpha-Task
```

2. Run the game:
```bash
python hangman_gui.py
```

## 📁 Project Structure

```
CodeAlpha-Task/
├── hangman_gui.py          # Main game implementation
├── README.md               # Project documentation
└── .github/
    └── workflows/
        ├── python-lint.yml # Code quality checks
        └── tests.yml       # Test automation
```

## 🎯 How to Play

1. **Launch the Game**: Run the Python script
2. **Guess Letters**: Click any letter button to make a guess
3. **Track Progress**: Monitor the word reveal and remaining guesses
4. **Win or Lose**: Follow the on-screen message
5. **Play Again**: The game resets automatically for the next round

## 💡 Code Structure

### HangmanGame Class

The main game logic is encapsulated in the `HangmanGame` class:

- **`__init__`**: Initializes the game window and UI elements
- **`create_letter_buttons`**: Generates clickable buttons for the alphabet
- **`guess_letter`**: Handles letter selection and game logic
- **`reset_game`**: Resets state for a new round

### Key Variables

- `word`: The current word to be guessed
- `guessed_word`: List tracking revealed letters
- `wrong_guesses`: Counter for incorrect guesses
- `max_wrong`: Maximum allowed wrong guesses (default: 6)

## 🔧 Customization

### Adding More Words

Edit the `words` list in `hangman_gui.py`:

```python
words = ["python", "flask", "coding", "developer", "program"]
```

### Adjusting Difficulty

Modify `max_wrong` to change difficulty:

```python
self.max_wrong = 4  # Harder
self.max_wrong = 8  # Easier
```

### Styling

Adjust fonts and window properties:

```python
self.word_label = tk.Label(root, text=" ".join(self.guessed_word), font=("Arial", 28))
```

## 📝 Requirements

- Python 3.6+
- tkinter (standard library)

## 🔄 CI/CD Workflows

This project includes automated workflows for:

- **Code Linting**: Validates Python code quality using Pylint
- **Tests**: Runs automated tests to ensure code reliability

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/Sujipals/CodeAlpha-Task/issues) on GitHub.

## 👨‍💻 Author

**Sujipals** - [GitHub Profile](https://github.com/Sujipals)

---

**Enjoy the game! 🎉**
