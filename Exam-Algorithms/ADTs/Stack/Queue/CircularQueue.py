QUEUE_SIZE = 5

Queue = [""] * QUEUE_SIZE

FrontPointer = 0
EndPointer = 0
NumItemsInQueue = 0


def Enqueue(item):
    global EndPointer, NumItemsInQueue

    # Check queue not full
    if NumItemsInQueue < QUEUE_SIZE:

        EndPointer += 1

        # Wrap around if required
        if EndPointer > QUEUE_SIZE:
            EndPointer = 1

        Queue[EndPointer - 1] = item    # Python uses index 0

        NumItemsInQueue += 1

        print(f'Enqueued "{item}" at index {EndPointer}')

    else:
        print(f'Queue full - can\'t enqueue "{item}"')


def Dequeue():
    global FrontPointer, NumItemsInQueue

    # Check queue not empty
    if NumItemsInQueue > 0:

        FrontPointer += 1

        # Wrap around if required
        if FrontPointer > QUEUE_SIZE:
            FrontPointer = 1

        NumItemsInQueue -= 1

        return Queue[FrontPointer - 1]

    else:
        return "Queue empty - can't dequeue"


# Example
Enqueue("A")
Enqueue("B")
Enqueue("C")

print(Dequeue())
print(Dequeue())

Enqueue("D")
Enqueue("E")
Enqueue("F")

print(Queue)
