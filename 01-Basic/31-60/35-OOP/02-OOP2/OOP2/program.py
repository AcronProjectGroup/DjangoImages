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

house1.houseExplanation()
# Output:
    # This house color is Blue,
    # and have 4 number of room,
    # and is on the Berlin area,
    # And Country is Germany.
