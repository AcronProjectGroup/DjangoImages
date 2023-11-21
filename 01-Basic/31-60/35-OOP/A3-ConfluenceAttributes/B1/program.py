class House:
    Country = "Germany" # This is Class Attribute


    def __init__(self, color, numberRooms, Area):
        self.color = color  # This is Instance Attribute
        self.numberRooms = numberRooms
        self.area = Area

    def houseExplanation(self):
        print(
            f"This house color is {self.color},\n"
            f"and have {self.numberRooms} number of room,\n"
            f"and is on the {self.area} area,\n"
            f"And Country is {self.Country}."
        )

 
house1 = House("Blue", 4, "Berlin")

house1.Country = "Another Count"
print(house1.Country)
del house1.Country  # If before delete class attribute you difined another value for it
                    #  Python don't arise an error
print(house1.Country)

# Output:
    # Another Count
    # Germany