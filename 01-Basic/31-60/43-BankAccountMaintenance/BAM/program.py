class Deposit:
    def __init__(self, name, AmountOfMoney = 0):
        self.owner = name
        self.AmountOfMoney = AmountOfMoney
    
    def __str__(self):
        return f'Owner: {self.owner} | Amount: ${self.AmountOfMoney} '

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.owner}, amount={self.AmountOfMoney})'

    def __add__(self, other):
        name = f'{self.owner}+{other.owner}'
        amount = self.AmountOfMoney + other.AmountOfMoney
        return Deposit(name, amount)

    def __iadd__(self, other):
        self.AmountOfMoney += other.AmountOfMoney
        other.AmountOfMoney = 0
        return self

    def __eq__(self, other):
        return self.AmountOfMoney == other.AmountOfMoney

    def Transfer(self, other, amount):
        if self.AmountOfMoney < amount:
            print("Not anough money.")
            return
        self.AmountOfMoney -= amount
        other.AmountOfMoney += amount

Jina = Deposit('Jina', 1000)
print(Jina)
print(repr(Jina))
# Output:
    # Owner: Jina | Amount: $1000 
    # Deposit(name=Jina, amount=1000)

Mina = Deposit('Mina', 2304)
print(Jina + Mina)
# Output:
    # Owner: Jina+Mina | Amount: $3304 


Jina += Mina
print("Jina:",Jina)
print("Mina:",Mina)
# Output:
    # Jina: Owner: Jina | Amount: $3304 
    # Mina: Owner: Mina | Amount: $0 

Sina = Deposit("Sina", 9231)
Bina = Deposit("Bina", 9231)
print(Sina == Bina)
# Output:
    # True

