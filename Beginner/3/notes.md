# Day 3 - Conditional Statements, Logical Operators, Code Blocks and Scope

## Overview
Learn how to make decisions in code using conditional statements (`if`, `elif`, `else`), logical operators (`and`, `or`, `not`), and understand code blocks and scope.

---

## 1. Conditional Statements: if-else

Basic syntax:

```python
if condition:
    do this
else:
    do the other one
```

### Example: Rollercoaster Height Limit

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster!")
```

**Key points:**
- `if` and `else` must be at the same indentation level
- Use `>=` or `<=` to include the boundary value
- Use `==` to compare equality (not `=` which assigns)

### The Modulo Operator: `%`

Returns the **remainder** of division. Useful for checking even/odd:

```python
10 % 5   # Output: 0 (no remainder)
10 % 3   # Output: 1 (remainder is 1)
```

### Exercise: Odd or Even Checker

```python
print("Welcome to the odd or even integer checker")
num_given = int(input("What is your number? "))

if num_given % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

---

## 2. Nested if-else Statements

Use `elif` for multiple conditions:

```python
if condition:
    do this
elif condition:
    do that
else:
    do the other one
```

### Example: Rollercoaster with Age-Based Pricing

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    if age < 12:
        print("You must pay $5!")
    elif age <= 18:
        print("You must pay $7!")
    else:
        print("You must pay $12!")
else:
    print("Sorry, you are not allowed to ride this rollercoaster")
```

---

## 3. Multiple if-else in Succession

Chain multiple conditions and use variables to track state:

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    price = 0
    
    if age < 12:
        price = 5
        print("The Child Cost is $5")
    elif age <= 18:
        price = 7
        print("The Teenager Cost is $7")
    elif not (age >= 45 and age <= 55):
        price = 12
        print("The Adult Cost is $12")
    else:
        price = 0
        print("For those between 45-55 years old, tickets are free!")
    
    buyPhoto = input("Do you want photos? [Yes|No] ")
    if buyPhoto == "Yes":
        price += 3
        print("The extra cost for photos is $3!")
    
    print(f"You must pay ${price}!")
else:
    print("Sorry, you are not allowed to ride this rollercoaster")
```

---

## 4. Logical Operators

### `and` — Both conditions must be True

```python
age = 25
if age >= 18 and age <= 65:
    print("You are eligible to work")
```

### `or` — At least one condition must be True

```python
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
```

### `not` — Negates the condition

```python
age = 50
if not (age >= 45 and age <= 55):
    print("Not in the senior discount range")
```

**Truth table:**

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T       | T      | F     |
| T | F | F       | T      | F     |
| F | T | F       | T      | T     |
| F | F | F       | F      | T     |

---

## Key Takeaways

✅ Use `if`, `elif`, `else` for decision-making  
✅ `==` for comparison, `=` for assignment  
✅ Indentation matters—it defines code blocks  
✅ `%` (modulo) finds remainders  
✅ `and`, `or`, `not` combine conditions  
✅ Nested conditions for complex logic
