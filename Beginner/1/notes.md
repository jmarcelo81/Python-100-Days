# Day 1 - Printing, Commenting, Debugging, String Manipulation and Variables

## Overview
Learn the fundamentals: printing text, using comments, string manipulation, and storing data in variables.

## Key Resources
- [Stack Overflow](https://stackoverflow.com) — search for code errors
- [W3Schools Python Docs](https://www.w3schools.com/python/) — reference

---

## Task 1: Print Statement

Use the `print()` function to output text to the console. Text inside double quotes is a **string**.

```python
print("Hello World!")
```

### Exercise: Recipe Instructions
```python
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
```

---

## Task 2: String Manipulation

### Concatenation
Merge strings together with `+`. **Note:** Spaces matter!

```python
print("Hello" + "Marcelo")  # Output: HelloMarcelo
print("Hello " + "Marcelo")  # Output: Hello Marcelo
```

### Escape Sequences
Use `\n` for newlines:

```python
print("Hello world!\nHello world!")
# Output:
# Hello world!
# Hello world!
```

---

## Task 3: User Input

Use `input()` to collect data from the user and incorporate it into your code.

```python
print("Hello " + input("What is your name? ") + "!")
```

**Example run:**
What is your name? Marcelo
Hello Marcelo!

---

## Task 4: Variables

Variables are named containers that store values. Use them to reference data throughout your code.

```python
name = input("What is your name? ")
print(name)
```

### Getting String Length

```python
name = input("What is your name? ")
print(len(name))  # Prints the number of characters
```

### Exercise: Swap Variables

Given two variables, swap their contents **without** using the literal values:

```python
glass1 = "milk"
glass2 = "juice"

# Solution (using a temporary variable)
new_glass1 = glass2
glass2 = glass1
glass1 = new_glass1

print(glass1)  # Output: juice
print(glass2)  # Output: milk
```

---

## Final Project: Band Generator

```python
print("Welcome to the Band Generator")
city = input("What city did you grow up in?\n")
pet = input("What is the name of your current or former pet?\n")

print("Your band name could be: " + city + " " + pet)
```

**Example:**
Welcome to the Band Generator
What city did you grow up in?
Waukesha
What is the name of your current or former pet?
Daisy
Your band name could be: Waukesha Daisy

Process finished with exit code 0
