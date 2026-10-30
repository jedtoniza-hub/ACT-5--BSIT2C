# Sample Runs

Run the programs and compare your output with these examples.

## Array Stack overflow

```text
Array Stack
1. Push
Enter a value: A
Pushed: A
Enter a value: B
Pushed: B
Enter a value: C
Pushed: C
Enter a value: D
Error: Stack overflow: the stack is full.
Current state: Stack (top -> bottom): ['C', 'B', 'A']
```

## Stack underflow

```text
Linked Stack
2. Pop
Error: Stack underflow: the stack is empty.
```

## Queue underflow

```text
Print queue
2. Print next job
Error: Queue underflow: the queue is empty.
```

## Circular queue wrap-around

```text
Enqueue: A, B, C
Dequeue: A
Dequeue: B
Enqueue: D
Enqueue: E
Queue (front -> rear): ['C', 'D', 'E']
```

## Balanced parentheses

```text
Enter an expression: ({[]})
The parentheses are balanced.

Enter an expression: ({[})
The parentheses are not balanced.
```

## Print queue

```text
Job ID: J1
Number of pages: 2
Job added.
Job ID: J2
Number of pages: 5
Job added.
Printing job J1 (2 page(s)).
Printing job J2 (5 page(s)).
```
