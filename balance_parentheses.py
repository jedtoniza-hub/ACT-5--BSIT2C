from linked_stack import LinkedStack


def is_balanced(text):
    stack = LinkedStack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for character in text:
        if character in "([{":
            stack.push(character)
        elif character in ")]}":
            if stack.is_empty() or stack.pop() != pairs[character]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    text = input("Enter an expression: ")
    if is_balanced(text):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")
