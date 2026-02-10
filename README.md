# Module 2 Calculator Assignment

This is a simple command-line calculator written in Python.  
It supports addition, subtraction, multiplication, and division using a REPL (Read–Eval–Print Loop) interface.

The project includes automated unit tests using pytest and continuous integration using GitHub Actions.

---

## Features

- Add, subtract, multiply, divide  
- REPL command-line interface  
- Shortcut commands (add, sub, mul, div)  
- Error handling (invalid input, divide by zero)  
- Automated tests with pytest  
- GitHub Actions CI  

---

## Setup

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Calculator

```bash
python main.py
```

---

## Run Tests

```bash
pytest
```

---

## Continuous Integration

Tests automatically run on every push using GitHub Actions.