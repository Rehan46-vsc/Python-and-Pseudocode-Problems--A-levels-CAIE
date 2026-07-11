# Stack variables
STACK_SIZE = int(input("Enter stack size: "))
stack = [""] * STACK_SIZE
top = 0


# Let's reset the stack first
def reset_stack():
    global top #Global variables top this value is used everywhere and updated everywhere
    top = 0


def push(item):
    global top #Global variables top this value is used everywhere and updated everywhere

    # Check stack isn't full
    if top < STACK_SIZE:
        stack[top] = item
        top += 1 
        print(f"Pushed {item} at index {top - 1}")
    else:
        print(f"Stack is full - can't push {item}")


def pop():
    global top #Again global variable is used

    if top > 0:
        item = stack[top - 1]
        top -= 1
        return item
    else:
        print("Error - nothing to pop")
        return ""


# Reset the stack
reset_stack()

# Inputting elements into the stack using the push procedure
for i in range(STACK_SIZE):
    a = input("Enter element to be inserted: ")
    push(a)


# Display stack
print("\nCurrent Stack:")
print(stack)

# Example of popping
print("\nPopped:", pop())
print("Stack after pop:")
print(stack)


#Quick question: Why was top used as a global variable?
#Answer:Top is a global varaible because it stores the current position of the stack.Both the Push and pop operation use 
#variable top and for that reason to maintain cohesion between those two operations we create a variable that links the position of the stack. Therefore it is a global variable
