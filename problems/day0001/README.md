# day0001

## 🚀 Problem

Write and run the very first Python program in this series. It should display a simple welcome message on the console.

## 💡 Approach

1. **`def`**:

   * Used to define a function in Python.
   * In your program, `solution()` is a function that contains the code to execute.

2. **Function name `solution`**:

   * This is the name of the function.
   * You can call it anywhere after it is defined.

3. **`print()`**:

   * A built-in Python function that outputs text to the console.
   * `print("Welcome to Python")` will display the message `Welcome to Python`.

4. **`if __name__ == "__main__":`**

   * This checks whether the Python file is being run directly or being imported as a module in another file.
   * If run directly, the condition is `True` and `solution()` is called.
   * If imported, the condition is `False` and `solution()` is **not** called automatically.

5. **`;` (semicolon)**:

   * Optional in Python.
   * Python uses newlines to separate statements, so semicolons are rarely needed. In your code, `print("Welcome to Python");` works the same as without the semicolon.

---