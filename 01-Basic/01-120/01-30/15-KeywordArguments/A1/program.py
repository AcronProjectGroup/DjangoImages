# Keyword Arguments
def SumAny(**kwargs):
    print(kwargs)


SumAny(
    a=1,
    name="Sina",
    SureName='LalehBakhsh',
    year=30,
)
# Output:
    # 6
    # {'a': 1, 'name': 'Sina', 'SureName': 'LalehBakhsh', 'year': 30}




def SumEveryThingS(*args, **kwargs):
    print(args)
    print(kwargs)

SumEveryThingS(1,3,'Sina',First='is one', second='defenetly two!!', third='is bird!')
# Output:
    # ...
    # (1, 3, 'Sina')
    # {'First': 'is one', 'second': 'defenetly two!!', 'third': 'is bird!'}

