# Assignment: Leap Year Checker (Python)

## Overview
In this assignment, you will build a Python program that determines whether a given year is a leap year. This task practices conditional logic, modulo operations, and clear input/output handling.

## Requirements
Your program must:

- Read one integer from input (the year).
- Determine whether the year is a leap year using the rules below:
  - If the year is divisible by 400, it is a leap year.
  - If the year is divisible by 100, it is not a leap year.
  - If the year is divisible by 4, it is a leap year.
  - Otherwise, it is not a leap year.
- Print the result exactly as:
  - `Leap year`
  - `Not a leap year`

## Input
A single integer representing a year.

## Output
A single line:
- `Leap year`
- `Not a leap year`

## Examples

**Input**
```
2000
```

**Output**
```
Leap year
```

**Input**
```
1900
```

**Output**
```
Not a leap year
```

**Input**
```
2024
```

**Output**
```
Leap year
```

**Input**
```
2023
```

**Output**
```
Not a leap year
```

## Starter File
Create a file named `main.py` that reads input using `input()` and prints the result using `print()`.

## Evaluation Criteria (Rubric)
- 40%: Correct leap year logic for all four rules
- 30%: Exact output format
- 20%: Clear and readable code
- 10%: Extra test cases or clean function structure

## Suggested Autograding Tests
- `2000` -> `Leap year`
- `1900` -> `Not a leap year`
- `2024` -> `Leap year`
- `2023` -> `Not a leap year`
- `2400` -> `Leap year`
- `2100` -> `Not a leap year`

## Task ID
Task ID: TASK-1
