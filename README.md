# Stacks and Queues

**Name:** Jed Norman H. Toniza **Section:** BSIT 2C

## About

This program shows how stacks and queues work using arrays and linked lists. It also has a parentheses checker and a small print queue program.

## Files

- `array_stack.py`— stack made with a fixed-size list.
- `linked_stack.py`  stack made with linked nodes.
- `array_queue.py` — circular queue made with a fixed-size list.
- `linked_queue.py ` — queue with front and rear nodes.
- `main.py` — menu for testing the four data structures. 
- `balanced_parentheses.py`  — checks matching parentheses, brackets, and braces.
- `print_queue.py`  — adds and prints jobs in first-in, first-out order.
- `analysis.md` — answers the analysis question.
- `sample_runs.md`  — example outputs for testing.

## Requirements

Python 3 is required. No extra packages are needed.

## Run the programs

Open a terminal in this folder and run:

```bash
python main.py
```

To run the parentheses checker:

```bash
python balanced_parentheses.py
```

To run the print queue:

```bash
python print_queue.py
```

## Things to test

-Push more than three items into the Array Stack to see overflow.
-Pop from an empty stack to see underflow.
-Enqueue more than three items into the Circular Array Queue to see overflow.
-Dequeue from an empty queue to see underflow.
-For queue wrap-around, enqueue A, B, C; dequeue A and B; then enqueue D and E. The order should be C, D, E.
-Try ({[]}) and ({[}) in the parentheses checker.
-Add several print jobs and check that the first job added prints first.

Upload the files individually to the GitHub repository (not zipped).
