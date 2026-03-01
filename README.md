# Secure Password Generator (Python)

A simple command-line password generator written in Python.

This program generates a random password based on a user-defined length.  
It supports letters, digits, and special characters.

---

## Features

- User-defined password length
- Includes:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Input validation:
  - Rejects non-numeric input
  - Rejects non-positive numbers
  - Maximum length limit (128 characters)

---

## How It Works

The program:

1. Prompts the user to enter a password length.
2. Validates the input:
   - Must be a whole number
   - Must be greater than 0
   - Must not exceed 128 characters
3. Generates a random password using:
   - `string.ascii_letters`
   - `string.digits`
   - `string.punctuation`
4. Prints the generated password to the console.

The password is generated using Python’s built-in `random` module.

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How to Run

From the project directory:

```bash
python password_generator.py
```

Or (depending on your system):

```bash
python3 password_generator.py
```

---

## Example Usage

```
--- Secure Password Generator ---
Enter password length: 12
Your new password is: aB3#xT9!kLm2
```

If invalid input is provided:

```
Error: Invalid input. Please enter a whole number (e.g., 12).
```

---

## Project Structure

Single-file implementation:

```
password_generator.py
```

Main components:
- `generate_password(length)` – generates a random password
- Input validation logic inside `try/except` block

---

## Possible Improvements

- Guarantee at least one uppercase, lowercase, digit, and symbol
- Add option to exclude special characters
- Add option to copy password to clipboard
- Use `secrets` module instead of `random` for stronger security
- Add a graphical user interface (GUI)
