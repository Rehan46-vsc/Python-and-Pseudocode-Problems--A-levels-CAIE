#We will be writing our entire code for ascending order feel free to try descending order too.
#Python doesn't have array so we will be using lists
def bubblesort(arr):
    Boundary= len(arr)-1
    swapped=False #notice 6 follows efficiency rule from README
    while not swapped:
        swapped=True
        for i in range(Boundary):
            if arr[i]>arr[i+1]:#Checks for adjacent value for a possible swap
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swapped=False#If there is a swap continues whole pass or else stops the algorithm(boosts efficiency)
        n-=1 #follows efficiency rule as there is reduced looping each time
    return arr
#This is for user inputs in a list needed in A-2   
arr=[]
length=int(input("Input length of array:"))

for i in range(length):
    number=int(input(f"Input {i+1}th value"))
    arr.append(number)

print(f"Original list: \n ",arr)
bubblesort(arr)
print("List after sorting: \n",arr)






