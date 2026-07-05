#We will write corresponding python code of our pseudocode to follow cambridge protocol

mylist=[32,46,53,67,71,80,93,136,249] #Array of length 9
def binarysearch(mylist): #Function for binary search
    upperbound=len(mylist)-1 #python has a different counting system the lower bound starts from 0 and upper bound ends at final-1
    lowerbound=0
    searchitem=int(input(f"Enter value to be found in list")) #value to be found
    notfound=True #efficiency using boolean flag
    while notfound and lowerbound<=upperbound:#lowerbound<=upperbound to ensure that the entire list has been checked
        index=(upperbound+lowerbound)//2 #gets middle value's address to compare with value to be found
        if searchitem== mylist[index]: #checks if middle value is the target value
            notfound=False #if it is the value not found becomes false which means the code will stop
            found=index+1 #to find the position of the value
        elif searchitem>mylist[index]: 
            lowerbound=index+1 #takes right half for the values greater than value to be found 
        elif searchitem<mylist[index]:
            upperbound=index-1 #take left half for values less than value to be found

    if notfound:
        print(f"{searchitem} not found in list")
    else:
        #small code to assign suffix to position of the item
        if 11 <= found % 100 <= 13:
            suffix = "th"
        elif found % 10 == 1:
            suffix = "st"
        elif found % 10 == 2:
            suffix = "nd"
        elif found % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"

        print(f"{searchitem} is at the {found}{suffix} position.")
    
binarysearch(mylist)



