# Avoid changing the list and dictionary in functions
# Avoid changing the list and dictionary in functions
# Avoid changing the list and dictionary in functions


a = [5, 1, 7]

b = a.copy()
b[0]= 13

# a[0] == ? = 5 yet
print(a)
# Output:
    # [5, 1, 7]


