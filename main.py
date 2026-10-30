from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def run_stack(stack, label):
    while True:
        print(f"\n{label}: {stack}")
        print("1. Push\n2. Pop\n3. Peek\n4. Check empty\n5. Check full\n0. Back")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Enter a value: ").strip()
                stack.push(value)
                print("Pushed:", value)
            elif choice == "2":
                print("Popped:", stack.pop())
            elif choice == "3":
                print("Top element:", stack.peek())
            elif choice == "4":
                print("Is empty?", stack.is_empty())
            elif choice == "5":
                print("Is full?", stack.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid option.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
        print("Current state:", stack)


def run_queue(queue, label):
    while True:
        print(f"\n{label}: {queue}")
        print("1. Enqueue\n2. Dequeue\n3. Peek front\n4. Check empty\n5. Check full\n0. Back")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Enter a value: ").strip()
                queue.enqueue(value)
                print("Enqueued:", value)
            elif choice == "2":
