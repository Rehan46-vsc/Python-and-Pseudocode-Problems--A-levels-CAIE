class HashTable:
    def __init__(self,size):  #Whats init? init can be used to assign values to certain objects
        self.size=size
        self.table=[None]*size #Line 3  helped us set the size for table and 4 helped us inititate the table by inputting false values.

    def insert(self,key):
        address=key % self.size
        for i in range(address,self.size): #now users or code inputs values in the table
            if self.table[i]==None:
                address=i
                self.table[address]=key #this if loop inputs user value if address stores dummy value
                return
            elif i==self.size: #Here we check if we reached the end of the table and we circle back creating a circled list as learnt in A1
                for j in range(0,address):
                    if self.table[j]==None:
                        address=j
                        self.table[address]=key
                        return
                    elif j==address: #table full so outputs valid message
                        print(f"{key} can not be stored since the entire table is full")
                        return
                    
                    
            
    
    def search(self, key):
        address=key % self.size #hashing algorithm- Uses MOD function as you have learnt over the years to assign addresses based on remainders when divided by the table size
        for i in range(address,self.size):
            if self.table[i]==key:
                address=i
                return address #pretty self explanatory
                return
            elif i==self.size-1:
                for j in range(0,address):
                    if self.table[j]==key:
                        address=j
                        return address
                    elif j==address:
                        print(f"{key} not found in table") #message for non-existent data
                        return
                    
    def display(self):
        for i, value in enumerate(self.table):
            print(i, ":", value)


#Mini project with user input an interactive project NOT NEEDED FOR A LEVELS THE CODE ABOVE IS ENOUGH

table_name = input("Enter table name: ")
size = int(input("Enter table size: "))

h = HashTable(size)

n = int(input("How many values do you want to insert? "))

for i in range(n):
    key = int(input(f"Enter value {i+1}: "))
    h.insert(key)

print(f"\n{table_name}:")
h.display()

search_key = int(input("\nEnter a value to search for: "))

position = h.search(search_key)

if position == -1:
    print(f"{search_key} was not found.")
else:
    print(f"{search_key} is at address {position}.")


#FINAL SUGGESTION:Try implementing bubble sort in your code, try looking at my profile for bubble sort code
#Feel free to test abnormal border datas on this code and improve the efficiency of this code
                    
                    
            
            
        

            
            


            
        
        


    
