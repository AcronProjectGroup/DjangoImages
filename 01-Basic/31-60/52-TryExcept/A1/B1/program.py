ListNumbers = [100, -10, 30, 46, 11]

print(f"List of Numbers: {ListNumbers}")
print("Select just one")
index = int(input("Index 0-5? "))

def GetNumber(List, index):
    return List[index]

print(GetNumber(ListNumbers, index))

# Input = 10
    # ist of Numbers: [100, -10, 30, 46, 11]
    # Select just one
    # Index 0-5? 6
# Output:
    # Traceback (most recent call last):
    # File "/home/sina/01-Repo/6 DjangoWA/01-Basic/31-60/52-TryExcept/TryExpt/A1/program.py", line 10, in <module>
    #     print(GetNumber(ListNumbers, index))
    #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # File "/home/sina/01-Repo/6 DjangoWA/01-Basic/31-60/52-TryExcept/TryExpt/A1/program.py", line 8, in GetNumber
    #     return List[index]
    #         ~~~~^^^^^^^
    # IndexError: list index out of range

