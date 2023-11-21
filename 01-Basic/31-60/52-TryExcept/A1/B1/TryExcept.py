ListNumbers = [100, -10, 30, 46, 11]

print(f"List of Numbers: {ListNumbers}")
print("Select just one")
index = int(input("Index 0-5? "))

def GetNumber(List, index):
    return List[index]

try:
    print(GetNumber(ListNumbers, index))
except:
    print("Invalid Index ...")

# Input: 
    # List of Numbers: [100, -10, 30, 46, 11]
    # Select just one
    # Index 0-5? 6
    
# Output:
    # Invalid Index ...

