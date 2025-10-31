# Stack-Based Expression Evaluation (No-Class Version)

## Overview
This is a simplified Python version of the stack-based expression evaluator that uses **only lists and functions** — no classes.

## Files
- `stack_evaluator.py`: Main program file.
- `input.txt`: Sample input expressions.
- `output.txt`: Expected results.
- `README.md`: Instructions.

## How to Run
1. Place all files in the same folder.
2. Open the folder in VS Code or any terminal.
3. Run the program with:
   ```bash
   python stack_evaluator.py
   ```
4. The evaluated results will be saved in `output.txt`.

## Example
**Input (input.txt):**
```
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```

**Output (output.txt):**
```
13
-----
17
-----
-10
```
