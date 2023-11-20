a = 2
b = a
b = 3
print(a, b)
# Output:
# 2 3

List1 = [0, 1, 2]
List2 = List1
List2[0] = 99
# List1[0] == ?
# Output List1[0] == 99

print("List1=", List1)
print("List2=", List2)
# Output:
# List1= [99, 1, 2]
# List2= [99, 1, 2]


def Function(ListNumbers):
    ListNumbers.append(77)


AnotherListNumbers = [13, 14, 54]
print(AnotherListNumbers) # Output = [13, 14, 54] 
Function(AnotherListNumbers) # Output = None but -> + 77 to AnotherListNumbers
print(AnotherListNumbers) # Output = [13, 14, 54, 77]
# Output:
    # [13, 14, 54]
    # [13, 14, 54, 77]



def AnothFunc(Diction):
    Diction['key1'] = 'value1'

AnotherDictionary = {
    'k1': 'v1',
    'k2': 'v2',
}
print(AnotherDictionary)
AnothFunc(AnotherDictionary)
print(AnotherDictionary)
# Output:
    # {'k1': 'v1', 'k2': 'v2'}
    # {'k1': 'v1', 'k2': 'v2', 'key1': 'value1'}



 