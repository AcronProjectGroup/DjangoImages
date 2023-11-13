names = ['Sina', 'Lina', 'Jina']
marks = [20, 25, 30]
ages = [44, 55, 66]


for index, numbers in enumerate(names):
    print(index, numbers)

for index, name in enumerate(names):
    print(f'name={name}, mark={marks[index]}, age={ages[index]}')

