from app.operations import add, subtract, multiply, divide

HELP_TEXT = (
    "Commands:\n"
    "  add a b        -> adds a + b\n"
    "  subtract a b   -> subtracts a - b (shortcut: sub)\n"
    "  multiply a b   -> multiplies a * b (shortcut: mul)\n"
    "  divide a b     -> divides a / b (Shortcut: div)\n"
    "  help           -> show this message\n"
    "  exit           -> quit the program\n"
)

SHORTCUT = {
    "sub": "subtract",
    "mul": "multiply",
    "div": "divide",
}

def calculator():
    print("Welcome to the Calculator REPL! Type 'help' for commands, 'exit' to quit.")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        cmd_parts = user_input.split()

        cmd = cmd_parts[0].lower()

        if cmd == "help":
            print(HELP_TEXT)
            continue

        if cmd in ("exit", "quit"):
            print("Exiting calculator...")
            break

        cmd = SHORTCUT.get(cmd, cmd)

        if len(cmd_parts) != 3:
            print("Invalid input. Format: <operation> <num1> <num2>")
            continue

        try:
            a = float(cmd_parts[1])
            b = float(cmd_parts[2])

            if cmd == "add":
                print(f"Result: {add(a, b)}")
            elif cmd == "subtract":
                print(f"Result: {subtract(a, b)}")
            elif cmd == "multiply":
                print(f"Result: {multiply(a, b)}")
            elif cmd == "divide":
                print(f"Result: {divide(a, b)}")
            else:
                print("Invalid operation. Type 'help' for a list of commands.")

        except ValueError as e:
            print(e)
