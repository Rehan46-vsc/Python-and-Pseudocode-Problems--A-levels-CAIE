# Queue implementation using a linear queue

QUEUE_SIZE = int(input("Queue Size?: "))

Queue = [""] * QUEUE_SIZE
FrontPointer = 0
EndPointer = 0


def Enqueue(data):
    global FrontPointer, EndPointer

    # Check if queue is not full
    if EndPointer < QUEUE_SIZE:

        # Handle empty queue
        if FrontPointer == 0:
            FrontPointer = 1

        EndPointer += 1
        Queue[EndPointer - 1] = data      # Python lists start at index 0

        print(f'Enqueued "{data}" at index {EndPointer}')

    else:
        print(f'Can\'t enqueue "{data}" - queue full')


def Dequeue():
    global FrontPointer

    # Check queue is not empty
    if FrontPointer > 0 and FrontPointer <= EndPointer:

        data = Queue[FrontPointer - 1]
        FrontPointer += 1

        return data

    else:
        print("Queue empty - nothing to dequeue")
        return ""


# Example usage
Enqueue("Apple")
Enqueue("Banana")
Enqueue("Orange")

print("Dequeued:", Dequeue())
print("Dequeued:", Dequeue())

Enqueue("Mango")

print("\nCurrent Queue:")
print(Queue)
