class Deposit:
    def __init__(self, name, AmountOfMoney = 0):
        self.owner = name
        self.AmountOfMoney = AmountOfMoney
    
    def __str__(self):
        return f'Owner: {self.owner} | Amount: ${self.AmountOfMoney} '

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.owner}, amount={self.AmountOfMoney})'

Jina = Deposit('Jina', 1000)
print(Jina)
print(repr(Jina))

# Output:
    # Owner: Jina | Amount: $1000 
    # Deposit(name=Jina, amount=1000)
