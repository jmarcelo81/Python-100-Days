# Day 2 - Data Types, Numbers, Operations, Type Conversion, f-Strings

## Overview
Learn Python's primitive data types, mathematical operations, type conversion, and f-strings for string formatting.

---

## 1. Python Primitive Data Types

### A. String
Extract characters using **subscripting** (index notation). Indexing starts at **0**.

```python
print("Hello"[0])   # Output: H
print("Hello"[3])   # Output: l
print("Hello"[4])   # Output: o
```

### B. Integer
Whole numbers without decimals. Use `_` for readability in large numbers.

```python
print(199_000)  # Output: 199000 (more readable than 199000)
```

### C. Float
Numbers with decimal points.

```python
print(3.14)
print(type(3.14))  # Output: <class 'float'>
```

### D. Boolean
Two values: `True` or `False`.

```python
print(True)  # Output: True
```

---

## 2. Type Error, Type Checking, and Type Conversion

### Type Error
Occurs when you use the wrong data type with a function. Example:

```python
len(12345)  # ❌ TypeError: object of type 'int' has no len()
len("12345")  # ✅ Output: 5
```

### Type Checking
Use `type()` to check any value's data type:

```python
print(type("String"))      # <class 'str'>
print(type(123))           # <class 'int'>
print(type(456.789))       # <class 'float'>
print(type(True))          # <class 'bool'>
```

### Type Conversion
Convert between types using `str()`, `int()`, `float()`:

```python
name_length = input("Enter your name: ")
print("Number of letters in your name: " + str(len(name_length)))
```

**Example:**
Enter your name: Francesca
Number of letters in your name: 9


---

## 3. Mathematical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `5 - 3` → `2` |
| `*` | Multiplication | `5 * 3` → `15` |
| `**` | Exponent | `5 ** 2` → `25` |
| `/` | Division (float) | `6 / 2` → `3.0` |
| `//` | Division (integer) | `7 // 2` → `3` |
| `%` | Modulus (remainder) | `7 % 2` → `1` |

### Order of Operations: PEMDAS
Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

```python
print(3 * 3 + 3 / 3 - 3)         # Output: 7.0
print(3 * (3 + 3 / 3 - 3))       # Output: 3.0
```

### Exercise: BMI Calculator

Formula: `BMI = weight / (height²)`

```python
height = 1.65
weight = 84

bmi = weight / (height * height)
print(bmi)  # Output: ~30.86
```

---

## 4. Number Manipulation and f-Strings

### Rounding
```python
print(round(10 / 3, 2))  # Output: 3.33 (2 decimal places)
```

### f-Strings
Python f-strings allow you to embed expressions in curly braces `{}`:

```python
score = 86
print(f"Your score is {score}")  # Output: Your score is 86
```

**More examples:**
```python
age = 25
print(f"In 10 years, you'll be {age + 10}")  # Output: In 10 years, you'll be 35
print(f"Pi rounded: {round(3.14159, 2)}")    # Output: Pi rounded: 3.14
```

### Exercise: Life in Weeks

Calculate how many days, weeks, and months you have left if you live to 90:

```python
age = int(input("What is your current age? "))
days = (90 - age) * 365
weeks = (90 - age) * 52
months = (90 - age) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
```

**Example:**
What is your current age? 25
You have 23725 days, 3380 weeks, and 780 months left.


---

## Final Project: Tip Calculator

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill = tip / 100 * bill + bill
share_per_person = total_bill / people

print(f"Each person should pay: ${round(share_per_person, 2)}")
```

**Example:**
Welcome to the tip calculator!
What was the total bill? $64.27
What percentage tip would you like to give? 10 12 15 15
How many people to split the bill? 5
Each person should pay: $14.78
